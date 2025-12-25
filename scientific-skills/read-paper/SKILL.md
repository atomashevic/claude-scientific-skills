---
name: read-paper
description: "Extract hyper-relevant findings from academic PDFs with killer precision. Focused on computational social science, LLM agents, online communities, network science, information theory, and statistical physics. Outputs brief, citable notes on novel methods, measures, benchmarks, and use cases."
allowed-tools: [Read, Write, Edit, Bash]
---

# Read Paper - Precision Research Note Extraction

## Overview

Extract highly relevant findings from academic papers with surgical precision. This skill reads PDFs, identifies breakthrough findings aligned with your research interests, and outputs brief, citation-ready notes.

**Philosophy**: Be ruthlessly selective. Extract only killer findings that advance your research—novel methods, quantitative measures, critical benchmarks, elegant arguments, and unexpected use cases.

**Output**: Concise notes in chat, not documents. Each note is a standalone insight ready for brainstorming or citation.

## When to Use This Skill

Use this skill when:
- Reading academic PDFs to find actionable insights
- Building a research knowledge base from papers
- Identifying citable claims and quantitative results
- Extracting novel methods for LLM agents, social simulations, or online communities
- Finding benchmarks, critical values, or performance metrics
- Discovering interdisciplinary bridges (information theory ↔ social science)
- Seeking well-crafted arguments for citations

**Don't use** for:
- Comprehensive literature reviews (use `literature-review` skill)
- Managing citations bibliographically (use `citation-management` skill)
- Full paper summaries or systematic reviews

---

## Research Focus Areas

This skill is optimized to detect findings in these domains:

### Primary Research Areas

1. **Toxic language and hate-speech on online social platforms**
   - Detection methods, toxicity metrics, content moderation
   - Psychological mechanisms, community dynamics
   - Platform-specific patterns, cross-platform comparisons

2. **Realistic simulation of online social media spaces via LLM agents**
   - Agent architectures, memory mechanisms, behavioral fidelity
   - Multi-agent systems, emergent phenomena
   - Validation metrics, realism benchmarks

3. **Network science, statistical physics, information theory for online communities**
   - Network evolution models, phase transitions, criticality
   - Information-theoretic measures, entropy, mutual information
   - Statistical mechanics of social systems

4. **Open source LLMs and their capability for social simulations**
   - Model performance on social tasks, benchmarks
   - Prompt engineering, fine-tuning for social understanding
   - Model comparisons, capability analyses

5. **Quantifying trust and reputation in online communities**
   - Reputation metrics, trust propagation models
   - Information-theoretic approaches to reputation
   - Empirical validation, behavioral correlates

6. **Niche online communities (StackExchange, Reddit QA)**
   - Community structure, expertise networks
   - Content quality, moderation patterns
   - Comparative analyses across platforms

### High-Value Finding Types

Extract findings that match these categories:

1. **Novel Mechanisms**
   - Memory systems for LLM agents (especially controlled forgetting)
   - Attention mechanisms for social context
   - Belief updating, learning algorithms
   - Trust propagation, reputation dynamics

2. **Quantitative Measures**
   - Information-theoretic metrics (entropy, KL divergence, mutual information)
   - Network metrics (centrality, clustering, modularity)
   - Reputation scores, trust indices
   - Toxicity measures, sentiment metrics

3. **Interdisciplinary Bridges**
   - Information theory → computational social science
   - Statistical physics → online communities
   - Network science → LLM agent design
   - Cognitive science → agent memory

4. **Benchmarks & Critical Values**
   - LLM performance on social simulation tasks
   - Thresholds, phase transitions, critical points
   - Comparative baselines, state-of-the-art results
   - Validation metrics, evaluation frameworks

5. **Citable Arguments**
   - Theoretical frameworks elegantly stated
   - Well-supported claims with strong evidence
   - Definitional clarity, conceptual insights
   - Methodological justifications

6. **Novel Use Cases**
   - Unexpected applications of methods or models
   - Transfer learning across domains
   - Creative combinations of techniques
   - Proof-of-concept demonstrations

7. **Open-Source LLM Evidence**
   - Performance data for specific models
   - Task-specific capabilities
   - Comparisons with proprietary models
   - Fine-tuning or prompting strategies

---

## Core Workflow

### Step 1: Convert PDF to Markdown

Use `markitdown` to extract text from the PDF:

```bash
# Convert PDF to markdown
markitdown paper.pdf -o paper.md
```

**Note**: If the PDF is image-heavy or has complex formatting, consider using Azure Document Intelligence:

```bash
markitdown paper.pdf -o paper.md -d -e "<azure_endpoint>"
```

### Step 2: Critical Reading with Focus

Read the markdown systematically with a critical eye:

1. **Scan for relevance signals**:
   - Keywords: LLM agents, social simulation, online communities, toxicity, reputation, trust, hate speech, information theory, statistical physics, network science
   - Model names: Open-source LLMs (Llama, Mistral, Qwen, etc.)
   - Methods: Memory mechanisms, agent architectures, entropy measures, network metrics
   - Results sections with quantitative findings

2. **Apply critical filters**:
   - Is the method/measure **novel** or a **significant improvement**?
   - Are benchmarks/metrics **quantitative and reusable**?
   - Is the finding **actionable** for your research?
   - Is the argument **citation-worthy** (clear, well-supported)?
   - Does it **bridge disciplines** in an interesting way?

3. **Extract with precision**:
   - Note the exact claim, method, or result
   - Capture quantitative details (numbers, metrics, comparisons)
   - Record where it appears (section, table, figure)
   - Include citation information (authors, year, title, DOI)

### Step 3: Output Brief Notes

For each finding, output a concise note in this format:

```
**[Finding Type]**: [One-sentence description]
- **Paper**: Authors (Year). Title. DOI: [doi]
- **Key insight**: [2-3 sentence explanation with specifics]
- **Quantitative**: [Numbers, metrics, benchmarks if applicable]
- **Use for**: [How it applies to your research]
```

**Example output**:

```
**Novel Memory Mechanism**: Controlled forgetting via information-theoretic decay

- **Paper**: Smith et al. (2024). "Entropy-Driven Memory Decay in LLM Agents for Social Simulation." DOI: 10.1234/example
- **Key insight**: Introduces memory decay mechanism based on information entropy. Memories with low mutual information with current context decay faster. Enables agents to forget irrelevant details while retaining contextually important information.
- **Quantitative**: Tested on 5 agent architectures; 32% improvement in behavioral fidelity (F1=0.89 vs 0.67 baseline). Entropy threshold τ=0.3 optimal for social tasks.
- **Use for**: Implement in LLM agent memory for realistic forgetting in social simulations.
```

---

## Precision Extraction Guide

### What to Extract

**YES - Extract these**:
- ✅ Novel methods with clear implementation details
- ✅ Quantitative metrics with reported values
- ✅ Benchmarks with model names and scores
- ✅ Information-theoretic measures (formulas + interpretations)
- ✅ Phase transitions, critical values, thresholds
- ✅ Well-crafted theoretical arguments ready for citation
- ✅ Open-source LLM performance data
- ✅ Interdisciplinary bridges between your focus areas
- ✅ Unexpected use cases of familiar methods

**NO - Skip these**:
- ❌ Standard background/introduction material
- ❌ Generic related work summaries
- ❌ Vague claims without supporting data
- ❌ Methods without novelty (standard practices)
- ❌ Results without quantitative details
- ❌ Speculative future work without substance
- ❌ Findings outside your 6 research areas

### Critical Reading Checklist

Before extracting a finding, verify:

1. **Relevance**: Does it directly relate to one of your 6 research areas?
2. **Novelty**: Is it new, improved, or an interesting application?
3. **Specificity**: Can you extract actionable details (numbers, formulas, methods)?
4. **Citability**: Is the claim well-supported and clearly stated?
5. **Utility**: Could you use this in your own research (implementation, citation, comparison)?

If all 5 answers are "yes", extract the finding. Otherwise, skip.

---

## Finding Type Templates

Use these templates for different finding types:

### 1. Novel Method/Mechanism

```
**[Method Type]**: [Brief name]

- **Paper**: [Citation]
- **Key insight**: [How it works, what's novel]
- **Quantitative**: [Performance metrics, comparisons]
- **Implementation**: [Key technical details]
- **Use for**: [Your application]
```

### 2. Quantitative Measure

```
**[Measure Type]**: [Measure name]

- **Paper**: [Citation]
- **Definition**: [Formula or precise definition]
- **Interpretation**: [What it captures, why useful]
- **Validation**: [Empirical results, correlations]
- **Use for**: [Your application]
```

### 3. Benchmark/Critical Value

```
**Benchmark**: [Task/dataset name]

- **Paper**: [Citation]
- **Task**: [What is being measured]
- **Results**: [Model performances, baselines]
- **Critical values**: [Thresholds, phase transitions]
- **Use for**: [Your application]
```

### 4. Citable Argument

```
**Citable Claim**: [Topic]

- **Paper**: [Citation]
- **Argument**: [Well-crafted claim/framework]
- **Evidence**: [Supporting data]
- **Citation context**: [When to cite this]
```

### 5. Interdisciplinary Bridge

```
**Bridge**: [Domain A] → [Domain B]

- **Paper**: [Citation]
- **Connection**: [How domains are linked]
- **Formalism**: [Mathematical/conceptual framework]
- **Implications**: [What this enables]
- **Use for**: [Your application]
```

### 6. Open-Source LLM Performance

```
**LLM Performance**: [Model name] on [Task]

- **Paper**: [Citation]
- **Model**: [Specific model and size]
- **Task**: [Benchmark/evaluation]
- **Results**: [Scores, comparisons]
- **Notes**: [Prompting, fine-tuning details]
- **Use for**: [Your application]
```

---

## Example Session

**Input**: PDF of "Agent Memory Systems for Realistic Social Simulation"

**Process**:
1. Convert PDF: `markitdown paper.pdf -o paper.md`
2. Read markdown, scanning for memory mechanisms, LLM agents, social simulation
3. Critical filter: Is the memory mechanism novel? Yes—uses information theory for controlled forgetting
4. Extract details: Section 3.2, equation 5, Table 2 results
5. Output concise note

**Output**:
```
**Novel Memory Mechanism**: Information-theoretic controlled forgetting for LLM agents

- **Paper**: Chen et al. (2024). "Entropy-Based Memory Decay in Multi-Agent Social Simulations." Nature Machine Intelligence. DOI: 10.1038/s41234-024-01234-5
- **Key insight**: Memory decay rate proportional to KL divergence between memory embedding and current context. Implements selective forgetting—contextually irrelevant memories fade faster. Mathematically grounded in information theory (mutual information < threshold → decay).
- **Quantitative**: Tested on 3 social simulation tasks (debate, collaboration, conflict). Behavioral fidelity improved 28-35% (Cohen's d = 1.2) vs. baseline LRU cache. Optimal KL threshold = 0.4 bits for Llama-3-70B.
- **Implementation**: Eq. 5 (section 3.2): decay_rate = α · KL(mem_emb || context_emb). Requires embedding layer access. Code: github.com/example/entropy-memory
- **Use for**: Implement for realistic LLM agent forgetting in online community simulations. Compare with recency-based decay.

**Interdisciplinary Bridge**: Information theory → Agent memory design

- **Paper**: Chen et al. (2024). [same as above]
- **Connection**: Applies Shannon entropy and KL divergence to model human-like memory decay in artificial agents
- **Formalism**: Memory importance I(m) = -Σ p(m|c) log p(m|c), where c is context. Low I(m) → high decay rate.
- **Implications**: Provides principled, quantitative basis for memory management vs. ad-hoc heuristics
- **Use for**: Cite when justifying information-theoretic approaches to agent design

**LLM Performance**: Llama-3-70B on social role-playing fidelity

- **Paper**: Chen et al. (2024). [same as above]
- **Model**: Llama-3-70B-Instruct with entropy-based memory
- **Task**: Multi-turn social role-playing (debate, negotiation, collaboration)
- **Results**: Behavioral fidelity F1 = 0.89 (vs 0.67 baseline), human evaluation agreement 83%
- **Notes**: Requires 8K context window, 4-bit quantization viable with <5% performance drop
- **Use for**: Baseline for LLM agent social simulation experiments
```

---

## Best Practices

### Ruthless Selectivity

1. **Quality over quantity**: Extract 3 killer findings > 20 mediocre ones
2. **Action-oriented**: Ask "Can I implement this?" or "Will I cite this?"
3. **Specificity**: Capture numbers, formulas, model names—no vague descriptions
4. **Your research only**: If it doesn't align with your 6 focus areas, skip it

### Precision Notes

1. **One finding, one note**: Don't combine multiple insights
2. **Standalone**: Each note should be independently useful
3. **Citable**: Include full citation info (authors, year, title, DOI)
4. **Quantitative**: Always include numbers when available
5. **Contextual**: Note where to find details (section, equation, table, figure)

### Critical Reading

1. **Apply scientific-critical-thinking**: Evaluate methodology, biases, validity
2. **Question novelty**: Is this really new, or incremental?
3. **Check support**: Are claims backed by strong evidence?
4. **Assess generalizability**: Does it apply beyond the specific study context?
5. **Note limitations**: Flag important caveats for future use

### Efficient Workflow

1. **Scan first**: Read abstract, conclusions, figures before deep reading
2. **Navigate to sections**: Jump to Methods, Results for details
3. **Use grep**: Search markdown for keywords if paper is long
4. **Batch process**: Convert multiple PDFs, then read all markdowns
5. **Template reuse**: Copy-paste finding templates for consistency

---

## Integration with Other Skills

### Complementary Skills

**This skill (`read-paper`)** → Precision extraction of killer findings
**`literature-review`** → Systematic multi-paper synthesis
**`citation-management`** → Bibliography management, BibTeX generation
**`scientific-critical-thinking`** → Methodology evaluation, bias detection
**`markitdown`** → PDF to markdown conversion

### Combined Workflows

**Workflow 1: Deep dive on a specific paper**
```bash
# 1. Convert PDF
markitdown paper.pdf -o paper.md

# 2. Use read-paper skill to extract findings
# → Outputs 3-5 concise notes in chat

# 3. Use citation-management to get BibTeX
python scripts/doi_to_bibtex.py 10.1234/example >> references.bib
```

**Workflow 2: Survey a topic**
```bash
# 1. Use literature-review to find papers systematically
# 2. Convert all PDFs to markdown
for pdf in papers/*.pdf; do
  markitdown "$pdf" -o "markdown/$(basename $pdf .pdf).md"
done

# 3. Use read-paper on each markdown
# → Extract killer findings across all papers

# 4. Use citation-management to build bibliography
```

**Workflow 3: Evaluate a method's validity**
```bash
# 1. Use read-paper to extract the method
# 2. Use scientific-critical-thinking to evaluate:
#    - Methodology rigor
#    - Statistical validity
#    - Potential biases
#    - Generalizability
# → Decide: trust and use, or flag concerns
```

---

## Scripts

### `extract_findings.py`

Automated finding extraction helper (work in progress):

```bash
# Extract findings from markdown
python scripts/extract_findings.py paper.md \
  --focus "LLM agents, social simulation" \
  --output findings.json
```

**Features**:
- Keyword-based section identification
- Pattern matching for metrics (numbers, percentages, p-values)
- Citation extraction
- JSON output for downstream processing

**Status**: Experimental—manual extraction still recommended for precision

### `batch_process.py`

Convert and process multiple papers:

```bash
# Process directory of PDFs
python scripts/batch_process.py papers/ \
  --output-dir markdown/ \
  --extract-findings \
  --focus-areas "social simulation, network science"
```

---

## Quick Reference

### Research Area Keywords

**Area 1 (Toxic language)**: toxicity, hate speech, content moderation, offensive language, harassment, trolling, abusive language

**Area 2 (Social simulation)**: LLM agents, multi-agent simulation, agent-based modeling, social behavior, emergent phenomena, behavioral fidelity

**Area 3 (Network science + physics)**: network evolution, phase transitions, entropy, statistical mechanics, information theory, complex systems, criticality

**Area 4 (Open-source LLMs)**: Llama, Mistral, Qwen, Phi, open models, benchmarks, capabilities, fine-tuning, prompt engineering

**Area 5 (Trust/reputation)**: reputation systems, trust metrics, credibility, social capital, network trust, information-theoretic reputation

**Area 6 (Niche communities)**: StackExchange, Reddit, Q&A platforms, community structure, moderation, expertise networks

### Common Metrics to Extract

**Information theory**: entropy, mutual information, KL divergence, transfer entropy, information gain

**Network science**: degree centrality, betweenness, clustering coefficient, modularity, assortativity

**LLM performance**: perplexity, BLEU, ROUGE, F1, accuracy, human evaluation agreement

**Social metrics**: engagement rate, toxicity score, sentiment, controversy, virality

**Statistical**: effect size (Cohen's d, η²), p-values, confidence intervals, correlation coefficients

---

## Dependencies

### Required

```bash
# MarkItDown for PDF conversion
pip install 'markitdown[all]'
```

### Optional

```bash
# For Azure Document Intelligence (complex PDFs)
pip install 'markitdown[az-doc-intel]'

# For automated extraction (experimental)
pip install pandas numpy scikit-learn
```

---

## Summary

The `read-paper` skill provides:

1. **Precision extraction** of hyper-relevant findings from academic PDFs
2. **Focused filters** aligned with your 6 research areas and 7 finding types
3. **Brief, citable notes** ready for brainstorming and reference
4. **Critical reading** informed by scientific-critical-thinking principles
5. **Integration** with markitdown, literature-review, and citation-management skills
6. **Efficiency** for building a curated research knowledge base

**Philosophy**: Extract only what advances your research. Be ruthlessly selective. Capture killer findings with surgical precision.

**Output format**: Concise notes in chat, not lengthy documents. Each note is a standalone insight.

Use this skill to build a high-signal research knowledge base—novel methods, quantitative measures, interdisciplinary bridges, and citable arguments that directly advance your work on LLM agents, online communities, and computational social science.
