#!/usr/bin/env python3
"""
Little Bet: [ID] [Name]
Question: [Core question this experiment answers]
Date: [YYYY-MM-DD]
Time Budget: [X hours]

Usage:
    python experiment.py
    python experiment.py --seed 123
    python experiment.py --n-samples 200
"""

import argparse
import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional


# === CONFIGURATION ===
BET_ID = "001"
BET_NAME = "your_bet_name"
QUESTION = "Does X affect Y?"
OUTPUT_DIR = Path("results")


# === TOY DATA ===
def create_toy_data(n_samples: int = 100, seed: int = 42) -> Dict[str, Any]:
    """
    Generate minimal dataset for testing.
    
    Guidelines:
    - Keep it SMALL (10-100 samples often enough)
    - Make ground truth recoverable (for validation)
    - Document any simplifications
    
    Args:
        n_samples: Number of samples to generate
        seed: Random seed for reproducibility
    
    Returns:
        Dictionary containing the toy dataset
    """
    np.random.seed(seed)
    
    # TODO: Implement toy data generation
    # Example:
    # X = np.random.randn(n_samples, 2)
    # y = (X[:, 0] + X[:, 1] > 0).astype(int)
    # return {'X': X, 'y': y, 'n_samples': n_samples}
    
    data = {
        'n_samples': n_samples,
        'seed': seed,
        # Add your data here
    }
    
    return data


# === METHOD ===
def run_experiment(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Core experiment logic.
    
    Guidelines:
    - Implement the SIMPLEST possible version first
    - Skip optimization, error handling, edge cases
    - Focus on answering the core question
    
    Args:
        data: Output from create_toy_data()
    
    Returns:
        Dictionary containing experiment results
    """
    # TODO: Implement simplest possible version
    # Example:
    # model = SimpleModel()
    # model.fit(data['X'], data['y'])
    # accuracy = model.score(data['X'], data['y'])
    # return {'accuracy': accuracy, 'model': model}
    
    results = {
        'status': 'not_implemented',
        # Add your results here
    }
    
    return results


# === ANALYSIS ===
def analyze_results(results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Quick analysis of what happened.
    
    Args:
        results: Output from run_experiment()
    
    Returns:
        Analysis summary with decision-relevant information
    """
    analysis = {
        'key_metric': None,
        'key_finding': "",
        'meets_minimum_criteria': False,
        'is_exciting': False,
        'worth_continuing': False,
        'suggested_next_step': "",
        'timestamp': datetime.now().isoformat()
    }
    
    # TODO: Fill in analysis based on results
    # Example:
    # analysis['key_metric'] = results['accuracy']
    # analysis['meets_minimum_criteria'] = results['accuracy'] > 0.6
    # analysis['is_exciting'] = results['accuracy'] > 0.9
    # analysis['worth_continuing'] = analysis['meets_minimum_criteria']
    # analysis['key_finding'] = f"Achieved {results['accuracy']:.1%} accuracy"
    # analysis['suggested_next_step'] = "Try with more features" if analysis['worth_continuing'] else "Park this idea"
    
    return analysis


def plot_results(
    data: Dict[str, Any],
    results: Dict[str, Any],
    save_path: Path
) -> None:
    """
    Quick visualization of results.
    
    Guidelines:
    - One clear figure that shows the main finding
    - Don't spend time on aesthetics
    - Include title with key result
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # TODO: Create plot
    # Example:
    # ax.scatter(data['X'][:, 0], data['X'][:, 1], c=data['y'], cmap='coolwarm')
    # ax.set_title(f"Classification Result (acc={results['accuracy']:.1%})")
    # ax.set_xlabel("Feature 1")
    # ax.set_ylabel("Feature 2")
    
    ax.text(0.5, 0.5, "TODO: Add visualization", 
            ha='center', va='center', transform=ax.transAxes)
    ax.set_title(f"Little Bet {BET_ID}: {BET_NAME}")
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved figure to {save_path}")


def save_results(
    data: Dict[str, Any],
    results: Dict[str, Any],
    analysis: Dict[str, Any],
    output_dir: Path
) -> None:
    """Save all results to files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save analysis summary
    summary_path = output_dir / "summary.json"
    with open(summary_path, 'w') as f:
        json.dump({
            'bet_id': BET_ID,
            'bet_name': BET_NAME,
            'question': QUESTION,
            'analysis': analysis,
            'data_config': {
                'n_samples': data.get('n_samples'),
                'seed': data.get('seed')
            }
        }, f, indent=2, default=str)
    print(f"  Saved summary to {summary_path}")
    
    # Save human-readable summary
    txt_path = output_dir / "summary.txt"
    with open(txt_path, 'w') as f:
        f.write(f"Little Bet {BET_ID}: {BET_NAME}\n")
        f.write(f"{'=' * 50}\n\n")
        f.write(f"Question: {QUESTION}\n\n")
        f.write("Analysis:\n")
        for k, v in analysis.items():
            f.write(f"  {k}: {v}\n")
    print(f"  Saved text summary to {txt_path}")


# === MAIN ===
def main(n_samples: int = 100, seed: int = 42) -> Dict[str, Any]:
    """Run the complete experiment pipeline."""
    
    print(f"\n{'=' * 60}")
    print(f"Little Bet {BET_ID}: {BET_NAME}")
    print(f"Question: {QUESTION}")
    print(f"{'=' * 60}\n")
    
    # Step 1: Create toy data
    print("1. Creating toy data...")
    data = create_toy_data(n_samples=n_samples, seed=seed)
    print(f"   Created dataset with {data.get('n_samples', '?')} samples")
    
    # Step 2: Run experiment
    print("\n2. Running experiment...")
    results = run_experiment(data)
    print(f"   Status: {results.get('status', 'completed')}")
    
    # Step 3: Analyze results
    print("\n3. Analyzing results...")
    analysis = analyze_results(results)
    
    # Step 4: Save outputs
    print("\n4. Saving outputs...")
    save_results(data, results, analysis, OUTPUT_DIR)
    plot_results(data, results, OUTPUT_DIR / "results.png")
    
    # Step 5: Print summary
    print(f"\n{'=' * 60}")
    print("RESULTS SUMMARY")
    print(f"{'=' * 60}")
    print(f"\nKey Finding: {analysis['key_finding']}")
    print(f"Key Metric: {analysis['key_metric']}")
    print(f"Meets Minimum Criteria: {'✅' if analysis['meets_minimum_criteria'] else '❌'}")
    print(f"Is Exciting: {'🔥' if analysis['is_exciting'] else '—'}")
    print(f"\nDecision: {'Continue' if analysis['worth_continuing'] else 'Park/Pivot'}")
    print(f"Next Step: {analysis['suggested_next_step']}")
    print(f"\nResults saved to: {OUTPUT_DIR.absolute()}/")
    print(f"{'=' * 60}\n")
    
    return analysis


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Little Bet {BET_ID}: {BET_NAME}"
    )
    parser.add_argument(
        '--n-samples', type=int, default=100,
        help='Number of samples for toy data (default: 100)'
    )
    parser.add_argument(
        '--seed', type=int, default=42,
        help='Random seed for reproducibility (default: 42)'
    )
    
    args = parser.parse_args()
    main(n_samples=args.n_samples, seed=args.seed)
