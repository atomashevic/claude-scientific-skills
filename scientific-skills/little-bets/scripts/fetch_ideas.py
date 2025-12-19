#!/usr/bin/env python3
"""
Fetch and parse ideas from a GitHub gist.

This script helps load ideas from your research ideas inbox (stored as a GitHub gist)
and extract individual ideas with metadata for use in little bets.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Optional


def fetch_gist(url: str) -> str:
    """
    Fetch raw content from a GitHub gist using gh CLI.
    
    Args:
        url: GitHub gist URL (e.g., https://gist.github.com/user/id)
    
    Returns:
        Raw markdown content from the gist
    
    Raises:
        RuntimeError: If gh CLI is not available or gist fetch fails
    """
    # Extract gist ID from URL
    gist_id_match = re.search(r'gist\.github\.com/[^/]+/([a-f0-9]+)', url)
    if not gist_id_match:
        # Try direct ID format
        gist_id_match = re.search(r'([a-f0-9]{32})', url)
    
    if not gist_id_match:
        raise ValueError(f"Could not extract gist ID from URL: {url}")
    
    gist_id = gist_id_match.group(1) if gist_id_match.lastindex else gist_id_match.group(0)
    
    try:
        # Use gh CLI to fetch gist
        result = subprocess.run(
            ['gh', 'gist', 'view', gist_id, '--raw'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to fetch gist: {e.stderr}")
    except FileNotFoundError:
        raise RuntimeError(
            "gh CLI not found. Install GitHub CLI: https://cli.github.com/"
        )


def parse_ideas(content: str) -> List[Dict[str, any]]:
    """
    Parse markdown content into structured idea objects.
    
    Supports multiple formats:
    1. ## Idea: Title format
    2. ### Idea: Title format
    3. Bullet lists with metadata
    
    Args:
        content: Markdown content from gist
    
    Returns:
        List of idea dictionaries with metadata
    """
    ideas = []
    current_idea = None
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        # Detect idea header (## or ###)
        header_match = re.match(r'^#{2,3}\s+Idea:\s*(.+)$', line, re.IGNORECASE)
        if header_match:
            # Save previous idea if exists
            if current_idea:
                ideas.append(current_idea)
            
            # Start new idea
            current_idea = {
                'title': header_match.group(1).strip(),
                'metadata': {},
                'description': [],
                'line_number': i + 1
            }
            continue
        
        # Detect metadata lines (key: value format)
        if current_idea:
            metadata_match = re.match(r'^-\s*([^:]+):\s*(.+)$', line)
            if metadata_match:
                key = metadata_match.group(1).strip().lower()
                value = metadata_match.group(2).strip()
                current_idea['metadata'][key] = value
                continue
            
            # Collect description lines (non-empty, non-header)
            if line.strip() and not line.strip().startswith('#'):
                current_idea['description'].append(line.strip())
    
    # Don't forget the last idea
    if current_idea:
        ideas.append(current_idea)
    
    # Clean up descriptions
    for idea in ideas:
        idea['description'] = '\n'.join(idea['description']).strip()
    
    return ideas


def format_ideas(ideas: List[Dict], format_type: str = 'markdown') -> str:
    """
    Format ideas in the requested format.
    
    Args:
        ideas: List of idea dictionaries
        format_type: 'markdown', 'json', or 'list'
    
    Returns:
        Formatted string
    """
    if format_type == 'json':
        return json.dumps(ideas, indent=2)
    
    elif format_type == 'list':
        lines = []
        for i, idea in enumerate(ideas, 1):
            lines.append(f"{i}. {idea['title']}")
            if idea.get('metadata'):
                priority = idea['metadata'].get('priority', 'unknown')
                domain = idea['metadata'].get('domain', 'unknown')
                lines.append(f"   Priority: {priority}, Domain: {domain}")
        return '\n'.join(lines)
    
    else:  # markdown
        lines = []
        for i, idea in enumerate(ideas, 1):
            lines.append(f"## {i}. {idea['title']}")
            lines.append("")
            if idea.get('metadata'):
                lines.append("**Metadata:**")
                for key, value in idea['metadata'].items():
                    lines.append(f"- {key}: {value}")
                lines.append("")
            if idea.get('description'):
                lines.append("**Description:**")
                lines.append(idea['description'])
                lines.append("")
        return '\n'.join(lines)


def select_idea(ideas: List[Dict], criteria: Optional[Dict] = None) -> Optional[Dict]:
    """
    Help select an idea based on criteria.
    
    Args:
        ideas: List of idea dictionaries
        criteria: Optional dict with filters (e.g., {'priority': 'high'})
    
    Returns:
        Selected idea or None
    """
    if not criteria:
        return ideas[0] if ideas else None
    
    filtered = ideas
    for key, value in criteria.items():
        filtered = [
            idea for idea in filtered
            if idea.get('metadata', {}).get(key, '').lower() == str(value).lower()
        ]
    
    return filtered[0] if filtered else None


def main():
    parser = argparse.ArgumentParser(
        description='Fetch and parse ideas from a GitHub gist',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all ideas
  python fetch_ideas.py https://gist.github.com/user/id --list
  
  # Export as JSON
  python fetch_ideas.py https://gist.github.com/user/id --format json --output ideas.json
  
  # Get random idea
  python fetch_ideas.py https://gist.github.com/user/id --random
  
  # Filter by priority
  python fetch_ideas.py https://gist.github.com/user/id --priority high
        """
    )
    
    parser.add_argument(
        'url',
        help='GitHub gist URL or gist ID'
    )
    
    parser.add_argument(
        '--format',
        choices=['markdown', 'json', 'list'],
        default='list',
        help='Output format (default: list)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (default: stdout)'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='Quick list of all ideas (same as --format list)'
    )
    
    parser.add_argument(
        '--random',
        action='store_true',
        help='Select and display a random idea'
    )
    
    parser.add_argument(
        '--priority',
        choices=['high', 'medium', 'low'],
        help='Filter by priority'
    )
    
    parser.add_argument(
        '--domain',
        type=str,
        help='Filter by domain'
    )
    
    args = parser.parse_args()
    
    try:
        # Fetch gist content
        print(f"Fetching gist: {args.url}", file=sys.stderr)
        content = fetch_gist(args.url)
        
        # Parse ideas
        ideas = parse_ideas(content)
        print(f"Found {len(ideas)} ideas", file=sys.stderr)
        
        if not ideas:
            print("No ideas found in gist", file=sys.stderr)
            sys.exit(1)
        
        # Apply filters
        criteria = {}
        if args.priority:
            criteria['priority'] = args.priority
        if args.domain:
            criteria['domain'] = args.domain
        
        if criteria:
            filtered_ideas = [
                idea for idea in ideas
                if all(
                    idea.get('metadata', {}).get(k, '').lower() == str(v).lower()
                    for k, v in criteria.items()
                )
            ]
            if filtered_ideas:
                ideas = filtered_ideas
            else:
                print(f"No ideas match criteria: {criteria}", file=sys.stderr)
                sys.exit(1)
        
        # Select idea
        if args.random:
            import random
            selected = random.choice(ideas)
            ideas = [selected]
            print(f"\n🎲 Random idea selected:", file=sys.stderr)
        
        # Format output
        output_format = 'list' if args.list else args.format
        output = format_ideas(ideas, output_format)
        
        # Write output
        if args.output:
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Saved to {args.output}", file=sys.stderr)
        else:
            print(output)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
