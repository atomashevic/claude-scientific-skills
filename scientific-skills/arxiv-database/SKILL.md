---
name: arxiv-database
description: "Search and browse ArXiv preprints. Query by title, abstract, author, category. Browse recent papers, skim abstracts, filter by subject area (cs, q-bio, physics, math, etc.). Export to BibTeX/JSON/CSV. For quick abstract skimming and staying current with latest research across physics, mathematics, computer science, quantitative biology, and more."
---

# ArXiv Database

## Overview

ArXiv is a preprint repository hosting 2M+ scholarly articles across physics, mathematics, computer science, quantitative biology, statistics, electrical engineering, and economics. This skill provides robust tools for searching ArXiv papers, browsing recent submissions, skimming abstracts, and exporting results in multiple formats.

**Key Features:**
- Search by keywords, title, abstract, author, or category
- Browse recent papers with date filtering
- Skim abstracts with keyword highlighting
- Export to JSON, CSV, or BibTeX formats
- Rate limiting with exponential backoff
- Local caching for faster repeated queries

## When to Use This Skill

This skill should be used when:
- Searching for preprints in physics, math, CS, quantitative biology, or statistics
- Browsing recent papers to stay current in a field
- Quickly skimming abstracts to assess paper relevance
- Finding papers by specific authors
- Conducting literature searches before a project
- Exporting citations for reference management
- Monitoring new submissions in specific categories

## Quick Start

### Installation

```bash
uv pip install requests
```

### Basic Usage

```python
from scripts.arxiv_client import ArxivClient

client = ArxivClient()

# Search for papers
results = client.search("machine learning", max_results=10)

# Display results
for paper in results:
    print(f"\n{paper['title']}")
    print(f"Authors: {', '.join(paper['authors'][:3])}")
    print(f"Abstract: {paper['abstract'][:200]}...")
```

### Command-Line Tool

```bash
# Browse recent ML papers
python scripts/abstract_skimmer.py --category cs.LG --max 20

# Search with keyword highlighting
python scripts/abstract_skimmer.py --query "transformer attention" --keywords transformer attention

# Export to BibTeX
python scripts/abstract_skimmer.py --category cs.AI --max 50 --bibtex refs.bib
```

## Core Capabilities

### 1. Search Papers

Search ArXiv by keywords, with support for field-specific queries.

**Basic Search:**
```python
# Simple keyword search
results = client.search("quantum computing", max_results=20)

# Search with field tags
results = client.search(
    query="ti:transformer AND abs:attention mechanism",
    max_results=50
)
```

**Field Tags:**
| Tag | Field | Example |
|-----|-------|---------|
| `ti:` | Title | `ti:neural network` |
| `au:` | Author | `au:Vaswani` |
| `abs:` | Abstract | `abs:deep learning` |
| `cat:` | Category | `cat:cs.LG` |
| `co:` | Comment | `co:ICML` |
| `all:` | All fields | `all:reinforcement` |

**Boolean Operators:**
```python
# AND - both conditions
results = client.search("ti:transformer AND abs:attention")

# OR - either condition
results = client.search("cat:cs.LG OR cat:stat.ML")

# ANDNOT - exclude
results = client.search("cat:cs.LG ANDNOT ti:survey")
```

**Phrase Matching:**
```python
# Exact phrase
results = client.search('ti:"attention is all you need"')
```

### 2. Browse Recent Papers

Get the latest submissions in specific categories for daily abstract skimming.

```python
# Recent papers in Machine Learning
recent = client.get_recent(category="cs.LG", max_results=50)

# Recent papers from last 7 days
recent = client.get_recent(
    category="cs.AI",
    days_back=7,
    max_results=100
)

# Recent papers with keyword filter
recent = client.get_recent(
    category="q-bio.QM",
    query="ti:CRISPR",
    max_results=30
)
```

### 3. Author Search

Find all papers by a specific author.

```python
# Search by author
papers = client.search_by_author("Vaswani", max_results=50)

# Author + topic
papers = client.search(
    query="au:LeCun AND ti:convolutional",
    max_results=20
)
```

### 4. Get Paper Details

Retrieve specific papers by ArXiv ID.

```python
# By ArXiv ID
paper = client.get_paper("2301.12345")

# By URL
paper = client.get_paper("https://arxiv.org/abs/2301.12345")

# Multiple papers (batch)
papers = client.get_papers(["2301.12345", "2302.23456", "2303.34567"])
```

### 5. Abstract Skimming with Highlighting

Use keyword highlighting to quickly scan abstracts.

```python
from scripts.arxiv_client import ArxivClient

client = ArxivClient()
results = client.search("cat:cs.LG AND ti:transformer", max_results=20)

# Highlight keywords
keywords = ["attention", "transformer", "efficient"]

for paper in results:
    highlighted = client.highlight_keywords(paper['abstract'], keywords)
    print(f"\n{paper['title']}")
    print(highlighted)
```

**Command-line with highlighting:**
```bash
python scripts/abstract_skimmer.py \
    --query "ti:transformer" \
    --keywords attention efficient scalable \
    --max 20
```

### 6. Export Results

Export search results in multiple formats for reference management.

**JSON Export:**
```python
results = client.search("quantum computing", max_results=50)
client.export_json(results, "quantum_papers.json")
```

**CSV Export:**
```python
client.export_csv(results, "quantum_papers.csv")
```

**BibTeX Export:**
```python
client.export_bibtex(results, "quantum_papers.bib")
```

**Command-line:**
```bash
# Export to all formats
python scripts/abstract_skimmer.py \
    --category cs.LG \
    --max 50 \
    --export results.json \
    --csv results.csv \
    --bibtex results.bib
```

### 7. Pagination for Large Queries

Retrieve all results for comprehensive searches.

```python
# Get all papers (with pagination)
all_papers = client.paginate_all(
    query="cat:cs.LG AND ti:optimization",
    max_results=500,
    page_size=100
)
```

### 8. Caching

Enable caching to speed up repeated queries.

```python
# Initialize with caching
client = ArxivClient(
    cache_dir="./arxiv_cache",
    cache_ttl_hours=24
)

# First query hits API
results = client.search("machine learning")

# Second identical query uses cache (instant)
results = client.search("machine learning")
```

## Command-Line Interface

The `abstract_skimmer.py` tool provides quick access to ArXiv from the terminal.

### Usage

```bash
python scripts/abstract_skimmer.py [OPTIONS]
```

### Options

**Search Options:**
| Option | Description |
|--------|-------------|
| `--query, -q` | Search query (supports field tags) |
| `--category, -c` | ArXiv category (e.g., cs.LG) |
| `--author, -a` | Search by author name |
| `--title, -t` | Search by title keywords |

**Filter Options:**
| Option | Description |
|--------|-------------|
| `--max, -m` | Maximum results (default: 20) |
| `--days-back, -d` | Only papers from last N days |
| `--keywords, -k` | Filter and highlight keywords |

**Display Options:**
| Option | Description |
|--------|-------------|
| `--format, -f` | Output format: compact, detailed, oneline, abstract |
| `--no-color` | Disable colored output |
| `--summary` | Show summary statistics |

**Export Options:**
| Option | Description |
|--------|-------------|
| `--export, -e` | Export to JSON file |
| `--csv` | Export to CSV file |
| `--bibtex, -b` | Export to BibTeX file |

### Examples

```bash
# Browse recent ML papers with abstract view
python scripts/abstract_skimmer.py -c cs.LG -m 20

# Search with keyword highlighting
python scripts/abstract_skimmer.py \
    -q "ti:large language model" \
    -k LLM transformer attention \
    --format abstract

# Quick one-line scan
python scripts/abstract_skimmer.py -c cs.CV -m 50 --format oneline

# Detailed view of author's papers
python scripts/abstract_skimmer.py -a "Hinton" --format detailed

# Export to BibTeX for citations
python scripts/abstract_skimmer.py \
    -q "cat:cs.LG AND ti:reinforcement" \
    -m 100 \
    --bibtex rl_papers.bib

# Papers from last week with summary
python scripts/abstract_skimmer.py \
    -c q-bio.QM \
    --days-back 7 \
    --summary
```

## Common Workflows

### Workflow 1: Daily Abstract Skimming

Stay current with recent papers in your field.

```python
from scripts.arxiv_client import ArxivClient

client = ArxivClient()

# Get today's papers
recent = client.get_recent(
    category="cs.LG",
    days_back=1,
    max_results=50
)

# Quick scan
for paper in recent:
    print(f"\n📄 {paper['title']}")
    print(f"   {paper['abstract'][:200]}...")
    print(f"   → {paper['arxiv_url']}")
```

**Command-line:**
```bash
python scripts/abstract_skimmer.py -c cs.LG --days-back 1 --format abstract
```

### Workflow 2: Literature Search

Find relevant papers for a research topic.

```python
# Comprehensive search
results = client.paginate_all(
    query="(ti:transformer OR ti:attention) AND abs:efficient",
    max_results=200
)

# Filter by relevance
keywords = ['efficient', 'scalable', 'optimization']
relevant = [
    p for p in results
    if any(kw in p['abstract'].lower() for kw in keywords)
]

# Export for reading
client.export_json(relevant, 'efficient_transformers.json')
client.export_bibtex(relevant, 'efficient_transformers.bib')

print(f"Found {len(relevant)} relevant papers out of {len(results)}")
```

### Workflow 3: Author Tracking

Monitor publications from key researchers.

```python
# Track multiple authors
authors = ["Vaswani", "Devlin", "Brown", "Radford"]
all_papers = []

for author in authors:
    papers = client.search_by_author(author, max_results=20)
    all_papers.extend(papers)

# Sort by date
all_papers.sort(
    key=lambda x: x.get('published_datetime', ''),
    reverse=True
)

# Show recent work
print("Recent papers from tracked authors:\n")
for paper in all_papers[:10]:
    print(f"[{paper['published']}] {paper['title']}")
    print(f"  Authors: {', '.join(paper['authors'][:3])}")
    print(f"  → {paper['arxiv_url']}\n")
```

### Workflow 4: Category Monitoring

Track multiple related categories.

```bash
# Machine Learning ecosystem
for cat in cs.LG cs.AI cs.CV cs.CL stat.ML; do
    echo "=== $cat ==="
    python scripts/abstract_skimmer.py -c $cat --days-back 7 -m 10 --format oneline
    echo ""
done
```

### Workflow 5: Export for Reference Manager

Build a bibliography for a project.

```python
# Search for your topic
results = client.search(
    query="cat:cs.LG AND (ti:optimization OR abs:gradient)",
    max_results=100
)

# Filter manually if needed
selected = [p for p in results if 'Adam' in p['abstract']]

# Export to BibTeX for Zotero/Mendeley/EndNote
client.export_bibtex(selected, 'optimization_refs.bib')

print(f"Exported {len(selected)} papers to BibTeX")
```

## ArXiv Categories

### Computer Science
| Category | Description |
|----------|-------------|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation and Language (NLP) |
| `cs.CV` | Computer Vision |
| `cs.LG` | Machine Learning |
| `cs.NE` | Neural and Evolutionary Computing |
| `cs.RO` | Robotics |
| `cs.CR` | Cryptography and Security |
| `cs.DS` | Data Structures and Algorithms |

### Quantitative Biology
| Category | Description |
|----------|-------------|
| `q-bio.BM` | Biomolecules |
| `q-bio.GN` | Genomics |
| `q-bio.NC` | Neurons and Cognition |
| `q-bio.QM` | Quantitative Methods |

### Physics
| Category | Description |
|----------|-------------|
| `quant-ph` | Quantum Physics |
| `cond-mat` | Condensed Matter |
| `physics.bio-ph` | Biological Physics |
| `physics.comp-ph` | Computational Physics |

### Statistics
| Category | Description |
|----------|-------------|
| `stat.ML` | Machine Learning |
| `stat.AP` | Applications |
| `stat.TH` | Statistics Theory |

### Mathematics
| Category | Description |
|----------|-------------|
| `math.OC` | Optimization and Control |
| `math.NA` | Numerical Analysis |
| `math.ST` | Statistics Theory |

See `references/categories.md` for complete category list.

## API Reference

### ArxivClient Class

```python
class ArxivClient:
    def __init__(
        self,
        rate_limit_delay: float = 3.0,  # Seconds between requests
        cache_dir: str = None,           # Cache directory
        cache_ttl_hours: int = 24,       # Cache TTL
        max_retries: int = 3,            # Retry attempts
        timeout: int = 30                # Request timeout
    )
```

### Methods

| Method | Description |
|--------|-------------|
| `search(query, max_results, sort_by, sort_order, start)` | Search papers |
| `get_recent(category, query, max_results, days_back)` | Get recent papers |
| `get_paper(arxiv_id)` | Get single paper by ID |
| `get_papers(arxiv_ids)` | Get multiple papers (batch) |
| `search_by_author(author_name, max_results)` | Search by author |
| `search_by_title(title_query, max_results)` | Search by title |
| `search_by_abstract(abstract_query, max_results)` | Search by abstract |
| `paginate_all(query, max_results, page_size)` | Paginate all results |
| `export_json(papers, output_path)` | Export to JSON |
| `export_csv(papers, output_path)` | Export to CSV |
| `export_bibtex(papers, output_path)` | Export to BibTeX |
| `highlight_keywords(text, keywords)` | Highlight keywords |
| `to_bibtex(paper)` | Convert paper to BibTeX |

### Paper Dictionary Structure

```python
{
    'arxiv_id': '2301.12345v1',
    'base_id': '2301.12345',
    'title': 'Paper Title',
    'authors': ['Author One', 'Author Two'],
    'affiliations': ['MIT', 'Stanford'],
    'abstract': 'Full abstract text...',
    'published': '2023-01-15',
    'published_datetime': '2023-01-15T12:00:00+00:00',
    'updated': '2023-01-20',
    'updated_datetime': '2023-01-20T15:30:00+00:00',
    'primary_category': 'cs.LG',
    'categories': ['cs.LG', 'cs.AI', 'stat.ML'],
    'doi': '10.1234/example',  # If published
    'journal_ref': 'Nature 2023',  # If published
    'comment': '20 pages, 5 figures',
    'arxiv_url': 'https://arxiv.org/abs/2301.12345',
    'pdf_url': 'https://arxiv.org/pdf/2301.12345.pdf',
    'links': {'abstract': '...', 'pdf': '...'}
}
```

## Best Practices

### Efficient Searching

1. **Use field tags** for precise searches:
   ```python
   # ✅ Specific - faster and more accurate
   query = "ti:transformer AND abs:attention"
   
   # ❌ Too broad - slower and noisier
   query = "transformer attention"
   ```

2. **Filter by category** to reduce noise:
   ```python
   query = "cat:cs.LG AND ti:optimization"
   ```

3. **Use caching** for repeated queries:
   ```python
   client = ArxivClient(cache_dir="./cache")
   ```

### Abstract Skimming

1. **Set reasonable limits** - Don't try to read everything:
   ```python
   max_results = 50  # Manageable for skimming
   ```

2. **Use keyword highlighting** to focus attention:
   ```bash
   python scripts/abstract_skimmer.py -q "machine learning" -k neural deep
   ```

3. **Use one-line format** for quick scanning:
   ```bash
   python scripts/abstract_skimmer.py -c cs.LG --format oneline
   ```

### Rate Limiting

ArXiv recommends **3 seconds between requests**:

1. The client enforces this automatically
2. Don't bypass rate limiting
3. Use caching for repeated queries
4. Use batch operations when possible

### Error Handling

```python
try:
    results = client.search("quantum computing")
except Exception as e:
    print(f"Search failed: {e}")
    # Handle error appropriately
```

## Limitations

### Coverage
- Primarily quantitative fields (physics, math, CS, q-bio, stats)
- Not comprehensive for biology, medicine, or social sciences
- Use PubMed for biomedical, bioRxiv for biology preprints

### Search Limitations
- No full-text search (only title, abstract, authors, comments)
- Complex boolean queries can be tricky
- No citation-based relevance ranking

### API Limitations
- Rate limited (3 seconds between requests recommended)
- Large result sets require pagination
- Maximum 2000 results per query

## Testing

Verify the skill works correctly:

```bash
# Test basic search
python -c "
from scripts.arxiv_client import ArxivClient
client = ArxivClient()
results = client.search('machine learning', max_results=5)
print(f'✅ Found {len(results)} papers')
for p in results:
    print(f'  - {p[\"title\"][:60]}...')
"

# Test command-line tool
python scripts/abstract_skimmer.py -c cs.LG -m 5 --format oneline
```

## Reference Documentation

### references/api_reference.md
Complete ArXiv API documentation including query syntax, parameters, response formats, and error handling.

### references/categories.md
Comprehensive list of all ArXiv categories organized by field with descriptions.

### references/search_examples.md
Extensive collection of search query examples for common research tasks.

## Support Resources

- **ArXiv API Documentation**: https://arxiv.org/help/api/user-manual
- **ArXiv Categories**: https://arxiv.org/category_taxonomy
- **ArXiv Help**: https://arxiv.org/help
- **ArXiv Blog**: https://blogs.cornell.edu/arxiv/

## Related Skills

- **pubmed-database**: For biomedical literature
- **biorxiv-database**: For biology preprints
- **openalex-database**: For comprehensive scholarly search (240M+ works)
- **literature-review**: For systematic literature reviews
- **citation-management**: For managing citations and bibliographies
