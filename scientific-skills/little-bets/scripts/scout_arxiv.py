#!/usr/bin/env python3
"""
Streamlined ArXiv scouting for little bets.

This script wraps arxiv-database functionality to quickly find relevant papers,
extract key information (datasets, baselines, methods), and highlight important
keywords. Optimized for rapid methodology discovery.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Dict, Optional

# Try to import arxiv_client from arxiv-database skill
try:
    # Assume we're in the little-bets directory
    arxiv_skill_path = Path(__file__).parent.parent.parent / 'arxiv-database' / 'scripts'
    if arxiv_skill_path.exists():
        sys.path.insert(0, str(arxiv_skill_path))
    from arxiv_client import ArxivClient, highlight_keywords
except ImportError:
    print("Warning: Could not import arxiv_client. Make sure arxiv-database skill is available.", file=sys.stderr)
    print("You may need to install dependencies or adjust the path.", file=sys.stderr)
    sys.exit(1)


def extract_keywords(text: str, keywords: List[str]) -> Dict[str, int]:
    """Count occurrences of keywords in text (case-insensitive)."""
    text_lower = text.lower()
    counts = {}
    for keyword in keywords:
        counts[keyword] = text_lower.count(keyword.lower())
    return counts


def extract_datasets(abstract: str) -> List[str]:
    """Extract dataset mentions from abstract."""
    # Common dataset patterns
    patterns = [
        r'([A-Z][a-z]+-[0-9]+)',  # e.g., ImageNet-1K
        r'([A-Z]{2,}[0-9]*)',     # e.g., MNIST, CIFAR10
        r'([A-Z][a-z]+ dataset)',  # e.g., ImageNet dataset
    ]
    
    datasets = []
    for pattern in patterns:
        import re
        matches = re.findall(pattern, abstract)
        datasets.extend(matches)
    
    return list(set(datasets))  # Remove duplicates


def extract_baselines(abstract: str) -> List[str]:
    """Extract baseline method mentions."""
    # Look for common baseline phrases
    baseline_phrases = [
        'baseline',
        'compared to',
        'outperforms',
        'improves upon',
        'state-of-the-art',
        'sota'
    ]
    
    baselines = []
    abstract_lower = abstract.lower()
    
    # Simple extraction: find sentences with baseline keywords
    sentences = abstract.split('.')
    for sentence in sentences:
        sentence_lower = sentence.lower()
        if any(phrase in sentence_lower for phrase in baseline_phrases):
            # Extract method names (heuristic: capitalized words)
            import re
            methods = re.findall(r'\b([A-Z][a-z]+(?:-[A-Z][a-z]+)*)\b', sentence)
            baselines.extend(methods)
    
    return list(set(baselines[:5]))  # Limit to 5


def format_paper_compact(paper: Dict, keywords: List[str] = None, focus: str = None) -> str:
    """Format paper for compact display with highlighting."""
    lines = []
    
    # Title with highlighting
    title = paper['title']
    if keywords:
        title = highlight_keywords(title, keywords, marker='**')
    lines.append(f"**{title}**")
    
    # Authors and date
    authors_str = ', '.join(paper['authors'][:3])
    if len(paper['authors']) > 3:
        authors_str += f" et al. ({len(paper['authors'])} authors)"
    lines.append(f"  {authors_str} | {paper['published']}")
    
    # Abstract preview with highlighting
    abstract = paper['abstract'][:300]
    if len(paper['abstract']) > 300:
        abstract += "..."
    
    if keywords:
        abstract = highlight_keywords(abstract, keywords, marker='**')
    
    lines.append(f"  {abstract}")
    
    # Extract focused information
    if focus == 'datasets':
        datasets = extract_datasets(paper['abstract'])
        if datasets:
            lines.append(f"  📊 Datasets: {', '.join(datasets[:5])}")
    
    if focus == 'baselines':
        baselines = extract_baselines(paper['abstract'])
        if baselines:
            lines.append(f"  📈 Baselines: {', '.join(baselines[:5])}")
    
    if focus == 'methods':
        # Highlight method-related keywords
        method_keywords = ['method', 'algorithm', 'approach', 'model', 'framework']
        method_counts = extract_keywords(paper['abstract'], method_keywords)
        if sum(method_counts.values()) > 0:
            lines.append(f"  🔧 Method mentions: {sum(method_counts.values())}")
    
    # Links
    lines.append(f"  🔗 {paper['arxiv_url']}")
    
    return '\n'.join(lines)


def scout_arxiv(
    query: str,
    max_results: int = 15,
    focus: Optional[str] = None,
    keywords: List[str] = None
) -> List[Dict]:
    """
    Scout ArXiv for relevant papers.
    
    Args:
        query: Search query
        max_results: Maximum number of results
        focus: What to focus on ('datasets', 'baselines', 'methods', None)
        keywords: Keywords to highlight
    
    Returns:
        List of paper dictionaries
    """
    client = ArxivClient()
    
    # Search
    papers = client.search(query, max_results=max_results)
    
    # Sort by relevance (ArXiv API already does this, but we can re-sort by date if needed)
    # For now, keep as-is (sorted by relevance)
    
    return papers


def main():
    parser = argparse.ArgumentParser(
        description='Scout ArXiv for relevant papers (optimized for little bets)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Quick search
  python scout_arxiv.py "graph neural networks"
  
  # Focus on datasets
  python scout_arxiv.py "node classification" --show-datasets
  
  # Focus on baselines
  python scout_arxiv.py "transformer attention" --show-baselines
  
  # Highlight specific keywords
  python scout_arxiv.py "machine learning" --keywords "transformer" "attention"
  
  # Limit results
  python scout_arxiv.py "topic" --max 10
        """
    )
    
    parser.add_argument(
        'query',
        help='Search query for ArXiv'
    )
    
    parser.add_argument(
        '--max', '-n',
        type=int,
        default=15,
        help='Maximum number of results (default: 15)'
    )
    
    parser.add_argument(
        '--focus',
        choices=['methods', 'datasets', 'baselines'],
        help='What to focus on extracting'
    )
    
    parser.add_argument(
        '--show-datasets',
        action='store_true',
        help='Show dataset mentions (alias for --focus datasets)'
    )
    
    parser.add_argument(
        '--show-baselines',
        action='store_true',
        help='Show baseline mentions (alias for --focus baselines)'
    )
    
    parser.add_argument(
        '--keywords', '-k',
        nargs='+',
        help='Keywords to highlight in results'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Save results to JSON file'
    )
    
    args = parser.parse_args()
    
    # Handle aliases
    if args.show_datasets:
        args.focus = 'datasets'
    if args.show_baselines:
        args.focus = 'baselines'
    
    try:
        print(f"🔍 Searching ArXiv for: '{args.query}'", file=sys.stderr)
        print(f"   Max results: {args.max}", file=sys.stderr)
        if args.focus:
            print(f"   Focus: {args.focus}", file=sys.stderr)
        print(file=sys.stderr)
        
        # Scout
        papers = scout_arxiv(
            query=args.query,
            max_results=args.max,
            focus=args.focus,
            keywords=args.keywords
        )
        
        if not papers:
            print("No papers found.", file=sys.stderr)
            sys.exit(1)
        
        print(f"Found {len(papers)} papers:\n")
        
        # Display results
        for i, paper in enumerate(papers, 1):
            print(f"{'=' * 80}")
            print(f"[{i}/{len(papers)}]")
            print(format_paper_compact(paper, keywords=args.keywords, focus=args.focus))
            print()
        
        # Save to file if requested
        if args.output:
            import json
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Prepare papers for JSON export
            papers_export = []
            for paper in papers:
                paper_export = {
                    'title': paper['title'],
                    'authors': paper['authors'],
                    'published': paper['published'],
                    'abstract': paper['abstract'],
                    'arxiv_url': paper['arxiv_url'],
                    'pdf_url': paper['pdf_url'],
                }
                
                # Add focused extractions
                if args.focus == 'datasets':
                    paper_export['datasets'] = extract_datasets(paper['abstract'])
                if args.focus == 'baselines':
                    paper_export['baselines'] = extract_baselines(paper['abstract'])
                
                papers_export.append(paper_export)
            
            with open(output_path, 'w') as f:
                json.dump(papers_export, f, indent=2)
            
            print(f"💾 Saved results to {args.output}", file=sys.stderr)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
