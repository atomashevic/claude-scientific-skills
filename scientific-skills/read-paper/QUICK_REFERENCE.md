# Read-Paper Skill - Quick Reference

One-page guide for rapid paper reading and note extraction.

---

## 🎯 Purpose

Extract **killer findings** from PDFs with surgical precision. Output: brief, citable notes in chat.

---

## 📋 Quick Workflow

```bash
# 1. Convert PDF to markdown
markitdown paper.pdf -o paper.md

# 2. Read and extract (manual, focused)
# Scan for: novel methods, metrics, benchmarks, LLM performance

# 3. Output concise notes using templates (see assets/note_templates.md)
```

---

## 🔍 What to Extract (7 Types)

1. **Novel mechanisms**: Memory systems, forgetting, attention, belief updating
2. **Quantitative measures**: Entropy, MI, KL divergence, network metrics
3. **Interdisciplinary bridges**: Info theory ↔ social science, physics ↔ communities
4. **Benchmarks**: LLM performance, critical values, thresholds
5. **Citable arguments**: Well-supported theoretical claims
6. **Novel use cases**: Unexpected applications of methods
7. **Open-source LLM data**: Model performance on social/agent tasks

---

## 🎓 Research Areas (Filter by These)

1. Toxic language / hate speech
2. LLM agents for social simulation
3. Network science + statistical physics + info theory for online communities
4. Open-source LLM capabilities
5. Trust and reputation quantification
6. Niche communities (StackExchange, Reddit QA)

---

## ✅ Extract / ❌ Skip

**Extract**:
- ✅ Novel method with implementation details
- ✅ Quantitative metrics with reported values
- ✅ Equations, algorithms, formulas
- ✅ Model names + benchmark scores
- ✅ Phase transitions, critical values
- ✅ Well-crafted arguments ready for citation

**Skip**:
- ❌ Standard background material
- ❌ Vague claims without data
- ❌ Generic related work summaries
- ❌ Results without numbers
- ❌ Content outside your 6 research areas

---

## 📝 Note Template (Copy-Paste)

```markdown
**[Finding Type]**: [One-line description]

- **Paper**: Authors (Year). Title. DOI: [doi]
- **Key insight**: [2-3 sentences with specifics]
- **Quantitative**: [Numbers, metrics, comparisons]
- **Use for**: [Your application]
```

See `assets/note_templates.md` for 7 specialized templates.

---

## 🔎 Keyword Scanning

Use these to quickly assess relevance:

**Area 1 (Toxicity)**: toxicity, hate speech, content moderation, Perspective API

**Area 2 (Agents)**: LLM agent, multi-agent simulation, memory mechanism, behavioral fidelity

**Area 3 (Network+Physics+Info)**: entropy, mutual information, KL divergence, phase transition, network evolution

**Area 4 (Open LLMs)**: Llama, Mistral, Qwen, benchmark, performance comparison

**Area 5 (Trust)**: reputation, trust metric, credibility, trust propagation

**Area 6 (Communities)**: StackExchange, Reddit, Q&A, expert networks, moderation

Full keyword list: `references/research_focus_keywords.md`

---

## 🔧 Grep Tricks (Search Markdown)

```bash
# Find equations
grep -E "\$\$|\\begin\{equation\}" paper.md

# Find performance metrics
grep -iE "(f1|accuracy|precision|auc|entropy)" paper.md

# Find model names
grep -iE "(llama|mistral|qwen)" paper.md

# Find novelty claims
grep -iE "(novel|new|first|introduce)" paper.md

# Find statistical tests
grep -iE "(p\s*<\s*0\.|cohen|effect size)" paper.md
```

---

## 🚀 Batch Processing

```bash
# Convert multiple PDFs
python scripts/batch_convert_pdfs.py papers/ -o markdown/

# Filter by keywords
python scripts/batch_convert_pdfs.py papers/ -o markdown/ \
  --focus-keywords "LLM agents,toxicity,entropy"
```

---

## 🎯 Critical Filters

Before extracting, verify **all 5**:

1. **Relevance**: Relates to one of your 6 research areas?
2. **Novelty**: New, improved, or interesting application?
3. **Specificity**: Actionable details (numbers, formulas)?
4. **Citability**: Well-supported and clearly stated?
5. **Utility**: Could you use this in your research?

If all 5 → **extract**. Otherwise → **skip**.

---

## 💡 Example Output

```markdown
**Memory Mechanism**: Entropy-driven controlled forgetting

- **Paper**: Zhang et al. (2024). "Info-Theoretic Memory for Agents." ICML. DOI: 10.1234/icml.5678
- **Key insight**: Decay rate ∝ KL(mem_emb || context). Low MI memories pruned faster.
- **Quantitative**: +32% fidelity (F1: 0.89 vs 0.67), optimal KL threshold = 0.35
- **Use for**: Implement for LLM agents in Reddit community simulations

**LLM Performance**: Llama-3.3-70B on social role-playing

- **Paper**: Wang et al. (2024). "Open LLMs for Social Simulation." ACL. DOI: 10.18653/acl.789
- **Model**: Llama-3.3-70B-Instruct, 4-bit quantized
- **Results**: F1=0.79 (vs Claude-4.5: 0.85, GPT-4: 0.87)
- **Use for**: Cost-effective baseline for social agent experiments
```

---

## 🧠 Remember

- **Ruthless selectivity**: 3 killer findings > 20 mediocre ones
- **Quantitative precision**: Always include numbers
- **Action-oriented**: "Use for" = concrete application
- **Standalone notes**: Each note independently useful
- **Brief > comprehensive**: Notes for brainstorming, not literature review

---

## 📚 Full Documentation

- Main guide: `SKILL.md`
- Keywords: `references/research_focus_keywords.md`
- Templates: `assets/note_templates.md`

---

**Philosophy**: Be surgically selective. Extract only what advances your research. Capture killer findings with precision.
