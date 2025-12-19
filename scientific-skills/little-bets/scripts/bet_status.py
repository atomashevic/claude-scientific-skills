#!/usr/bin/env python3
"""
Track and display status of all little bets.

Scans bet directories, parses status from design.md files, and displays
a summary table with time tracking and findings.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


def parse_bet_directory(bet_dir: Path) -> Optional[Dict]:
    """
    Parse a bet directory and extract metadata.
    
    Args:
        bet_dir: Path to bet directory
    
    Returns:
        Dictionary with bet metadata or None if invalid
    """
    design_file = bet_dir / 'design.md'
    results_file = bet_dir / 'results.md'
    
    if not design_file.exists():
        return None
    
    # Extract bet ID and name from directory name
    dir_name = bet_dir.name
    match = re.match(r'bet_(\d+)_(.+)', dir_name)
    if not match:
        return None
    
    bet_id = match.group(1)
    bet_name = match.group(2).replace('_', ' ')
    
    # Parse design.md
    design_content = design_file.read_text()
    
    # Extract date
    date_match = re.search(r'\*\*Date\*\*:\s*\[?(\d{4}-\d{2}-\d{2})\]?', design_content)
    date = date_match.group(1) if date_match else None
    
    # Extract time budget
    budget_match = re.search(r'\*\*Time Budget\*\*:\s*\[?(\d+)\s*hours?\]?', design_content, re.IGNORECASE)
    time_budget = budget_match.group(1) if budget_match else None
    
    # Extract status
    status_match = re.search(r'\*\*Status\*\*:\s*(🔄|✅|❌|💡)\s*(Active|Done|Parked|Pivoted)?', design_content)
    if status_match:
        status_emoji = status_match.group(1)
        status_text = status_match.group(2) or 'Active'
    else:
        # Try to infer from results.md
        if results_file.exists():
            results_content = results_file.read_text()
            if '✅ Done' in results_content or 'Status**: ✅' in results_content:
                status_emoji = '✅'
                status_text = 'Done'
            elif '❌ Parked' in results_content or 'Status**: ❌' in results_content:
                status_emoji = '❌'
                status_text = 'Parked'
            else:
                status_emoji = '🔄'
                status_text = 'Active'
        else:
            status_emoji = '🔄'
            status_text = 'Active'
    
    # Extract key finding from results.md if available
    key_finding = None
    if results_file.exists():
        results_content = results_file.read_text()
        finding_match = re.search(r'## Key Finding\s*\n\*\*(.+?)\*\*', results_content, re.DOTALL)
        if finding_match:
            key_finding = finding_match.group(1).strip()[:50]  # Limit length
            if len(finding_match.group(1)) > 50:
                key_finding += "..."
    
    # Try to extract time spent from results.md
    time_spent = None
    if results_file.exists():
        results_content = results_file.read_text()
        spent_match = re.search(r'\*\*Time Spent\*\*:\s*(\d+)\s*hours?', results_content, re.IGNORECASE)
        if spent_match:
            time_spent = int(spent_match.group(1))
    
    return {
        'id': bet_id,
        'name': bet_name,
        'date': date,
        'time_budget': int(time_budget) if time_budget else None,
        'time_spent': time_spent,
        'status_emoji': status_emoji,
        'status_text': status_text,
        'key_finding': key_finding,
        'directory': bet_dir
    }


def scan_bets(bets_dir: Path) -> List[Dict]:
    """
    Scan directory for bet subdirectories.
    
    Args:
        bets_dir: Directory containing bet subdirectories
    
    Returns:
        List of bet metadata dictionaries
    """
    bets = []
    
    if not bets_dir.exists():
        return bets
    
    for item in bets_dir.iterdir():
        if item.is_dir() and item.name.startswith('bet_'):
            bet_data = parse_bet_directory(item)
            if bet_data:
                bets.append(bet_data)
    
    # Sort by ID
    bets.sort(key=lambda x: int(x['id']))
    
    return bets


def format_status_table(bets: List[Dict], active_only: bool = False) -> str:
    """Format bets as a markdown table."""
    if active_only:
        bets = [b for b in bets if b['status_text'] != 'Done']
    
    if not bets:
        return "No bets found."
    
    # Build table
    lines = []
    lines.append("| ID  | Name | Started | Status | Time | Finding |")
    lines.append("|-----|------|---------|--------|------|---------|")
    
    for bet in bets:
        # Format time
        if bet['time_spent'] and bet['time_budget']:
            time_str = f"{bet['time_spent']}h/{bet['time_budget']}h"
        elif bet['time_budget']:
            time_str = f"—/{bet['time_budget']}h"
        else:
            time_str = "—"
        
        # Format finding
        finding = bet['key_finding'] or "—"
        if len(finding) > 30:
            finding = finding[:27] + "..."
        
        # Format name
        name = bet['name'][:20] if len(bet['name']) <= 20 else bet['name'][:17] + "..."
        
        lines.append(
            f"| {bet['id']:>3s} | {name:<20s} | {bet['date'] or '—':<8s} | "
            f"{bet['status_emoji']} {bet['status_text']:<6s} | {time_str:<5s} | {finding:<30s} |"
        )
    
    return '\n'.join(lines)


def format_summary(bets: List[Dict]) -> str:
    """Format summary statistics."""
    total = len(bets)
    active = sum(1 for b in bets if b['status_text'] == 'Active')
    done = sum(1 for b in bets if b['status_text'] == 'Done')
    parked = sum(1 for b in bets if b['status_text'] == 'Parked')
    
    total_time_budgeted = sum(b['time_budget'] for b in bets if b['time_budget'])
    total_time_spent = sum(b['time_spent'] for b in bets if b['time_spent'])
    
    lines = []
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Total bets**: {total}")
    lines.append(f"- **Active**: {active} 🔄")
    lines.append(f"- **Done**: {done} ✅")
    lines.append(f"- **Parked**: {parked} ❌")
    
    if total_time_budgeted:
        lines.append(f"- **Total time budgeted**: {total_time_budgeted}h")
    if total_time_spent:
        lines.append(f"- **Total time spent**: {total_time_spent}h")
        if total_time_budgeted:
            efficiency = (total_time_spent / total_time_budgeted) * 100
            lines.append(f"- **Efficiency**: {efficiency:.1f}%")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Track and display status of all little bets',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show all bets
  python bet_status.py
  
  # Show only active bets
  python bet_status.py --active
  
  # Show summary statistics
  python bet_status.py --summary
  
  # Export to markdown file
  python bet_status.py --export bets_log.md
  
  # Scan specific directory
  python bet_status.py --directory ./my_bets
        """
    )
    
    parser.add_argument(
        '--directory', '-d',
        type=str,
        default='.',
        help='Directory containing bet subdirectories (default: current directory)'
    )
    
    parser.add_argument(
        '--active',
        action='store_true',
        help='Show only active bets'
    )
    
    parser.add_argument(
        '--summary',
        action='store_true',
        help='Show summary statistics only'
    )
    
    parser.add_argument(
        '--export',
        type=str,
        help='Export status to markdown file'
    )
    
    args = parser.parse_args()
    
    try:
        bets_dir = Path(args.directory).resolve()
        
        # Scan for bets
        bets = scan_bets(bets_dir)
        
        if not bets:
            print("No bets found.", file=sys.stderr)
            sys.exit(0)
        
        # Generate output
        output_lines = []
        
        if args.summary:
            output_lines.append(format_summary(bets))
        else:
            output_lines.append("# Little Bets Status")
            output_lines.append("")
            output_lines.append(format_summary(bets))
            output_lines.append("")
            output_lines.append("## All Bets")
            output_lines.append("")
            output_lines.append(format_status_table(bets, active_only=args.active))
        
        output = '\n'.join(output_lines)
        
        # Write output
        if args.export:
            export_path = Path(args.export)
            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_text(output)
            print(f"Exported to {export_path}", file=sys.stderr)
        else:
            print(output)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
