# ArXiv Search Examples

Comprehensive collection of search query examples organized by use case.

## Quick Reference

| Use Case | Query Pattern |
|----------|---------------|
| Simple search | `machine learning` |
| Title search | `ti:transformer` |
| Author search | `au:Vaswani` |
| Abstract search | `abs:attention` |
| Category search | `cat:cs.LG` |
| Phrase match | `ti:"large language model"` |
| Boolean AND | `ti:deep AND abs:learning` |
| Boolean OR | `cat:cs.LG OR cat:cs.AI` |
| Exclude | `cat:cs.LG ANDNOT ti:survey` |

## Basic Searches

### Simple Keyword Search

```python
# Search all fields
results = client.search("machine learning", max_results=20)
```

### Title Search

```python
# Find papers with specific title keywords
results = client.search("ti:transformer", max_results=20)

# Multiple title keywords
results = client.search("ti:efficient transformer", max_results=20)
```

### Abstract Search

```python
# Search in abstracts
results = client.search("abs:attention mechanism", max_results=20)

# Phrase search in abstract
results = client.search('abs:"self-attention"', max_results=20)
```

### Author Search

```python
# Find papers by author
results = client.search("au:Vaswani", max_results=50)

# Full author name
results = client.search("au:Ashish Vaswani", max_results=50)

# Multiple authors (any of them)
results = client.search("au:Vaswani OR au:Devlin OR au:Brown", max_results=50)
```

### Category Search

```python
# All papers in a category
results = client.search("cat:cs.LG", max_results=50)

# Multiple categories
results = client.search("cat:cs.LG OR cat:stat.ML", max_results=50)
```

## Combined Searches

### Category + Keywords

```python
# ML papers about transformers
results = client.search("cat:cs.LG AND ti:transformer", max_results=50)

# Computer vision papers about detection
results = client.search("cat:cs.CV AND (ti:detection OR abs:detector)", max_results=50)

# NLP papers about large language models
results = client.search("cat:cs.CL AND abs:large language model", max_results=50)
```

### Author + Topic

```python
# Author's work on specific topic
results = client.search("au:LeCun AND ti:convolutional", max_results=20)

# Multiple authors on topic
results = client.search("(au:Hinton OR au:Bengio) AND ti:deep learning", max_results=30)
```

### Title + Abstract

```python
# Both title and abstract contain keywords
results = client.search("ti:efficient AND abs:optimization", max_results=30)

# Title keyword with abstract phrase
results = client.search('ti:neural AND abs:"gradient descent"', max_results=30)
```

## Boolean Queries

### AND Operator

```python
# Both conditions must match
results = client.search("ti:quantum AND abs:computing", max_results=20)

# Multiple ANDs
results = client.search("ti:deep AND abs:learning AND abs:neural", max_results=20)
```

### OR Operator

```python
# Either condition matches
results = client.search("ti:transformer OR ti:attention", max_results=30)

# Multiple ORs
results = client.search("ti:GAN OR ti:VAE OR ti:diffusion", max_results=50)

# Categories OR
results = client.search("cat:cs.LG OR cat:cs.AI OR cat:stat.ML", max_results=100)
```

### ANDNOT Operator

```python
# Exclude terms
results = client.search("cat:cs.LG ANDNOT ti:survey", max_results=50)

# Exclude multiple terms
results = client.search("cat:cs.LG ANDNOT (ti:survey OR ti:review)", max_results=50)

# Category exclusion
results = client.search("ti:transformer ANDNOT cat:cs.CL", max_results=30)
```

### Complex Boolean

```python
# Nested conditions
results = client.search(
    "(ti:deep OR ti:neural) AND (abs:learning OR abs:training)",
    max_results=30
)

# Multiple categories with keyword
results = client.search(
    "(cat:cs.LG OR cat:cs.AI) AND ti:reinforcement AND abs:policy",
    max_results=30
)

# Full complex query
results = client.search(
    "(cat:cs.LG OR cat:stat.ML) AND (ti:efficient OR abs:scalable) ANDNOT (ti:survey OR ti:review)",
    max_results=50
)
```

## Phrase Matching

### Exact Phrases

```python
# Title phrase
results = client.search('ti:"attention is all you need"', max_results=10)

# Abstract phrase
results = client.search('abs:"deep reinforcement learning"', max_results=30)

# Multi-word phrase
results = client.search('ti:"large language model"', max_results=50)
```

## Domain-Specific Examples

### Machine Learning

```python
# Deep learning papers
results = client.search("cat:cs.LG AND (ti:deep OR abs:neural network)", max_results=50)

# Reinforcement learning
results = client.search("cat:cs.LG AND abs:reinforcement learning", max_results=30)

# Transfer learning
results = client.search("cat:cs.LG AND ti:transfer learning", max_results=30)

# Meta-learning
results = client.search('cat:cs.LG AND (ti:"meta-learning" OR abs:"few-shot")', max_results=30)

# Federated learning
results = client.search("cat:cs.LG AND ti:federated", max_results=30)

# Efficient/Fast models
results = client.search("cat:cs.LG AND (ti:efficient OR ti:fast OR ti:lightweight)", max_results=50)
```

### Large Language Models

```python
# LLM papers
results = client.search('ti:"large language model" OR ti:LLM', max_results=50)

# GPT-related
results = client.search("ti:GPT OR abs:GPT-4 OR abs:ChatGPT", max_results=50)

# Instruction tuning
results = client.search('abs:"instruction tuning" OR abs:"instruction following"', max_results=30)

# RLHF
results = client.search('abs:"reinforcement learning from human feedback" OR abs:RLHF', max_results=30)

# Prompt engineering
results = client.search("ti:prompting OR abs:prompt engineering", max_results=30)
```

### Computer Vision

```python
# Object detection
results = client.search("cat:cs.CV AND (ti:detection OR abs:object detection)", max_results=30)

# Image segmentation
results = client.search("cat:cs.CV AND ti:segmentation", max_results=30)

# Vision transformers
results = client.search("cat:cs.CV AND (ti:ViT OR abs:vision transformer)", max_results=30)

# Image generation
results = client.search("cat:cs.CV AND (ti:diffusion OR ti:GAN OR abs:image generation)", max_results=50)

# 3D vision
results = client.search("cat:cs.CV AND (ti:3D OR abs:point cloud OR abs:depth)", max_results=30)

# Medical imaging
results = client.search("cat:cs.CV AND (abs:medical OR abs:radiology OR abs:pathology)", max_results=30)
```

### Natural Language Processing

```python
# Language models
results = client.search("cat:cs.CL AND (ti:language model OR abs:transformer)", max_results=50)

# Question answering
results = client.search("cat:cs.CL AND abs:question answering", max_results=30)

# Machine translation
results = client.search("cat:cs.CL AND ti:translation", max_results=30)

# Named entity recognition
results = client.search('cat:cs.CL AND abs:"named entity"', max_results=30)

# Sentiment analysis
results = client.search("cat:cs.CL AND abs:sentiment", max_results=30)

# Summarization
results = client.search("cat:cs.CL AND ti:summarization", max_results=30)
```

### Quantitative Biology

```python
# CRISPR papers
results = client.search("cat:q-bio.* AND ti:CRISPR", max_results=30)

# Single-cell analysis
results = client.search("cat:q-bio.QM AND abs:single-cell", max_results=30)

# Protein structure
results = client.search('(cat:q-bio.BM OR cat:q-bio.QM) AND abs:"protein structure"', max_results=30)

# Genomics + ML
results = client.search("cat:q-bio.GN AND (ti:deep OR ti:neural)", max_results=30)

# Drug discovery
results = client.search('cat:q-bio.* AND (ti:drug OR abs:"drug discovery")', max_results=30)
```

### Physics

```python
# Quantum computing
results = client.search("cat:quant-ph AND ti:quantum computing", max_results=30)

# Quantum machine learning
results = client.search("(cat:quant-ph OR cat:cs.LG) AND abs:quantum machine learning", max_results=30)

# Materials science
results = client.search("cat:cond-mat.mtrl-sci", max_results=30)

# Neural network potentials
results = client.search('cat:physics.* AND abs:"neural network potential"', max_results=30)
```

### Statistics

```python
# Statistical ML
results = client.search("cat:stat.ML", max_results=50)

# Bayesian methods
results = client.search("cat:stat.* AND ti:Bayesian", max_results=30)

# Causal inference
results = client.search('cat:stat.* AND (ti:causal OR abs:"causal inference")', max_results=30)

# Time series
results = client.search('cat:stat.* AND ti:"time series"', max_results=30)
```

## Filtering & Exclusion

### Exclude Surveys/Reviews

```python
# Original research only
results = client.search(
    "cat:cs.LG ANDNOT (ti:survey OR ti:review OR ti:tutorial)",
    max_results=50
)
```

### Exclude Specific Topics

```python
# ML without computer vision
results = client.search("cat:cs.LG ANDNOT cat:cs.CV", max_results=50)

# NLP without machine translation
results = client.search("cat:cs.CL ANDNOT ti:translation", max_results=50)
```

### Focus on Recent Work

```python
# Get recent papers and sort by date
results = client.search(
    "cat:cs.LG",
    max_results=100,
    sort_by="submittedDate",
    sort_order="descending"
)
```

## Workflow Examples

### Literature Review

```python
# Comprehensive search for a topic
query = """
(cat:cs.LG OR cat:stat.ML) AND
(ti:transformer OR ti:attention) AND
abs:efficient ANDNOT
(ti:survey OR ti:review)
"""
results = client.search(query, max_results=200)

# Filter in code for more control
relevant = [
    p for p in results
    if any(kw in p['abstract'].lower() for kw in ['optimization', 'pruning', 'quantization'])
]
```

### Author Tracking

```python
# Monitor multiple authors
authors = ["Vaswani", "Devlin", "Brown", "Radford", "Sutskever"]
all_papers = []

for author in authors:
    papers = client.search(
        f"au:{author}",
        max_results=20,
        sort_by="submittedDate",
        sort_order="descending"
    )
    all_papers.extend(papers)

# Deduplicate and sort
seen = set()
unique = []
for p in sorted(all_papers, key=lambda x: x['published'], reverse=True):
    if p['arxiv_id'] not in seen:
        seen.add(p['arxiv_id'])
        unique.append(p)
```

### Category Monitoring

```python
# Monitor multiple related categories
categories = ["cs.LG", "cs.AI", "cs.CV", "cs.CL", "stat.ML"]

for cat in categories:
    recent = client.get_recent(category=cat, max_results=10)
    print(f"\n=== {cat} ===")
    for paper in recent:
        print(f"  {paper['title'][:60]}...")
```

### Trending Topics

```python
# Find recent highly-discussed topics
topics = [
    ("LLM", 'ti:"large language model" OR ti:LLM'),
    ("Diffusion", "ti:diffusion"),
    ("Vision Transformer", "ti:ViT OR ti:vision transformer"),
    ("RLHF", "abs:RLHF OR abs:reinforcement learning from human feedback"),
]

for name, query in topics:
    results = client.search(query, max_results=20, sort_by="submittedDate")
    print(f"{name}: {len(results)} recent papers")
```

## Tips for Effective Searches

### 1. Start Broad, Then Narrow

```python
# Start with category
results = client.search("cat:cs.LG", max_results=100)

# Then add keywords
results = client.search("cat:cs.LG AND ti:efficient", max_results=50)

# Then add constraints
results = client.search("cat:cs.LG AND ti:efficient AND abs:transformer", max_results=30)
```

### 2. Use Multiple Variations

```python
# Cover different phrasings
results = client.search(
    'ti:efficient OR ti:fast OR ti:lightweight OR abs:"low complexity"',
    max_results=50
)
```

### 3. Combine Field Tags Strategically

```python
# Title for main topic, abstract for methods
results = client.search("ti:sentiment AND abs:BERT", max_results=30)

# Category for field, title for specific topic
results = client.search("cat:cs.CV AND ti:detection", max_results=30)
```

### 4. Use Exclusions Carefully

```python
# Exclude noise without over-filtering
results = client.search(
    "cat:cs.LG AND ti:optimization ANDNOT ti:survey",
    max_results=50
)
```

### 5. Sort Appropriately

```python
# Recent work: sort by date
results = client.search(
    "cat:cs.LG",
    sort_by="submittedDate",
    sort_order="descending"
)

# Relevant work: sort by relevance (for keyword searches)
results = client.search(
    "transformer attention efficient",
    sort_by="relevance"
)
```

## Common Patterns

### Find Seminal Papers (approximate)

```python
# Older papers often have more citations (use external tools for citation count)
# Here we search for well-known paper titles
seminal_queries = [
    'ti:"attention is all you need"',
    'ti:"BERT" AND au:Devlin',
    'ti:"ResNet" OR ti:"deep residual"',
]
```

### Conference Submissions

```python
# Papers mentioning conferences in comments
results = client.search("co:NeurIPS OR co:ICML OR co:ICLR", max_results=50)

# Submitted to specific venue
results = client.search("cat:cs.LG AND co:NeurIPS", max_results=50)
```

### Pre-print vs Published

```python
# Get all papers and filter in code
results = client.search("cat:cs.LG", max_results=100)

# Check for DOI (indicates journal publication)
published = [p for p in results if p.get('doi')]
preprints = [p for p in results if not p.get('doi')]
```
