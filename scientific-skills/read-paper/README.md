# Read-Paper Skill

Extract hyper-relevant findings from academic PDFs with killer precision.

## Overview

This skill helps you read academic papers and extract **only the most important findings** aligned with your research interests:

- Computational social science
- LLM agents and social simulation
- Network science, statistical physics, information theory
- Online communities (toxicity, trust, reputation)
- Open-source LLM capabilities

**Output**: Brief, citation-ready notes in chat—not lengthy documents.

**Philosophy**: Ruthless selectivity. Extract 3 killer findings instead of 20 mediocre ones.

---

## Quick Start

### 1. Install Dependencies

```bash
pip install 'markitdown[all]'
```

### 2. Convert PDF to Markdown

```bash
markitdown your_paper.pdf -o paper.md
```

### 3. Read and Extract

Use Claude with the `read-paper` skill to:
- Scan for relevant findings (7 types: mechanisms, metrics, benchmarks, etc.)
- Apply critical filters (novelty, specificity, utility)
- Output concise notes using provided templates

### 4. Get Brief Notes

Example output:
```markdown
**Memory Mechanism**: Entropy-driven controlled forgetting

- **Paper**: Zhang et al. (2024). DOI: 10.1234/example
- **Key insight**: Decay rate ∝ KL divergence. Low MI → faster forgetting.
- **Quantitative**: +32% fidelity (F1: 0.89 vs 0.67)
- **Use for**: Implement for LLM agent memory in simulations
```

---

## Documentation

- **`SKILL.md`** - Complete skill guide with workflow, finding types, templates
- **`QUICK_REFERENCE.md`** - One-page quick reference for rapid use
- **`references/research_focus_keywords.md`** - Comprehensive keyword lists for all 6 research areas
- **`assets/note_templates.md`** - 7 copy-paste templates for different finding types

---

## Scripts

### `batch_convert_pdfs.py`

Batch convert multiple PDFs to markdown:

```bash
# Convert all PDFs in directory
python scripts/batch_convert_pdfs.py papers/ -o markdown/

# Filter by keywords (skip irrelevant papers)
python scripts/batch_convert_pdfs.py papers/ -o markdown/ \
  --focus-keywords "LLM agents,toxicity,entropy"

# Dry run (see what would be converted)
python scripts/batch_convert_pdfs.py papers/ -o markdown/ --dry-run
```

---

## What Makes This Skill Different?

### Not a Literature Review Tool
- **Literature Review**: Systematic search, comprehensive synthesis, formal methodology
- **Read-Paper**: Precision extraction of killer findings for your specific research

### Not Citation Management
- **Citation Management**: BibTeX generation, bibliography formatting, metadata extraction
- **Read-Paper**: Extract research insights, methods, metrics—not just citations

### Not a Summary Generator
- **Summary**: Condense entire paper into abstract
- **Read-Paper**: Extract 3-5 actionable findings that advance YOUR research

### Ruthlessly Focused

Only extract findings that match:
- ✅ One of your 6 research areas
- ✅ One of 7 high-value finding types
- ✅ Novelty + specificity + citability + utility

Everything else is **skipped**.

---

## Research Focus Areas

1. **Toxic language and hate speech** on online platforms
2. **Realistic simulation** of social media via LLM agents
3. **Network science, statistical physics, info theory** for online communities
4. **Open-source LLM capabilities** for social simulation
5. **Quantifying trust and reputation** in online communities
6. **Niche communities** (StackExchange, Reddit Q&A)

---

## High-Value Finding Types

1. **Novel mechanisms**: Memory systems, controlled forgetting, belief updating
2. **Quantitative measures**: Entropy, mutual information, network metrics
3. **Interdisciplinary bridges**: Info theory ↔ social science, physics ↔ communities
4. **Benchmarks & critical values**: LLM performance, phase transitions, thresholds
5. **Citable arguments**: Well-crafted theoretical frameworks
6. **Novel use cases**: Unexpected applications of methods
7. **Open-source LLM evidence**: Model performance data

---

## Example Workflow

```bash
# 1. Batch convert papers
python scripts/batch_convert_pdfs.py papers/ -o markdown/ \
  --focus-keywords "social simulation,LLM,entropy"

# 2. Read first paper
# → Scan for novel memory mechanisms, LLM benchmarks
# → Extract 2-3 killer findings
# → Output concise notes

# 3. Continue with remaining papers
# → Build curated knowledge base of high-signal findings
```

---

## Integration with Other Skills

- **`markitdown`**: PDF → Markdown conversion
- **`scientific-critical-thinking`**: Methodology evaluation, bias detection
- **`literature-review`**: Systematic multi-paper synthesis
- **`citation-management`**: BibTeX generation for extracted findings

---

## Best Practices

1. **Quality over quantity**: Extract 3 killer findings > 20 mediocre ones
2. **Specificity**: Capture numbers, formulas, model names—no vague descriptions
3. **Action-oriented**: Always include "Use for" with concrete application
4. **Standalone notes**: Each note independently useful months later
5. **Critical reading**: Apply scientific-critical-thinking filters

---

## Dependencies

### Required
```bash
pip install 'markitdown[all]'
```

### Optional (for complex PDFs)
```bash
pip install 'markitdown[az-doc-intel]'
```

---

## License

Part of [Claude Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills)
MIT License - see repository root for details

---

## Quick Links

- [Main Skill Guide](SKILL.md) - Complete documentation
- [Quick Reference](QUICK_REFERENCE.md) - One-page cheat sheet
- [Keywords](references/research_focus_keywords.md) - All research area keywords
- [Templates](assets/note_templates.md) - 7 note templates with examples

---

**Remember**: Be surgically selective. Extract only what advances your research. Capture killer findings with precision.
