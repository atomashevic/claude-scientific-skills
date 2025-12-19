# Toy Data Strategies

Quick guide for creating minimal, informative datasets for little bets. The goal is to generate or obtain the smallest dataset that can answer your question.

---

## Principles

1. **Small is beautiful**: 10-100 samples often enough
2. **Known structure**: Ground truth should be recoverable (for validation)
3. **Fast generation**: Should take < 1 minute to create
4. **Document simplifications**: Note what's missing vs. real data

---

## 1. Synthetic Data Strategies

### Random with Known Structure

Generate data where you control the underlying pattern.

**Use Case**: Method validation, testing if algorithms can recover known structure.

**Examples**:

```python
import numpy as np
from sklearn.datasets import make_classification, make_regression

# Classification: Known decision boundary
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_classes=2,
    class_sep=1.5,  # Clear separation
    random_state=42
)

# Regression: Known linear relationship
X, y = make_regression(
    n_samples=100,
    n_features=1,
    noise=10.0,
    bias=0.0,
    random_state=42
)

# Custom: Create your own pattern
def create_custom_pattern(n=100):
    X = np.random.randn(n, 2)
    y = (X[:, 0]**2 + X[:, 1]**2 < 1).astype(int)  # Circle boundary
    return X, y
```

### Parametric Generators

Use domain-specific generators with known parameters.

**Use Case**: Testing methods on data that mimics real structure.

**Examples**:

```python
import networkx as nx

# Networks: Known topology
G_er = nx.erdos_renyi_graph(n=50, p=0.1, seed=42)  # Random
G_ws = nx.watts_strogatz_graph(n=50, k=4, p=0.3, seed=42)  # Small-world
G_ba = nx.barabasi_albert_graph(n=50, m=2, seed=42)  # Scale-free

# Time series: Known dynamics
def ar_process(n=100, phi=0.7, noise_std=1.0):
    """AR(1) process: x_t = phi * x_{t-1} + noise"""
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t-1] + np.random.randn() * noise_std
    return x

# Text: Synthetic corpus
def generate_synthetic_text(n_docs=50, vocab_size=100):
    """Simple bag-of-words documents."""
    vocab = [f"word_{i}" for i in range(vocab_size)]
    docs = []
    for _ in range(n_docs):
        n_words = np.random.randint(10, 50)
        doc = np.random.choice(vocab, size=n_words)
        docs.append(' '.join(doc))
    return docs
```

### Simulation-Based

Simulate a process to generate data.

**Use Case**: Testing methods on data from known generative process.

**Examples**:

```python
# Agent-based simulation
def simulate_opinion_dynamics(n_agents=50, steps=100):
    """Simple opinion dynamics simulation."""
    opinions = np.random.random(n_agents)
    network = nx.erdos_renyi_graph(n_agents, 0.1)
    
    for step in range(steps):
        new_opinions = opinions.copy()
        for node in network.nodes():
            neighbors = list(network.neighbors(node))
            if neighbors:
                neighbor_opinions = opinions[neighbors]
                new_opinions[node] = np.mean(neighbor_opinions)
        opinions = new_opinions
    
    return opinions

# Physical simulation
def simulate_diffusion(n_particles=100, steps=50):
    """Simple diffusion process."""
    positions = np.random.randn(n_particles, 2) * 0.1
    for step in range(steps):
        positions += np.random.randn(n_particles, 2) * 0.01
    return positions
```

---

## 2. Subsampling Strategies

Take a small sample from existing datasets.

### Random Subsample

**Use Case**: Quick test on real data structure.

```python
import pandas as pd

# Load full dataset
df = pd.read_csv('large_dataset.csv')

# Random subsample
df_small = df.sample(n=100, random_state=42)

# Stratified subsample (preserve class distribution)
df_stratified = df.groupby('label').apply(
    lambda x: x.sample(min(50, len(x)), random_state=42)
).reset_index(drop=True)
```

### Representative Subset Selection

**Use Case**: Want diverse examples, not just random.

```python
from sklearn.cluster import KMeans

# Select diverse examples via clustering
kmeans = KMeans(n_clusters=20, random_state=42)
clusters = kmeans.fit_predict(X)

# Select one example per cluster
indices = []
for cluster_id in range(20):
    cluster_indices = np.where(clusters == cluster_id)[0]
    if len(cluster_indices) > 0:
        indices.append(cluster_indices[0])

X_diverse = X[indices]
y_diverse = y[indices]
```

---

## 3. Proxy Data

Use simpler domains that capture the essence of your problem.

### Finding Simpler Domains

**Examples**:
- Instead of real images → use MNIST digits
- Instead of natural language → use synthetic sequences
- Instead of real networks → use synthetic graphs
- Instead of real time series → use AR processes

### Using Benchmark Datasets

**Quick Data Sources**:

```python
from sklearn.datasets import (
    load_iris, load_wine, load_breast_cancer,
    make_moons, make_circles, make_blobs
)

# Classic small datasets
iris = load_iris()
wine = load_wine()

# Synthetic benchmarks
X, y = make_moons(n_samples=100, noise=0.1)
X, y = make_circles(n_samples=100, noise=0.1, factor=0.5)
X, y = make_blobs(n_samples=100, centers=3, n_features=2)
```

### Adapting Public Datasets

**Examples**:

```python
# MNIST subset (images)
from tensorflow.keras.datasets import mnist
(X_train, y_train), _ = mnist.load_data()
X_small = X_train[:100]  # First 100 images
y_small = y_train[:100]

# CIFAR-10 subset (images)
from tensorflow.keras.datasets import cifar10
(X_train, y_train), _ = cifar10.load_data()
X_small = X_train[:100]
y_small = y_train[:100]

# UCI datasets (tabular)
import pandas as pd
url = "https://archive.ics.uci.edu/ml/datasets/wine"
# Download and subsample
```

---

## 4. Domain-Specific Generators

### Networks

```python
import networkx as nx

# Random graphs
G = nx.erdos_renyi_graph(n=50, p=0.1)

# Small-world
G = nx.watts_strogatz_graph(n=50, k=4, p=0.3)

# Scale-free
G = nx.barabasi_albert_graph(n=50, m=2)

# Bipartite
G = nx.bipartite.random_graph(20, 20, 0.2)

# With attributes
G = nx.erdos_renyi_graph(n=50, p=0.1)
nx.set_node_attributes(G, {n: np.random.random() for n in G.nodes()}, 'opinion')
```

### Time Series

```python
# AR processes
def ar_process(n=100, order=1, coeffs=[0.7], noise_std=1.0):
    x = np.zeros(n)
    for t in range(order, n):
        x[t] = sum(coeffs[i] * x[t-i-1] for i in range(order)) + np.random.randn() * noise_std
    return x

# Seasonal patterns
def seasonal_series(n=100, period=12, amplitude=1.0):
    t = np.arange(n)
    return amplitude * np.sin(2 * np.pi * t / period) + np.random.randn(n) * 0.1

# Trends
def trend_series(n=100, slope=0.01):
    t = np.arange(n)
    return slope * t + np.random.randn(n) * 0.5
```

### Text

```python
# Synthetic corpus
def generate_text_corpus(n_docs=50, vocab_size=100, doc_length_range=(10, 50)):
    vocab = [f"word_{i}" for i in range(vocab_size)]
    corpus = []
    for _ in range(n_docs):
        n_words = np.random.randint(*doc_length_range)
        doc = np.random.choice(vocab, size=n_words)
        corpus.append(' '.join(doc))
    return corpus

# With topics (simple LDA-like)
def generate_topical_corpus(n_docs=50, n_topics=3, words_per_topic=20):
    topics = []
    for topic_id in range(n_topics):
        topic_words = [f"topic{topic_id}_word{i}" for i in range(words_per_topic)]
        topics.append(topic_words)
    
    corpus = []
    for _ in range(n_docs):
        topic = np.random.choice(n_topics)
        n_words = np.random.randint(10, 30)
        doc = np.random.choice(topics[topic], size=n_words)
        corpus.append(' '.join(doc))
    return corpus
```

### Images

```python
# Synthetic patterns
def generate_pattern_images(n=100, size=(28, 28)):
    images = []
    for i in range(n):
        img = np.zeros(size)
        # Add pattern (e.g., lines, circles, noise)
        if i % 3 == 0:
            # Horizontal lines
            img[::5, :] = 1.0
        elif i % 3 == 1:
            # Vertical lines
            img[:, ::5] = 1.0
        else:
            # Random noise
            img = np.random.random(size)
        images.append(img)
    return np.array(images)

# Or use MNIST/CIFAR subsets (see above)
```

### Tabular

```python
from sklearn.datasets import (
    make_classification, make_regression, make_blobs,
    make_moons, make_circles, make_s_curve
)

# Classification
X, y = make_classification(n_samples=100, n_features=5, n_classes=2)

# Regression
X, y = make_regression(n_samples=100, n_features=3, noise=10.0)

# Clustering
X, y = make_blobs(n_samples=100, centers=3, n_features=2)

# Non-linear
X, y = make_moons(n_samples=100, noise=0.1)
X, y = make_circles(n_samples=100, noise=0.1)
```

---

## 5. Quick Data Sources

### Built-in Datasets

**sklearn.datasets**:
- `load_iris()`, `load_wine()`, `load_breast_cancer()` - Classic small datasets
- `make_*` functions - Synthetic generators

**TensorFlow/Keras**:
- `mnist`, `cifar10`, `cifar100`, `imdb` - Pre-loaded datasets

**PyTorch**:
- `torchvision.datasets` - Image datasets
- `torchtext.datasets` - Text datasets

### Public Repositories

**UCI ML Repository**:
```python
import pandas as pd

# Many datasets available via direct URLs
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df = pd.read_csv(url, header=None)
```

**OpenML**:
```python
from openml import datasets

# List available datasets
dataset_list = datasets.list_datasets(output_format='dataframe')
# Download specific dataset
dataset = datasets.get_dataset(1)  # e.g., dataset ID 1
X, y, _, _ = dataset.get_data(target=dataset.default_target_attribute)
```

**Kaggle**:
- Many datasets available via `kaggle datasets download`
- Often have small sample versions

### Domain-Specific

**Networks**: NetworkX generators (see above)

**Text**: NLTK corpora, HuggingFace datasets

**Images**: torchvision, tensorflow_datasets

**Time Series**: `tslearn.datasets`, `sktime.datasets`

---

## Strategy Selection Guide

| Your Domain | Recommended Strategy | Example |
|-------------|---------------------|---------|
| ML classification | sklearn.make_classification | 100 samples, 2-5 features |
| ML regression | sklearn.make_regression | 100 samples, linear relationship |
| Networks | networkx generators | 50-node graphs |
| Time series | AR processes | 100 time steps |
| Text | Synthetic corpus | 50 documents, 100 vocab |
| Images | MNIST/CIFAR subset | 100 images per class |
| Tabular | sklearn.make_* or UCI | 100-500 rows |
| Unknown domain | Proxy data | Find similar simpler domain |

---

## Best Practices

1. **Start smaller**: If unsure, start with 10-20 samples, scale up if needed
2. **Document assumptions**: Note what's simplified vs. real data
3. **Check ground truth**: Ensure you can verify results
4. **Reproducibility**: Always set random seeds
5. **Visualize**: Plot small datasets to sanity-check structure

---

## Anti-Patterns

❌ **Too complex**: Generating 10,000 samples defeats the purpose  
❌ **Too simple**: 5 samples might not capture any structure  
❌ **Unrealistic**: Data that doesn't resemble your real problem  
❌ **No ground truth**: Can't verify if method worked  
❌ **Slow generation**: Takes > 5 minutes to generate  

✅ **Sweet spot**: 20-100 samples, known structure, < 1 min generation
