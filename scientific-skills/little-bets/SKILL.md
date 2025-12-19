---
name: little-bets
description: "Rapid research prototyping through mini-experiments. A meta-skill for exploring ideas quickly with time-boxed experiments, toy datasets, and structured decision-making."
allowed-tools: [Read, Write, Edit, Bash, WebFetch, WebSearch]
---

# Little Bets: Rapid Research Prototyping

> "Little bets are concrete actions taken to discover, test, and develop ideas that are achievable and affordable."
> — Peter Sims, *Little Bets: How Breakthrough Ideas Emerge from Small Discoveries*

## Overview

The **Little Bets** methodology transforms research exploration from analysis paralysis into action. Instead of planning the perfect experiment, you rapidly prototype ideas through small, time-boxed experiments that provide quick feedback and guide next steps.

A "little bet" is:
- **Small**: 2-4 hours maximum
- **Concrete**: Produces a tangible result
- **Informative**: Answers a specific question
- **Documented**: Every bet generates learnings

This skill orchestrates other scientific skills (arxiv-database, exploratory-data-analysis, hypothesis-generation) into a cohesive rapid prototyping workflow.

## When to Use

✅ **Use Little Bets when:**
- Exploring a new research direction with uncertainty
- Validating whether an approach is worth deeper investment
- Breaking out of "research paralysis" 
- Testing many ideas quickly to find promising ones
- Need empirical evidence before committing to a direction
- Learning a new method or domain

❌ **Don't use Little Bets when:**
- You already know the approach works (just implement it)
- The experiment requires extensive infrastructure
- Results need statistical rigor for publication
- The question can be answered by reading a paper

## The Little Bets Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│    │  IDEAS   │────▶│  SCOUT   │────▶│  DESIGN  │              │
│    │  INBOX   │     │  ARXIV   │     │ TOY CASE │              │
│    └──────────┘     └──────────┘     └──────────┘              │
│         ▲                                  │                    │
│         │                                  ▼                    │
│    ┌──────────┐                      ┌──────────┐              │
│    │  REFINE  │◀────────────────────│ BUILD &  │              │
│    │  IDEAS   │                      │   RUN    │              │
│    └──────────┘                      └──────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Core Workflow

### Phase 1: Ideas Inbox

Load ideas from a GitHub gist that serves as your research ideas inbox.

```bash
# Fetch ideas from gist
gh gist view YOUR_GIST_URL --raw
```

Or use the provided script:

```bash
python scripts/fetch_ideas.py YOUR_GIST_URL --list
```

**Idea Format** (in your gist):
```markdown
## Idea: Effect of network topology on opinion dynamics
- Domain: computational social science
- Motivation: Different network structures might accelerate/slow consensus
- Quick test: Simulate on small graphs, measure convergence time
- Priority: high

## Idea: Using LLMs for synthetic data augmentation
- Domain: ML/NLP
- Motivation: Generate training examples for rare classes
- Quick test: Generate 100 examples, check quality
- Priority: medium
```

### Phase 2: Scout ArXiv

Use the `arxiv-database` skill to quickly survey the literature:

```python
from arxiv_client import ArxivClient

client = ArxivClient()

# Quick search for relevant papers
papers = client.search("opinion dynamics network topology", max_results=15)

# Focus on methodology
for p in papers:
    print(f"[{p['published']}] {p['title']}")
    print(f"   {p['abstract'][:200]}...")
    print()
```

Or use the streamlined scouting script:

```bash
python scripts/scout_arxiv.py "opinion dynamics network" --max 15 --focus methods
```

**Scout Output**: Note down:
- Common datasets used
- Baseline methods to compare against
- Typical evaluation metrics
- Simple versions you can implement

### Phase 3: Design Toy Case

Create a minimal experiment using the design template:

```bash
python scripts/new_bet.py "network_topology_opinion" --id 001
```

Fill in `design.md`:
- **Core Question**: Single, answerable question
- **Hypothesis**: If X then Y because Z
- **Data**: Smallest dataset that could work
- **Method**: Simplest implementation
- **Success Criteria**: What would make this worth continuing?

**Toy Data Strategy Table**:

| Domain | Strategy | Example |
|--------|----------|---------|
| Networks | Small synthetic graphs | 50-node Erdos-Renyi, Watts-Strogatz |
| Text | Sample from existing corpus | 100 sentences from benchmark |
| Tabular | sklearn.datasets | make_classification(n=500) |
| Images | MNIST/CIFAR subset | 100 images per class |
| Time series | Synthetic patterns | AR(1) with known parameters |

### Phase 4: Build & Run

Implement using the experiment template:

```python
# bet_001_network_topology/experiment.py

import networkx as nx
import numpy as np

# === TOY DATA ===
def create_toy_data(n_nodes=50, seed=42):
    """Generate small test networks."""
    np.random.seed(seed)
    graphs = {
        'erdos_renyi': nx.erdos_renyi_graph(n_nodes, 0.1, seed=seed),
        'watts_strogatz': nx.watts_strogatz_graph(n_nodes, 4, 0.3, seed=seed),
        'barabasi_albert': nx.barabasi_albert_graph(n_nodes, 2, seed=seed),
    }
    return graphs

# === METHOD ===
def run_opinion_dynamics(graph, steps=100):
    """Simplest opinion dynamics: average with neighbors."""
    opinions = np.random.random(len(graph.nodes))
    
    for _ in range(steps):
        new_opinions = opinions.copy()
        for node in graph.nodes:
            neighbors = list(graph.neighbors(node))
            if neighbors:
                new_opinions[node] = np.mean(opinions[list(neighbors) + [node]])
        opinions = new_opinions
    
    return np.std(opinions)  # Consensus = low std

# === MAIN ===
graphs = create_toy_data()
for name, G in graphs.items():
    consensus = run_opinion_dynamics(G)
    print(f"{name}: final std = {consensus:.4f}")
```

**Time Budget**: Set a timer! When time is up, document what you have.

### Phase 5: Refine

After the experiment, make a decision:

| Result | Decision | Action |
|--------|----------|--------|
| 🔥 Exciting | Continue | Design larger experiment |
| ✅ Promising | Iterate | Refine hypothesis, try variation |
| 🤔 Unclear | Pivot | Change approach, same question |
| ❌ Dead end | Park | Document learnings, move on |
| 💡 Pivot | New bet | Found different interesting question |

Update your ideas gist with learnings and spawn new ideas.

## Quick Start: Your First Little Bet

**10-minute setup**:

1. **Choose an idea** from your inbox (or pick one now)
2. **Create bet directory**:
   ```bash
   python scripts/new_bet.py "my_first_bet" --id 001
   ```
3. **Fill in design.md**: 5 minutes maximum
4. **Implement in experiment.py**: 30-60 minutes
5. **Run and analyze**: 15-30 minutes
6. **Document in results.md**: 10 minutes
7. **Decision**: Continue, pivot, or park

**Total time**: 60-120 minutes for complete feedback loop.

## Skill Integration

Little Bets orchestrates other skills effectively:

### Literature Discovery

| Skill | Use Case | When |
|-------|----------|------|
| `arxiv-database` | Quick methodology scan | Phase 2: Scout |
| `pubmed-database` | Biomedical literature | Phase 2: Scout |
| `openalex-database` | Cross-disciplinary | Phase 2: Scout |
| `research-lookup` | Deep dive on key papers | After promising bet |

### Data & Analysis

| Skill | Use Case | When |
|-------|----------|------|
| `exploratory-data-analysis` | Understand dataset | Phase 3: Design |
| `hypothesis-generation` | Formalize findings | Phase 5: Refine |

### Visualization

| Skill | Use Case | When |
|-------|----------|------|
| `matplotlib` | Quick plots | Phase 4: Build |
| `seaborn` | Statistical viz | Phase 4: Build |

### ML & Statistics

| Skill | Use Case | When |
|-------|----------|------|
| `scikit-learn` | ML prototypes | Phase 4: Build |
| `statsmodels` | Statistical tests | Phase 4: Build |
| `networkx` | Graph analysis | Phase 4: Build |

## Bet Management

### Directory Structure

```
little_bets/
├── bet_001_topic_a/
│   ├── design.md          # Experiment design
│   ├── experiment.py      # Implementation
│   ├── results.md         # Findings
│   ├── data/              # Local data
│   └── results/           # Outputs, figures
├── bet_002_topic_b/
│   └── ...
└── bets_log.md            # Summary of all bets
```

### Tracking Progress

```bash
# View status of all bets
python scripts/bet_status.py

# Export tracking log
python scripts/bet_status.py --export bets_log.md
```

Output:
```
| ID  | Name          | Started    | Status   | Time   | Key Finding        |
|-----|---------------|------------|----------|--------|-------------------|
| 001 | network_topo  | 2025-01-15 | ✅ Done  | 2h/4h  | Topology matters   |
| 002 | llm_augment   | 2025-01-16 | 🔄 Active| 1h/2h  | Quality varies     |
```

## Best Practices

### Do ✅

- Set a timer before starting
- Write down success criteria BEFORE experimenting
- Use the simplest possible implementation first
- Document failures (they're valuable!)
- Stop when time is up, even if not "done"
- Share learnings in ideas inbox
- Keep toy datasets tiny (10-100 samples often enough)

### Don't ❌

- Spend time perfecting code style
- Build infrastructure for hypothetical scale
- Collect full dataset before validating approach
- Optimize prematurely
- Skip documentation ("I'll remember")
- Merge exploration with production code

## Common Patterns

### 1. Method Validation
**Question**: Does method X work at all for problem Y?
**Data**: Synthetic with known answer
**Success**: Recovers known structure

### 2. Effect Size Estimation  
**Question**: Is there any detectable effect?
**Data**: Small real sample
**Success**: Effect size > noise

### 3. Feasibility Check
**Question**: Can we even get/generate this data?
**Data**: Manual collection of 10-20 examples
**Success**: Data exists and is accessible

### 4. Baseline Establishment
**Question**: What does naive approach achieve?
**Data**: Benchmark subset
**Success**: Have baseline to beat

### 5. Scaling Probe
**Question**: Does performance change with scale?
**Data**: 10, 100, 1000 samples
**Success**: Understand scaling behavior

## Templates & Scripts

This skill provides:

**Templates** (in `assets/`):
- `design_template.md` - Structure experiment design
- `experiment_template.py` - Boilerplate for experiments
- `results_template.md` - Document findings

**Scripts** (in `scripts/`):
- `fetch_ideas.py` - Load ideas from GitHub gist
- `scout_arxiv.py` - Streamlined literature search
- `new_bet.py` - Initialize new bet directory
- `bet_status.py` - Track all bets

## Philosophy

Little Bets is built on these principles:

1. **Action over analysis**: Do something small rather than plan something big
2. **Failing fast is succeeding fast**: Quick experiments reveal dead ends early  
3. **Compound learning**: Each bet builds intuition, even failures
4. **Documentation as investment**: Written learnings pay dividends
5. **Time-boxing forces decisions**: Constraints breed creativity

> "The key is to make lots of little bets, stay nimble, and be ready to change direction when you learn what does and doesn't work."

## See Also

- `arxiv-database` - ArXiv paper search and analysis
- `research-lookup` - Deep paper analysis
- `exploratory-data-analysis` - Dataset exploration
- `hypothesis-generation` - Formalizing hypotheses
- `scientific-writing` - Writing up results
