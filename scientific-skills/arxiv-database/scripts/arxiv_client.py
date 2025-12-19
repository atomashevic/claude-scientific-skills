#!/usr/bin/env python3
"""
ArXiv API Client for searching and browsing preprints.

Provides a robust client for interacting with the ArXiv API with:
- Rate limiting (respects 3-second recommendation)
- Exponential backoff retry logic
- Caching support
- Multiple output formats (JSON, BibTeX, CSV)
- Keyword highlighting in abstracts
- Batch operations
"""

import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional, Any, Set
from datetime import datetime, timedelta
import time
import re
import json
import hashlib
from pathlib import Path


class ArxivClient:
    """Client for interacting with the ArXiv API."""
    
    BASE_URL = "http://export.arxiv.org/api/query"
    NS = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
    
    def __init__(
        self, 
        rate_limit_delay: float = 3.0,
        cache_dir: Optional[str] = None,
        cache_ttl_hours: int = 24,
        max_retries: int = 3,
        timeout: int = 30
    ):
        """
        Initialize ArXiv client.
        
        Args:
            rate_limit_delay: Seconds to wait between requests (default: 3.0)
            cache_dir: Directory for caching results (None to disable)
            cache_ttl_hours: Cache time-to-live in hours (default: 24)
            max_retries: Maximum retry attempts for failed requests
            timeout: Request timeout in seconds
        """
        self.rate_limit_delay = rate_limit_delay
        self.last_request_time = 0
        self.max_retries = max_retries
        self.timeout = timeout
        
        # Setup caching
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.cache_ttl = timedelta(hours=cache_ttl_hours)
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def _rate_limit(self):
        """Enforce rate limiting between requests."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)
        self.last_request_time = time.time()
    
    def _get_cache_key(self, params: Dict) -> str:
        """Generate cache key from request parameters."""
        param_str = json.dumps(params, sort_keys=True)
        return hashlib.md5(param_str.encode()).hexdigest()
    
    def _get_cached(self, cache_key: str) -> Optional[List[Dict]]:
        """Retrieve cached results if valid."""
        if not self.cache_dir:
            return None
        
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    cached = json.load(f)
                
                cached_time = datetime.fromisoformat(cached['timestamp'])
                if datetime.now() - cached_time < self.cache_ttl:
                    return cached['results']
            except (json.JSONDecodeError, KeyError):
                pass
        
        return None
    
    def _set_cached(self, cache_key: str, results: List[Dict]):
        """Cache results."""
        if not self.cache_dir:
            return
        
        cache_file = self.cache_dir / f"{cache_key}.json"
        with open(cache_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'results': results
            }, f)
    
    def _parse_entry(self, entry) -> Dict:
        """Parse an ArXiv entry element into a dictionary."""
        # Extract ArXiv ID from URL
        id_elem = entry.find('atom:id', self.NS)
        arxiv_url = id_elem.text if id_elem is not None else ""
        arxiv_id = arxiv_url.split('/')[-1] if arxiv_url else ""
        
        # Remove version from ID for base ID
        base_id = re.sub(r'v\d+$', '', arxiv_id)
        
        # Title
        title_elem = entry.find('atom:title', self.NS)
        title = title_elem.text.strip().replace('\n', ' ') if title_elem is not None else ""
        title = re.sub(r'\s+', ' ', title)  # Normalize whitespace
        
        # Authors
        authors = []
        affiliations = []
        for author in entry.findall('atom:author', self.NS):
            name_elem = author.find('atom:name', self.NS)
            if name_elem is not None:
                authors.append(name_elem.text)
            
            aff_elem = author.find('arxiv:affiliation', self.NS)
            if aff_elem is not None:
                affiliations.append(aff_elem.text)
        
        # Abstract
        summary_elem = entry.find('atom:summary', self.NS)
        abstract = summary_elem.text.strip() if summary_elem is not None else ""
        abstract = re.sub(r'\s+', ' ', abstract)  # Normalize whitespace
        
        # Published date
        published_elem = entry.find('atom:published', self.NS)
        published = published_elem.text if published_elem is not None else ""
        try:
            published_dt = datetime.fromisoformat(published.replace('Z', '+00:00'))
        except ValueError:
            published_dt = None
        
        # Updated date
        updated_elem = entry.find('atom:updated', self.NS)
        updated = updated_elem.text if updated_elem is not None else ""
        try:
            updated_dt = datetime.fromisoformat(updated.replace('Z', '+00:00'))
        except ValueError:
            updated_dt = None
        
        # Primary category
        primary_cat_elem = entry.find('arxiv:primary_category', self.NS)
        primary_category = primary_cat_elem.get('term') if primary_cat_elem is not None else ""
        
        # All categories
        categories = [cat.get('term') for cat in entry.findall('atom:category', self.NS)]
        
        # Links
        links = {}
        for link in entry.findall('atom:link', self.NS):
            rel = link.get('rel', 'alternate')
            href = link.get('href', '')
            link_type = link.get('type', '')
            if link_type == 'application/pdf':
                links['pdf'] = href
            elif rel == 'alternate':
                links['abstract'] = href
            else:
                links[rel] = href
        
        # DOI (if available)
        doi_elem = entry.find('arxiv:doi', self.NS)
        doi = doi_elem.text if doi_elem is not None else None
        
        # Journal reference (if published)
        journal_ref_elem = entry.find('arxiv:journal_ref', self.NS)
        journal_ref = journal_ref_elem.text if journal_ref_elem is not None else None
        
        # Comments
        comment_elem = entry.find('arxiv:comment', self.NS)
        comment = comment_elem.text if comment_elem is not None else None
        
        return {
            'arxiv_id': arxiv_id,
            'base_id': base_id,
            'title': title,
            'authors': authors,
            'affiliations': affiliations,
            'abstract': abstract,
            'published': published_dt.strftime('%Y-%m-%d') if published_dt else "",
            'published_datetime': published_dt.isoformat() if published_dt else None,
            'updated': updated_dt.strftime('%Y-%m-%d') if updated_dt else "",
            'updated_datetime': updated_dt.isoformat() if updated_dt else None,
            'primary_category': primary_category,
            'categories': categories,
            'doi': doi,
            'journal_ref': journal_ref,
            'comment': comment,
            'arxiv_url': f"https://arxiv.org/abs/{base_id}",
            'pdf_url': f"https://arxiv.org/pdf/{base_id}.pdf",
            'links': links
        }
    
    def _make_request(self, params: Dict) -> List[Dict]:
        """Make API request with retry logic."""
        # Check cache first
        cache_key = self._get_cache_key(params)
        cached = self._get_cached(cache_key)
        if cached is not None:
            return cached
        
        for attempt in range(self.max_retries):
            try:
                self._rate_limit()
                response = requests.get(self.BASE_URL, params=params, timeout=self.timeout)
                
                if response.status_code == 200:
                    root = ET.fromstring(response.content)
                    entries = root.findall('atom:entry', self.NS)
                    
                    # Check for error response (empty entry with only id)
                    if len(entries) == 1:
                        entry = entries[0]
                        title = entry.find('atom:title', self.NS)
                        if title is not None and title.text and 'Error' in title.text:
                            raise Exception(f"ArXiv API Error: {title.text}")
                    
                    papers = [self._parse_entry(entry) for entry in entries]
                    
                    # Cache results
                    self._set_cached(cache_key, papers)
                    
                    return papers
                
                elif response.status_code >= 500:
                    # Server error - retry with backoff
                    wait_time = 2 ** attempt
                    print(f"Server error ({response.status_code}). Waiting {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    response.raise_for_status()
            
            except requests.exceptions.Timeout:
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Request timeout. Waiting {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise Exception(f"Request timed out after {self.max_retries} retries")
            
            except requests.exceptions.ConnectionError:
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Connection error. Waiting {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise Exception(f"Connection failed after {self.max_retries} retries")
            
            except ET.ParseError as e:
                raise Exception(f"Failed to parse ArXiv response: {e}")
        
        raise Exception(f"Failed after {self.max_retries} retries")
    
    def search(
        self, 
        query: str,
        max_results: int = 10,
        sort_by: str = "relevance",
        sort_order: str = "descending",
        start: int = 0
    ) -> List[Dict]:
        """
        Search ArXiv for papers matching the query.
        
        Args:
            query: Search query (supports field tags: ti:, au:, abs:, cat:, co:)
            max_results: Maximum number of results to return (default: 10, max: 2000)
            sort_by: Sort field ("relevance", "lastUpdatedDate", "submittedDate")
            sort_order: Sort order ("ascending" or "descending")
            start: Starting index for pagination (default: 0)
        
        Returns:
            List of paper dictionaries
        
        Example:
            >>> client = ArxivClient()
            >>> results = client.search("ti:transformer AND abs:attention", max_results=20)
        """
        params = {
            'search_query': query,
            'start': start,
            'max_results': min(max_results, 2000),
            'sortBy': sort_by,
            'sortOrder': sort_order
        }
        
        return self._make_request(params)
    
    def get_recent(
        self,
        category: Optional[str] = None,
        query: Optional[str] = None,
        max_results: int = 50,
        days_back: Optional[int] = None
    ) -> List[Dict]:
        """
        Get recent papers, optionally filtered by category or query.
        
        Args:
            category: ArXiv category (e.g., "cs.LG", "q-bio.QM")
            query: Additional search query to filter results
            max_results: Maximum number of results (default: 50)
            days_back: Only return papers from last N days (optional)
        
        Returns:
            List of recent papers sorted by submission date
        
        Example:
            >>> recent = client.get_recent(category="cs.LG", max_results=20)
        """
        # Build query
        search_parts = []
        
        if category:
            search_parts.append(f"cat:{category}")
        
        if query:
            search_parts.append(f"({query})")
        
        if not search_parts:
            search_parts.append("all:all")
        
        search_query = " AND ".join(search_parts)
        
        results = self.search(
            query=search_query,
            max_results=max_results,
            sort_by="submittedDate",
            sort_order="descending"
        )
        
        # Filter by date if specified
        if days_back is not None:
            cutoff = datetime.now() - timedelta(days=days_back)
            results = [
                p for p in results 
                if p['published_datetime'] and 
                   datetime.fromisoformat(p['published_datetime']) > cutoff
            ]
        
        return results
    
    def get_paper(self, arxiv_id: str) -> Optional[Dict]:
        """
        Get a specific paper by ArXiv ID.
        
        Args:
            arxiv_id: ArXiv ID (e.g., "2301.12345" or URL)
        
        Returns:
            Paper dictionary or None if not found
        """
        # Extract ID from URL if provided
        arxiv_id = self._clean_arxiv_id(arxiv_id)
        
        params = {
            'id_list': arxiv_id,
            'max_results': 1
        }
        
        results = self._make_request(params)
        return results[0] if results else None
    
    def get_papers(self, arxiv_ids: List[str]) -> List[Dict]:
        """
        Get multiple papers by ArXiv IDs (batch operation).
        
        Args:
            arxiv_ids: List of ArXiv IDs
        
        Returns:
            List of paper dictionaries
        """
        # Clean IDs
        clean_ids = [self._clean_arxiv_id(aid) for aid in arxiv_ids]
        
        params = {
            'id_list': ','.join(clean_ids),
            'max_results': len(clean_ids)
        }
        
        return self._make_request(params)
    
    def search_by_author(
        self,
        author_name: str,
        max_results: int = 50,
        sort_by: str = "submittedDate",
        sort_order: str = "descending"
    ) -> List[Dict]:
        """
        Search for papers by a specific author.
        
        Args:
            author_name: Author name to search for
            max_results: Maximum results
            sort_by: Sort field
            sort_order: Sort order
        
        Returns:
            List of papers by this author
        """
        return self.search(
            query=f"au:{author_name}",
            max_results=max_results,
            sort_by=sort_by,
            sort_order=sort_order
        )
    
    def search_by_title(
        self,
        title_query: str,
        max_results: int = 50
    ) -> List[Dict]:
        """
        Search for papers by title keywords.
        
        Args:
            title_query: Keywords to search in title
            max_results: Maximum results
        
        Returns:
            List of matching papers
        """
        return self.search(
            query=f"ti:{title_query}",
            max_results=max_results
        )
    
    def search_by_abstract(
        self,
        abstract_query: str,
        max_results: int = 50
    ) -> List[Dict]:
        """
        Search for papers by abstract content.
        
        Args:
            abstract_query: Keywords to search in abstract
            max_results: Maximum results
        
        Returns:
            List of matching papers
        """
        return self.search(
            query=f"abs:{abstract_query}",
            max_results=max_results
        )
    
    def paginate_all(
        self,
        query: str,
        max_results: Optional[int] = None,
        sort_by: str = "submittedDate",
        sort_order: str = "descending",
        page_size: int = 100
    ) -> List[Dict]:
        """
        Paginate through all results for a query.
        
        Args:
            query: Search query
            max_results: Maximum total results (None for all)
            sort_by: Sort field
            sort_order: Sort order
            page_size: Results per page
        
        Returns:
            List of all matching papers
        """
        all_papers = []
        start = 0
        
        while True:
            results = self.search(
                query=query,
                max_results=page_size,
                start=start,
                sort_by=sort_by,
                sort_order=sort_order
            )
            
            if not results:
                break
            
            all_papers.extend(results)
            
            if max_results and len(all_papers) >= max_results:
                return all_papers[:max_results]
            
            if len(results) < page_size:
                break
            
            start += page_size
        
        return all_papers
    
    def _clean_arxiv_id(self, arxiv_id: str) -> str:
        """Extract clean ArXiv ID from URL or ID string."""
        if 'arxiv.org' in arxiv_id:
            # New format URL
            match = re.search(r'/(\d{4}\.\d{4,5})', arxiv_id)
            if match:
                return match.group(1)
            # Old format URL
            match = re.search(r'/([a-z-]+/\d{7})', arxiv_id)
            if match:
                return match.group(1)
        
        # Remove version suffix if present
        return re.sub(r'v\d+$', '', arxiv_id)
    
    @staticmethod
    def highlight_keywords(text: str, keywords: List[str], marker: str = "**") -> str:
        """
        Highlight keywords in text.
        
        Args:
            text: Text to highlight
            keywords: List of keywords to highlight
            marker: Marker to use for highlighting
        
        Returns:
            Text with highlighted keywords
        """
        for keyword in keywords:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            text = pattern.sub(f"{marker}{keyword}{marker}", text)
        return text
    
    @staticmethod
    def to_bibtex(paper: Dict) -> str:
        """
        Convert paper to BibTeX format.
        
        Args:
            paper: Paper dictionary
        
        Returns:
            BibTeX entry string
        """
        # Generate citation key
        first_author = paper['authors'][0].split()[-1] if paper['authors'] else "Unknown"
        year = paper['published'][:4] if paper['published'] else "0000"
        title_word = paper['title'].split()[0] if paper['title'] else "paper"
        cite_key = f"{first_author}{year}{title_word}".lower()
        cite_key = re.sub(r'[^a-z0-9]', '', cite_key)
        
        # Build BibTeX entry
        # Escape special characters in title
        title_escaped = paper['title'].replace('{', '\\{').replace('}', '\\}')
        
        lines = []
        lines.append(f"@article{{{cite_key},")
        lines.append(f"  title = {{{{{title_escaped}}}}},")
        lines.append(f"  author = {{{' and '.join(paper['authors'])}}},")
        lines.append(f"  year = {{{year}}},")
        lines.append(f"  eprint = {{{paper['base_id']}}},")
        lines.append("  archivePrefix = {arXiv},")
        lines.append(f"  primaryClass = {{{paper['primary_category']}}},")
        
        if paper.get('doi'):
            lines.append(f"  doi = {{{paper['doi']}}},")
        
        if paper.get('journal_ref'):
            journal_escaped = paper['journal_ref'].replace('{', '\\{').replace('}', '\\}')
            lines.append(f"  journal = {{{journal_escaped}}},")
        
        lines.append(f"  url = {{{paper['arxiv_url']}}},")
        
        # Abstract (escape special characters)
        abstract = paper['abstract'].replace('{', '\\{').replace('}', '\\}')
        lines.append(f"  abstract = {{{abstract}}}")
        
        lines.append("}")
        
        return '\n'.join(lines)
    
    @staticmethod
    def to_csv_row(paper: Dict) -> Dict:
        """
        Convert paper to CSV-compatible dictionary.
        
        Args:
            paper: Paper dictionary
        
        Returns:
            Flat dictionary suitable for CSV export
        """
        return {
            'arxiv_id': paper['arxiv_id'],
            'title': paper['title'],
            'authors': '; '.join(paper['authors']),
            'published': paper['published'],
            'updated': paper['updated'],
            'primary_category': paper['primary_category'],
            'categories': '; '.join(paper['categories']),
            'abstract': paper['abstract'],
            'doi': paper.get('doi', ''),
            'journal_ref': paper.get('journal_ref', ''),
            'comment': paper.get('comment', ''),
            'arxiv_url': paper['arxiv_url'],
            'pdf_url': paper['pdf_url']
        }
    
    def export_bibtex(self, papers: List[Dict], output_path: str):
        """
        Export papers to BibTeX file.
        
        Args:
            papers: List of paper dictionaries
            output_path: Output file path
        """
        entries = [self.to_bibtex(p) for p in papers]
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(entries))
    
    def export_json(self, papers: List[Dict], output_path: str):
        """
        Export papers to JSON file.
        
        Args:
            papers: List of paper dictionaries
            output_path: Output file path
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, default=str)
    
    def export_csv(self, papers: List[Dict], output_path: str):
        """
        Export papers to CSV file.
        
        Args:
            papers: List of paper dictionaries
            output_path: Output file path
        """
        import csv
        
        rows = [self.to_csv_row(p) for p in papers]
        
        if rows:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)


def format_paper_compact(paper: Dict, max_title_len: int = 70) -> str:
    """Format paper for compact display."""
    title = paper['title'][:max_title_len]
    if len(paper['title']) > max_title_len:
        title = title[:max_title_len-3] + "..."
    
    abstract_preview = paper['abstract'][:150].replace('\n', ' ')
    
    return f"""{title:<{max_title_len}} | {paper['published']}
  {abstract_preview}...
  → {paper['arxiv_url']}"""


def format_paper_detailed(paper: Dict) -> str:
    """Format paper for detailed display."""
    lines = [
        "=" * 80,
        f"Title: {paper['title']}",
        f"Authors: {', '.join(paper['authors'])}",
        f"Published: {paper['published']}",
        f"Categories: {', '.join(paper['categories'])}",
    ]
    
    if paper.get('doi'):
        lines.append(f"DOI: {paper['doi']}")
    
    if paper.get('journal_ref'):
        lines.append(f"Journal: {paper['journal_ref']}")
    
    if paper.get('comment'):
        lines.append(f"Comment: {paper['comment']}")
    
    lines.extend([
        "",
        "Abstract:",
        paper['abstract'],
        "",
        f"ArXiv: {paper['arxiv_url']}",
        f"PDF: {paper['pdf_url']}",
    ])
    
    return '\n'.join(lines)


if __name__ == "__main__":
    # Example usage
    client = ArxivClient()
    
    # Search for papers
    results = client.search("machine learning", max_results=5)
    
    print(f"Found {len(results)} papers:\n")
    for paper in results:
        print(format_paper_compact(paper))
        print()
