#!/usr/bin/env python3
"""
Command-line tool for quickly browsing and skimming ArXiv abstracts.

Features:
- Browse recent papers by category
- Search by keywords, author, or title
- Multiple display formats (compact, detailed, one-line)
- Export to JSON, CSV, or BibTeX
- Keyword highlighting in abstracts
- Filtering by date range

Usage Examples:
    python abstract_skimmer.py --category cs.LG --max 20
    python abstract_skimmer.py --query "machine learning" --max 30
    python abstract_skimmer.py --author "Vaswani" --format detailed
    python abstract_skimmer.py --query "quantum" --export results.json
    python abstract_skimmer.py --category q-bio.QM --bibtex refs.bib
"""

import argparse
import json
import sys
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from arxiv_client import ArxivClient, format_paper_compact, format_paper_detailed


def highlight_text(text: str, keywords: List[str], use_color: bool = True) -> str:
    """Highlight keywords in text with ANSI colors or markers."""
    if not keywords:
        return text
    
    for keyword in keywords:
        if use_color:
            # ANSI yellow background
            replacement = f"\033[1;33m{keyword}\033[0m"
        else:
            replacement = f"**{keyword}**"
        
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        text = pattern.sub(replacement, text)
    
    return text


def format_oneline(paper: Dict, max_len: int = 100) -> str:
    """Format paper as single line for quick scanning."""
    title = paper['title'][:max_len-20]
    if len(paper['title']) > max_len-20:
        title = title + "..."
    return f"[{paper['published']}] {title}"


def format_abstract_focused(paper: Dict, keywords: Optional[List[str]] = None, use_color: bool = True) -> str:
    """Format paper with focus on abstract for skimming."""
    title = paper['title']
    abstract = paper['abstract']
    
    if keywords:
        title = highlight_text(title, keywords, use_color)
        abstract = highlight_text(abstract, keywords, use_color)
    
    authors_str = ', '.join(paper['authors'][:5])
    if len(paper['authors']) > 5:
        authors_str += f" et al. ({len(paper['authors'])} authors)"
    
    return f"""
{'─' * 80}
📄 {title}
👥 {authors_str}
📅 {paper['published']} | 🏷️ {paper['primary_category']} | 🔗 {paper['arxiv_url']}

{abstract}
"""


def filter_by_keywords(papers: List[Dict], keywords: List[str], 
                       search_in: str = "both") -> List[Dict]:
    """Filter papers by keywords in title and/or abstract."""
    filtered = []
    
    for paper in papers:
        text = ""
        if search_in in ("title", "both"):
            text += paper['title'].lower() + " "
        if search_in in ("abstract", "both"):
            text += paper['abstract'].lower()
        
        if all(kw.lower() in text for kw in keywords):
            filtered.append(paper)
    
    return filtered


def print_summary(papers: List[Dict]):
    """Print summary statistics for search results."""
    if not papers:
        print("No papers found.")
        return
    
    # Count categories
    categories = {}
    for paper in papers:
        cat = paper['primary_category']
        categories[cat] = categories.get(cat, 0) + 1
    
    # Date range
    dates = [p['published'] for p in papers if p['published']]
    min_date = min(dates) if dates else "N/A"
    max_date = max(dates) if dates else "N/A"
    
    print(f"\n📊 Summary: {len(papers)} papers")
    print(f"📅 Date range: {min_date} to {max_date}")
    print(f"🏷️ Categories: {', '.join(f'{k}({v})' for k, v in sorted(categories.items(), key=lambda x: -x[1])[:5])}")


def main():
    parser = argparse.ArgumentParser(
        description="Browse and skim ArXiv paper abstracts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Browse recent ML papers:
    python abstract_skimmer.py --category cs.LG --max 20
  
  Search for specific topic:
    python abstract_skimmer.py --query "ti:transformer AND abs:attention" --max 30
  
  Find papers by author:
    python abstract_skimmer.py --author "Vaswani" --format detailed
  
  Export to BibTeX:
    python abstract_skimmer.py --category cs.AI --max 50 --bibtex refs.bib

Categories (examples):
  cs.LG  - Machine Learning
  cs.AI  - Artificial Intelligence
  cs.CV  - Computer Vision
  cs.CL  - Computation and Language (NLP)
  q-bio.QM - Quantitative Methods (Biology)
  stat.ML  - Statistics Machine Learning
  quant-ph - Quantum Physics
"""
    )
    
    # Search options
    search_group = parser.add_argument_group('Search Options')
    search_group.add_argument(
        '--query', '-q',
        type=str,
        help='Search query (supports field tags: ti:, au:, abs:, cat:)'
    )
    search_group.add_argument(
        '--category', '-c',
        type=str,
        help='ArXiv category (e.g., cs.LG, q-bio.QM)'
    )
    search_group.add_argument(
        '--author', '-a',
        type=str,
        help='Search by author name'
    )
    search_group.add_argument(
        '--title', '-t',
        type=str,
        help='Search by title keywords'
    )
    
    # Filter options
    filter_group = parser.add_argument_group('Filter Options')
    filter_group.add_argument(
        '--max', '-m',
        type=int,
        default=20,
        help='Maximum number of results (default: 20)'
    )
    filter_group.add_argument(
        '--days-back', '-d',
        type=int,
        help='Only show papers from last N days'
    )
    filter_group.add_argument(
        '--keywords', '-k',
        nargs='+',
        help='Filter and highlight these keywords'
    )
    
    # Display options
    display_group = parser.add_argument_group('Display Options')
    display_group.add_argument(
        '--format', '-f',
        choices=['compact', 'detailed', 'oneline', 'abstract'],
        default='abstract',
        help='Output format (default: abstract)'
    )
    display_group.add_argument(
        '--no-color',
        action='store_true',
        help='Disable colored output'
    )
    display_group.add_argument(
        '--summary',
        action='store_true',
        help='Show summary statistics'
    )
    
    # Export options
    export_group = parser.add_argument_group('Export Options')
    export_group.add_argument(
        '--export', '-e',
        type=str,
        help='Export results to JSON file'
    )
    export_group.add_argument(
        '--csv',
        type=str,
        help='Export results to CSV file'
    )
    export_group.add_argument(
        '--bibtex', '-b',
        type=str,
        help='Export results to BibTeX file'
    )
    
    # Other options
    parser.add_argument(
        '--sort',
        choices=['relevance', 'submittedDate', 'lastUpdatedDate'],
        default='submittedDate',
        help='Sort order (default: submittedDate)'
    )
    parser.add_argument(
        '--cache-dir',
        type=str,
        help='Directory for caching results'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Initialize client
    client = ArxivClient(cache_dir=args.cache_dir)
    
    # Determine search type and execute
    try:
        if args.author:
            # Author search
            if args.verbose:
                print(f"Searching for papers by author: {args.author}")
            papers = client.search_by_author(
                author_name=args.author,
                max_results=args.max,
                sort_by=args.sort
            )
        elif args.title:
            # Title search
            if args.verbose:
                print(f"Searching for papers with title: {args.title}")
            papers = client.search_by_title(
                title_query=args.title,
                max_results=args.max
            )
        elif args.category:
            # Category browsing
            if args.verbose:
                print(f"Browsing recent papers in category: {args.category}")
            papers = client.get_recent(
                category=args.category,
                query=args.query,
                max_results=args.max,
                days_back=args.days_back
            )
        elif args.query:
            # General search
            if args.verbose:
                print(f"Searching for: {args.query}")
            papers = client.search(
                query=args.query,
                max_results=args.max,
                sort_by=args.sort,
                sort_order='descending'
            )
        else:
            # Default: recent ML papers
            if args.verbose:
                print("No query specified, showing recent papers in cs.LG")
            papers = client.get_recent(
                category="cs.LG",
                max_results=args.max
            )
            print("ℹ️  No query specified, showing recent papers in cs.LG\n")
        
        # Apply keyword filtering if specified
        if args.keywords:
            original_count = len(papers)
            papers = filter_by_keywords(papers, args.keywords)
            if args.verbose:
                print(f"Filtered {original_count} → {len(papers)} papers by keywords")
        
        # Display results
        use_color = not args.no_color and sys.stdout.isatty()
        
        if args.format == 'oneline':
            for paper in papers:
                print(format_oneline(paper))
        elif args.format == 'compact':
            for paper in papers:
                print(format_paper_compact(paper))
                print()
        elif args.format == 'detailed':
            for paper in papers:
                print(format_paper_detailed(paper))
                print()
        else:  # abstract (default)
            for paper in papers:
                output = format_abstract_focused(paper, args.keywords, use_color)
                print(output)
        
        # Show summary
        if args.summary:
            print_summary(papers)
        
        # Export if requested
        if args.export:
            client.export_json(papers, args.export)
            print(f"\n✅ Exported {len(papers)} papers to {args.export}")
        
        if args.csv:
            client.export_csv(papers, args.csv)
            print(f"\n✅ Exported {len(papers)} papers to {args.csv}")
        
        if args.bibtex:
            client.export_bibtex(papers, args.bibtex)
            print(f"\n✅ Exported {len(papers)} papers to {args.bibtex}")
        
        # Final count
        if not any([args.export, args.csv, args.bibtex]):
            print(f"\n📚 Found {len(papers)} papers")
    
    except KeyboardInterrupt:
        print("\n\nInterrupted.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
