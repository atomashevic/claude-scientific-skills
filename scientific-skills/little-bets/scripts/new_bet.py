#!/usr/bin/env python3
"""
Initialize a new little bet directory with templates.

Creates a bet directory structure, copies templates with ID/name filled in,
and sets up basic tracking.
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def get_skill_root() -> Path:
    """Get the root directory of the little-bets skill."""
    script_path = Path(__file__).resolve()
    # Script is in scripts/, skill root is parent
    return script_path.parent.parent


def get_next_bet_id(bets_dir: Path) -> str:
    """Find the next available bet ID by scanning existing bet directories."""
    if not bets_dir.exists():
        return "001"
    
    existing_ids = []
    for bet_dir in bets_dir.iterdir():
        if bet_dir.is_dir() and bet_dir.name.startswith('bet_'):
            # Extract ID from directory name (bet_001_name)
            parts = bet_dir.name.split('_')
            if len(parts) >= 2 and parts[1].isdigit():
                existing_ids.append(int(parts[1]))
    
    if not existing_ids:
        return "001"
    
    next_id = max(existing_ids) + 1
    return f"{next_id:03d}"


def sanitize_name(name: str) -> str:
    """Convert bet name to filesystem-safe format."""
    import re
    # Replace spaces and special chars with underscores
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '_', name)
    name = name.lower()
    return name


def load_idea_from_json(json_path: Path) -> Optional[dict]:
    """Load idea from JSON file (from fetch_ideas.py output)."""
    try:
        with open(json_path) as f:
            ideas = json.load(f)
            if isinstance(ideas, list) and ideas:
                return ideas[0] if len(ideas) == 1 else ideas
            return ideas
    except Exception as e:
        print(f"Warning: Could not load idea from {json_path}: {e}", file=sys.stderr)
        return None


def create_bet_directory(
    bet_id: str,
    bet_name: str,
    output_dir: Path,
    idea_data: Optional[dict] = None
) -> Path:
    """
    Create a new bet directory with templates.
    
    Args:
        bet_id: Bet ID (e.g., "001")
        bet_name: Sanitized bet name
        output_dir: Directory to create bet in
        idea_data: Optional idea data from fetch_ideas.py
    
    Returns:
        Path to created bet directory
    """
    skill_root = get_skill_root()
    
    # Create bet directory
    bet_dir_name = f"bet_{bet_id}_{bet_name}"
    bet_dir = output_dir / bet_dir_name
    bet_dir.mkdir(parents=True, exist_ok=True)
    
    # Create subdirectories
    (bet_dir / 'data').mkdir(exist_ok=True)
    (bet_dir / 'results').mkdir(exist_ok=True)
    
    # Load templates
    assets_dir = skill_root / 'assets'
    design_template = assets_dir / 'design_template.md'
    experiment_template = assets_dir / 'experiment_template.py'
    results_template = assets_dir / 'results_template.md'
    
    # Get current date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Create design.md from template
    if design_template.exists():
        design_content = design_template.read_text()
        design_content = design_content.replace('[ID]', bet_id)
        design_content = design_content.replace('[Name]', bet_name.replace('_', ' ').title())
        design_content = design_content.replace('[YYYY-MM-DD]', today)
        
        # Fill in idea data if available
        if idea_data:
            if 'title' in idea_data:
                # Use idea title as core question if not already set
                if '[Single clear question' in design_content:
                    design_content = design_content.replace(
                        '[Single clear question this experiment will answer]',
                        idea_data['title']
                    )
            if 'description' in idea_data:
                # Add description to hypothesis section
                pass  # Could add this
        
        (bet_dir / 'design.md').write_text(design_content)
    
    # Create experiment.py from template
    if experiment_template.exists():
        experiment_content = experiment_template.read_text()
        experiment_content = experiment_content.replace('"001"', f'"{bet_id}"')
        experiment_content = experiment_content.replace('"your_bet_name"', f'"{bet_name}"')
        experiment_content = experiment_content.replace('[ID]', bet_id)
        experiment_content = experiment_content.replace('[Name]', bet_name.replace('_', ' ').title())
        experiment_content = experiment_content.replace('[YYYY-MM-DD]', today)
        
        # Set question from idea if available
        if idea_data and 'title' in idea_data:
            experiment_content = experiment_content.replace(
                'Does X affect Y?',
                idea_data['title']
            )
        
        (bet_dir / 'experiment.py').write_text(experiment_content)
        # Make executable
        (bet_dir / 'experiment.py').chmod(0o755)
    
    # Create results.md from template (empty, to be filled later)
    if results_template.exists():
        results_content = results_template.read_text()
        results_content = results_content.replace('[ID]', bet_id)
        results_content = results_content.replace('[Name]', bet_name.replace('_', ' ').title())
        results_content = results_content.replace('[YYYY-MM-DD]', today)
        (bet_dir / 'results.md').write_text(results_content)
    
    # Create README.md
    readme_content = f"""# Little Bet {bet_id}: {bet_name.replace('_', ' ').title()}

**Created**: {today}
**Status**: 🔄 Active

## Quick Links

- [Design](design.md) - Experiment design and plan
- [Experiment](experiment.py) - Implementation code
- [Results](results.md) - Findings and outcomes

## Directory Structure

```
bet_{bet_id}_{bet_name}/
├── design.md          # Experiment design
├── experiment.py      # Implementation
├── results.md         # Results documentation
├── data/              # Input data
└── results/           # Output files, figures
```

## Quick Start

1. Fill in `design.md` with your experiment plan
2. Implement your experiment in `experiment.py`
3. Run: `python experiment.py`
4. Document results in `results.md`

## Idea Source

{f"**From idea**: {idea_data.get('title', 'N/A')}" if idea_data else "**From**: Manual creation"}
"""
    
    (bet_dir / 'README.md').write_text(readme_content)
    
    return bet_dir


def main():
    parser = argparse.ArgumentParser(
        description='Initialize a new little bet directory',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create bet with auto-generated ID
  python new_bet.py "network_topology_opinion"
  
  # Create bet with specific ID
  python new_bet.py "effect_of_X" --id 005
  
  # Create bet from idea JSON
  python new_bet.py "my_bet" --from-idea ideas.json
  
  # Create bet from idea JSON with specific index
  python new_bet.py "my_bet" --from-idea ideas.json --idea-index 2
  
  # Specify output directory
  python new_bet.py "my_bet" --output-dir ./my_bets
        """
    )
    
    parser.add_argument(
        'bet_name',
        help='Name for the bet (will be sanitized for filesystem)'
    )
    
    parser.add_argument(
        '--id',
        type=str,
        help='Bet ID (e.g., "001"). If not provided, auto-generated.'
    )
    
    parser.add_argument(
        '--from-idea',
        type=str,
        help='Load idea from JSON file (from fetch_ideas.py)'
    )
    
    parser.add_argument(
        '--idea-index',
        type=int,
        default=0,
        help='Index of idea to use if JSON contains multiple (default: 0)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='.',
        help='Directory to create bet in (default: current directory)'
    )
    
    parser.add_argument(
        '--no-git',
        action='store_true',
        help='Do not initialize git repository'
    )
    
    args = parser.parse_args()
    
    try:
        # Sanitize bet name
        bet_name = sanitize_name(args.bet_name)
        
        # Determine bet ID
        output_dir = Path(args.output_dir).resolve()
        if args.id:
            bet_id = args.id.zfill(3)  # Pad with zeros
        else:
            bet_id = get_next_bet_id(output_dir)
        
        # Load idea data if provided
        idea_data = None
        if args.from_idea:
            idea_path = Path(args.from_idea)
            if not idea_path.exists():
                print(f"Error: Idea file not found: {idea_path}", file=sys.stderr)
                sys.exit(1)
            
            ideas = load_idea_from_json(idea_path)
            if isinstance(ideas, list):
                if args.idea_index >= len(ideas):
                    print(f"Error: Idea index {args.idea_index} out of range (found {len(ideas)} ideas)", file=sys.stderr)
                    sys.exit(1)
                idea_data = ideas[args.idea_index]
            else:
                idea_data = ideas
        
        # Create bet directory
        print(f"Creating bet {bet_id}: {bet_name}", file=sys.stderr)
        bet_dir = create_bet_directory(bet_id, bet_name, output_dir, idea_data)
        
        print(f"✅ Created bet directory: {bet_dir}", file=sys.stderr)
        print(f"\nNext steps:", file=sys.stderr)
        print(f"  1. cd {bet_dir}", file=sys.stderr)
        print(f"  2. Edit design.md", file=sys.stderr)
        print(f"  3. Implement experiment.py", file=sys.stderr)
        print(f"  4. Run: python experiment.py", file=sys.stderr)
        
        # Initialize git if requested
        if not args.no_git:
            try:
                import subprocess
                subprocess.run(['git', 'init'], cwd=bet_dir, check=False, capture_output=True)
                print(f"\n📦 Initialized git repository", file=sys.stderr)
            except Exception:
                pass  # Git not available, that's okay
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
