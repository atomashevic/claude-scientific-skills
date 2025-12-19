# ArXiv API Reference

Complete technical reference for the ArXiv API.

## Base URL

```
http://export.arxiv.org/api/query
```

## Authentication

No authentication required. ArXiv API is completely open.

## Rate Limiting

**Recommended:** 1 request per 3 seconds

ArXiv doesn't enforce strict rate limits but requests responsible use:
- Wait 3+ seconds between requests
- Implement exponential backoff for retries
- Cache results locally when possible
- Use batch operations for multiple papers

## Query Parameters

### search_query

The search query string supporting field tags and boolean operators.

**Field Tags:**

| Tag | Field | Description |
|-----|-------|-------------|
| `ti:` | Title | Paper title |
| `au:` | Author | Author name |
| `abs:` | Abstract | Abstract text |
| `co:` | Comment | Author comments |
| `cat:` | Category | ArXiv category |
| `all:` | All | All fields |

**Boolean Operators:**

| Operator | Description | Example |
|----------|-------------|---------|
| `AND` | Both conditions | `ti:quantum AND abs:computing` |
| `OR` | Either condition | `cat:cs.LG OR cat:cs.AI` |
| `ANDNOT` | First without second | `cat:cs.LG ANDNOT ti:survey` |

**Phrase Matching:**

```
ti:"attention is all you need"
abs:"deep reinforcement learning"
```

**Grouping:**

```
(ti:quantum OR ti:classical) AND abs:computing
cat:cs.LG AND (ti:efficient OR abs:fast)
```

**Examples:**

```
# Simple keyword search
machine learning

# Title search
ti:transformer

# Author search
au:Vaswani

# Category + keyword
cat:cs.LG AND ti:optimization

# Complex query
(cat:cs.LG OR cat:stat.ML) AND (ti:efficient OR abs:scalable) ANDNOT ti:survey

# Exact phrase in title
ti:"large language model"
```

### id_list

Comma-separated list of ArXiv IDs for direct retrieval.

**Formats:**
- New format: `2301.12345` or `2301.12345v1`
- Old format: `hep-th/9901001`

**Examples:**

```
# Single paper
id_list=2301.12345

# Multiple papers
id_list=2301.12345,2302.23456,2303.34567

# With version
id_list=2301.12345v1

# Old format
id_list=quant-ph/0001001
```

### start

Starting index for pagination (0-based).

**Examples:**

```
start=0     # First page (default)
start=100   # Second page (if max_results=100)
start=200   # Third page
```

### max_results

Maximum number of results to return.

- **Default:** 10
- **Maximum:** 2000 (per request)

**Examples:**

```
max_results=50
max_results=200
max_results=2000  # Maximum
```

### sortBy

Sort field for results.

| Value | Description |
|-------|-------------|
| `relevance` | Relevance ranking (default for search) |
| `lastUpdatedDate` | Last update date |
| `submittedDate` | Original submission date |

### sortOrder

Sort direction.

| Value | Description |
|-------|-------------|
| `descending` | Newest/most relevant first (default) |
| `ascending` | Oldest/least relevant first |

## Response Format

The API returns Atom XML format.

### Namespaces

```xml
xmlns:atom="http://www.w3.org/2005/Atom"
xmlns:arxiv="http://arxiv.org/schemas/atom"
xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
```

### Feed Structure

```xml
<feed>
  <opensearch:totalResults>42</opensearch:totalResults>
  <opensearch:startIndex>0</opensearch:startIndex>
  <opensearch:itemsPerPage>10</opensearch:itemsPerPage>
  
  <entry>...</entry>
  <entry>...</entry>
</feed>
```

### Entry Structure

```xml
<entry>
  <id>http://arxiv.org/abs/2301.12345v1</id>
  <updated>2023-01-20T15:30:00Z</updated>
  <published>2023-01-15T12:00:00Z</published>
  
  <title>Paper Title Here</title>
  
  <summary>Full abstract text here...</summary>
  
  <author>
    <name>Author Name</name>
    <arxiv:affiliation>Institution</arxiv:affiliation>
  </author>
  
  <arxiv:primary_category term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
  <category term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
  <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>
  
  <link href="http://arxiv.org/abs/2301.12345v1" rel="alternate" type="text/html"/>
  <link href="http://arxiv.org/pdf/2301.12345v1" rel="related" type="application/pdf"/>
  
  <arxiv:doi>10.1234/example</arxiv:doi>
  <arxiv:journal_ref>Nature 2023</arxiv:journal_ref>
  <arxiv:comment>20 pages, 5 figures</arxiv:comment>
</entry>
```

### Field Mappings

| XML Element | Python Field | Description |
|------------|--------------|-------------|
| `atom:id` | `arxiv_id` | ArXiv identifier with version |
| `atom:title` | `title` | Paper title |
| `atom:summary` | `abstract` | Abstract text |
| `atom:published` | `published` | Original submission date |
| `atom:updated` | `updated` | Last update date |
| `atom:author/atom:name` | `authors` | List of author names |
| `atom:author/arxiv:affiliation` | `affiliations` | Author affiliations |
| `arxiv:primary_category[@term]` | `primary_category` | Primary category |
| `atom:category[@term]` | `categories` | All categories |
| `arxiv:doi` | `doi` | DOI (if published) |
| `arxiv:journal_ref` | `journal_ref` | Journal reference |
| `arxiv:comment` | `comment` | Author comments |

## Error Handling

### Empty Results

No papers matching query:
```xml
<feed>
  <opensearch:totalResults>0</opensearch:totalResults>
  <opensearch:startIndex>0</opensearch:startIndex>
  <opensearch:itemsPerPage>0</opensearch:itemsPerPage>
</feed>
```

### Invalid Query

Error message in entry title:
```xml
<entry>
  <title>Error: query syntax error</title>
</entry>
```

### HTTP Status Codes

| Code | Description | Action |
|------|-------------|--------|
| 200 | Success | Parse response |
| 400 | Bad request | Check query syntax |
| 500+ | Server error | Retry with backoff |

### Retry Strategy

```python
def make_request_with_retry(url, params, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 200:
                return response
            elif response.status_code >= 500:
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
        except requests.exceptions.Timeout:
            wait_time = 2 ** attempt
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
```

## Pagination

For large result sets, use pagination:

```python
start = 0
page_size = 100
all_papers = []

while True:
    params = {
        'search_query': query,
        'start': start,
        'max_results': page_size,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    papers = fetch_papers(params)
    
    if not papers:
        break
    
    all_papers.extend(papers)
    
    if len(papers) < page_size:
        break
    
    start += page_size
    time.sleep(3)  # Rate limiting
```

## Batch Operations

Retrieve multiple papers efficiently:

```
id_list=2301.12345,2302.23456,2303.34567,2304.45678
max_results=4
```

**Note:** Batch queries are more efficient than individual requests but are still subject to rate limiting.

## Complete Examples

### Basic Search Request

```
GET http://export.arxiv.org/api/query?
    search_query=machine+learning&
    max_results=10&
    sortBy=relevance&
    sortOrder=descending
```

### Category Search

```
GET http://export.arxiv.org/api/query?
    search_query=cat:cs.LG&
    max_results=50&
    sortBy=submittedDate&
    sortOrder=descending
```

### Complex Query

```
GET http://export.arxiv.org/api/query?
    search_query=(cat:cs.LG+OR+cat:cs.AI)+AND+ti:transformer&
    max_results=100&
    sortBy=submittedDate&
    sortOrder=descending
```

### Paper Lookup

```
GET http://export.arxiv.org/api/query?
    id_list=2301.12345&
    max_results=1
```

### Paginated Results

```
# First page
GET http://export.arxiv.org/api/query?
    search_query=cat:cs.LG&
    start=0&
    max_results=100

# Second page
GET http://export.arxiv.org/api/query?
    search_query=cat:cs.LG&
    start=100&
    max_results=100
```

## Python Implementation

```python
import requests
import xml.etree.ElementTree as ET
import time

BASE_URL = "http://export.arxiv.org/api/query"
NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom'
}

def search_arxiv(query, max_results=10):
    params = {
        'search_query': query,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    
    root = ET.fromstring(response.content)
    entries = root.findall('atom:entry', NS)
    
    papers = []
    for entry in entries:
        title = entry.find('atom:title', NS).text.strip()
        abstract = entry.find('atom:summary', NS).text.strip()
        authors = [a.find('atom:name', NS).text 
                   for a in entry.findall('atom:author', NS)]
        
        papers.append({
            'title': title,
            'abstract': abstract,
            'authors': authors
        })
    
    return papers

# Usage
time.sleep(3)  # Rate limit
papers = search_arxiv("machine learning", max_results=5)
for p in papers:
    print(p['title'])
```

## Best Practices

1. **Rate Limiting:** Wait 3+ seconds between requests
2. **Caching:** Store results locally to avoid repeated queries
3. **Batch Requests:** Use id_list for multiple papers
4. **Error Handling:** Implement exponential backoff
5. **Pagination:** Use for large result sets
6. **Field Tags:** Use specific fields for better results
7. **Timeouts:** Set appropriate request timeouts

## Additional Resources

- **Official Documentation:** https://arxiv.org/help/api/user-manual
- **Category Taxonomy:** https://arxiv.org/category_taxonomy
- **ArXiv Help:** https://arxiv.org/help
- **API Terms of Use:** https://arxiv.org/help/api/tou
