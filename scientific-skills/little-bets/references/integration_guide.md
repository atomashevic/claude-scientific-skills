# Integration Guide: Using Other Skills in Little Bets

Little Bets is a meta-skill that orchestrates other scientific skills. This guide shows how to effectively use each skill at different phases of the little bets workflow.

---

## Phase 1: Ideas Inbox

### Skills for Idea Management

**GitHub Gist** (via `gh` CLI):
- Store ideas as markdown
- Version control for idea evolution
- Easy to share and collaborate

**No specific scientific skills needed** - this is about capturing ideas quickly.

---

## Phase 2: Scout ArXiv (Literature Discovery)

### `arxiv-database` Skill

**Primary use**: Quick methodology scan, finding relevant papers.

**When to use**: 
- At the start of a bet to understand the landscape
- When you need methodology inspiration
- To find baseline methods to compare against

**Example workflow**:
```python
# Import from arxiv-database skill
import sys
sys.path.append('../arxiv-database/scripts')
from arxiv_client import ArxivClient

client = ArxivClient()

# Quick search
papers = client.search("graph neural networks node classification", max_results=15)

# Extract key information
for p in papers:
    print(f"[{p['published']}] {p['title']}")
    # Look for: datasets, baselines, metrics
    if 'dataset' in p['abstract'].lower():
        print(f"  → Mentions dataset")
    if 'baseline' in p['abstract'].lower():
        print(f"  → Mentions baseline")
```

**What to extract**:
- Dataset names and sizes
- Baseline methods used
- Evaluation metrics
- Simple methods that might work for your toy case

**Time budget**: 15-30 minutes max. Don't read full papers yet.

---

### `pubmed-database` Skill

**Use case**: Biomedical/health research ideas.

**When to use**: Your bet involves biomedical data or methods.

**Example**:
```python
# Similar pattern to arxiv-database
from pubmed_client import PubMedClient

client = PubMedClient()
results = client.search("machine learning drug discovery", max_results=10)
```

---

### `openalex-database` Skill

**Use case**: Cross-disciplinary search, finding papers across fields.

**When to use**: Your idea spans multiple domains or you want broader perspective.

---

### `research-lookup` Skill

**Use case**: Deep dive on 1-2 key papers after scouting.

**When to use**: 
- After scouting identifies a highly relevant paper
- When you need to understand a method in detail
- Before implementing a method from a paper

**Time budget**: 30-60 minutes. Use sparingly—only for critical papers.

---

## Phase 3: Design Toy Case

### `exploratory-data-analysis` Skill

**Use case**: Understanding a dataset before designing experiment.

**When to use**: 
- You're using real data (even if small)
- You need to understand data structure/distribution
- You want to check data quality

**Example**:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load small dataset
df = pd.read_csv('toy_data.csv')

# Quick EDA
print(df.describe())
print(df.info())
df.hist(figsize=(10, 6))
plt.tight_layout()
plt.savefig('data_overview.png')
```

**Time budget**: 10-20 minutes. Keep it minimal.

---

### `pandas` / `numpy` Skills

**Use case**: Data manipulation and preparation.

**When to use**: Always—these are fundamental tools.

**Quick patterns**:
```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Quick preprocessing
df = df.dropna()  # Remove missing values
df = df.sample(n=100, random_state=42)  # Subsample

# Create features
df['feature'] = df['col1'] * df['col2']
```

---

## Phase 4: Build & Run (Experimentation)

### `scikit-learn` Skill

**Use case**: Machine learning models for classification/regression/clustering.

**When to use**: Your bet involves ML.

**Quick patterns**:
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Simple train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.1%}")
```

**Time budget**: 10-30 minutes for simple models. Don't tune hyperparameters yet.

---

### `statsmodels` Skill

**Use case**: Statistical analysis, hypothesis testing, regression.

**When to use**: Your bet involves statistical inference.

**Example**:
```python
import statsmodels.api as sm

# Simple linear regression
X_with_const = sm.add_constant(X)
model = sm.OLS(y, X_with_const).fit()
print(model.summary())

# Check if effect is significant
print(f"P-value: {model.pvalues[1]:.4f}")
```

---

### `networkx` Skill

**Use case**: Network/graph analysis.

**When to use**: Your bet involves networks, graphs, or relational data.

**Quick patterns**:
```python
import networkx as nx

# Create graph
G = nx.erdos_renyi_graph(n=50, p=0.1)

# Basic analysis
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Connected: {nx.is_connected(G)}")

# Centrality
centrality = nx.degree_centrality(G)
```

---

### `scipy` Skill

**Use case**: Scientific computing, optimization, signal processing.

**When to use**: Your bet needs numerical methods, optimization, or signal processing.

**Example**:
```python
from scipy.optimize import minimize
from scipy.stats import ttest_ind

# Optimization
result = minimize(objective_function, x0=[0, 0])

# Statistical test
t_stat, p_value = ttest_ind(group_a, group_b)
```

---

### `pytorch-lightning` Skill

**Use case**: Deep learning experiments.

**When to use**: Your bet involves neural networks (use sparingly—DL takes longer).

**Guidelines**:
- Keep models small (< 1M parameters)
- Use small datasets (< 1000 samples)
- Limit training to < 100 epochs
- Use pre-trained models when possible

**Time budget**: 60-120 minutes. Consider if DL is necessary for a little bet.

---

## Phase 4: Visualization

### `matplotlib` Skill

**Use case**: Core plotting and visualization.

**When to use**: Always—visualization is crucial for understanding results.

**Quick patterns**:
```python
import matplotlib.pyplot as plt

# Simple plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('Classification Results')
plt.savefig('results.png', dpi=150, bbox_inches='tight')
plt.close()
```

---

### `seaborn` Skill

**Use case**: Statistical visualization, prettier plots.

**When to use**: When you want nicer-looking plots with minimal code.

**Example**:
```python
import seaborn as sns

sns.scatterplot(data=df, x='x', y='y', hue='label')
plt.savefig('results.png')
```

---

### `plotly` Skill

**Use case**: Interactive plots (rarely needed for little bets).

**When to use**: When interactivity helps understand results (usually not necessary).

---

## Phase 5: Refine (Documentation & Analysis)

### `hypothesis-generation` Skill

**Use case**: Formalizing findings into testable hypotheses.

**When to use**: After a promising bet, to formalize what you learned.

**Example workflow**:
1. Little bet shows effect exists
2. Use hypothesis-generation to create formal hypothesis
3. Design follow-up experiment to test hypothesis

---

### `scientific-writing` Skill

**Use case**: Writing up results in a structured way.

**When to use**: After completing a bet, to document findings clearly.

**Note**: Little bets don't need full papers, but clear documentation helps.

---

## Example Workflows

### Workflow 1: ML Method Testing Bet

**Phase 2: Scout**
```python
from arxiv_client import ArxivClient
client = ArxivClient()
papers = client.search("your_method topic", max_results=10)
# Extract: datasets, baselines, metrics
```

**Phase 3: Design**
```python
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=100, n_features=5, random_state=42)
```

**Phase 4: Build**
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
```

**Phase 4: Visualize**
```python
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
plt.savefig('results.png')
```

---

### Workflow 2: Statistical Effect Bet

**Phase 2: Scout**
```python
# Use arxiv-database to find similar studies
papers = client.search("effect of X on Y", max_results=10)
```

**Phase 3: Design**
```python
# Generate data with known effect
np.random.seed(42)
treatment = np.random.randn(50) + 1.0  # Effect size = 1.0
control = np.random.randn(50)
```

**Phase 4: Build**
```python
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(treatment, control)
print(f"Effect size: {np.mean(treatment) - np.mean(control):.2f}")
print(f"P-value: {p_value:.4f}")
```

**Phase 4: Visualize**
```python
plt.hist(treatment, alpha=0.5, label='Treatment')
plt.hist(control, alpha=0.5, label='Control')
plt.legend()
plt.savefig('results.png')
```

---

### Workflow 3: Network Analysis Bet

**Phase 2: Scout**
```python
papers = client.search("network analysis topic", max_results=10)
```

**Phase 3: Design**
```python
import networkx as nx
G = nx.erdos_renyi_graph(n=50, p=0.1, seed=42)
```

**Phase 4: Build**
```python
# Analyze network
centrality = nx.degree_centrality(G)
clustering = nx.clustering(G)
print(f"Avg clustering: {np.mean(list(clustering.values())):.3f}")
```

**Phase 4: Visualize**
```python
import matplotlib.pyplot as plt
nx.draw(G, node_size=100, with_labels=False)
plt.savefig('network.png')
```

---

## Skill Selection Decision Tree

```
Start: What phase are you in?
│
├─ Phase 2 (Scout)
│  ├─ General topic? → arxiv-database
│  ├─ Biomedical? → pubmed-database
│  └─ Cross-disciplinary? → openalex-database
│
├─ Phase 3 (Design)
│  ├─ Using real data? → exploratory-data-analysis
│  └─ Always: pandas, numpy
│
├─ Phase 4 (Build)
│  ├─ ML problem? → scikit-learn
│  ├─ Statistical inference? → statsmodels
│  ├─ Networks? → networkx
│  ├─ Deep learning? → pytorch-lightning (use sparingly)
│  └─ Scientific computing? → scipy
│
├─ Phase 4 (Visualize)
│  ├─ Quick plot? → matplotlib
│  └─ Statistical viz? → seaborn
│
└─ Phase 5 (Refine)
   ├─ Formalize findings? → hypothesis-generation
   └─ Write up? → scientific-writing
```

---

## Time Budget Guidelines

| Phase | Skill | Time Budget |
|-------|-------|-------------|
| Scout | arxiv-database | 15-30 min |
| Scout | research-lookup | 30-60 min (sparingly) |
| Design | exploratory-data-analysis | 10-20 min |
| Build | scikit-learn | 10-30 min |
| Build | statsmodels | 15-30 min |
| Build | networkx | 10-20 min |
| Build | pytorch-lightning | 60-120 min (avoid if possible) |
| Visualize | matplotlib | 5-15 min |
| Refine | hypothesis-generation | 10-20 min |

**Total per bet**: 2-4 hours maximum.

---

## Best Practices

1. **Use skills minimally**: Don't over-engineer
2. **Import only what you need**: Keep dependencies light
3. **Document skill usage**: Note which skills you used in bet documentation
4. **Reuse patterns**: Build a library of quick patterns for each skill
5. **Time-box skill usage**: Set timers for each phase

---

## Common Mistakes

❌ **Reading too many papers**: Scout quickly, don't deep-dive  
❌ **Over-engineering data**: Simple synthetic data is fine  
❌ **Tuning hyperparameters**: Not needed for little bets  
❌ **Using deep learning**: Usually too slow for little bets  
❌ **Perfect visualizations**: Quick plots are enough  
❌ **Full statistical rigor**: Quick checks are sufficient  

✅ **Quick and dirty**: Get signal fast, refine later if promising
