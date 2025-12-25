# Research Note Templates

Quick-copy templates for extracting different types of findings.

---

## Template 1: Novel Method/Mechanism

```markdown
**[Method Type]**: [Brief descriptive name]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Key insight**: [How it works in 2-3 sentences with technical details]
- **Quantitative**: [Performance metrics, comparisons, improvements over baseline]
- **Implementation**: [Key technical details: equations, algorithms, hyperparameters]
- **Use for**: [Specific application to your research]
```

**Example**:
```markdown
**Memory Mechanism**: Entropy-driven selective forgetting for LLM agents

- **Paper**: Zhang et al. (2024). "Information-Theoretic Memory Management in Multi-Agent Systems." ICML 2024. DOI: 10.1234/icml.2024.5678
- **Key insight**: Memory decay rate proportional to KL divergence between memory embedding and current context embedding. Memories with low contextual relevance (high KL divergence) decay faster, implementing controlled forgetting based on information theory.
- **Quantitative**: Social simulation fidelity improved 32% (F1: 0.89 vs 0.67). Tested on Llama-3-70B, GPT-3.5, Claude-2. Optimal KL threshold = 0.35 for social tasks, 0.50 for general tasks.
- **Implementation**: Decay rate d(t) = α · KL(p_mem || p_context), where α=0.1 empirically optimal. Requires embedding layer access. Memory pruned when importance I(m) < τ, where I(m) = -log(d(t)).
- **Use for**: Implement for realistic agent memory in Reddit/StackExchange community simulations
```

---

## Template 2: Quantitative Measure/Metric

```markdown
**[Measure Type]**: [Measure name]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Definition**: [Mathematical formula or precise operational definition]
- **Interpretation**: [What it captures, why it's useful, range/units]
- **Validation**: [Empirical results, correlations with other measures, reliability]
- **Use for**: [Your application]
```

**Example**:
```markdown
**Information-Theoretic Reputation**: Mutual information-based trust metric

- **Paper**: Kumar & Singh (2023). "Quantifying Trust via Mutual Information in Social Networks." Nature Communications. DOI: 10.1038/s41467-023-12345-6
- **Definition**: Trust(A→B) = I(A_actions ; B_behavior) = H(B_behavior) - H(B_behavior | A_actions), where I is mutual information, H is Shannon entropy. Captures predictability of B's behavior given A's actions.
- **Interpretation**: Measures in bits (0 to log₂(|behavior_space|)). High I → B's behavior strongly predicted by A's actions → high trust. Zero I → no predictive relationship → no trust basis.
- **Validation**: Tested on Epinions (r=0.76 with explicit trust labels), Reddit karma (r=0.68), StackExchange reputation (r=0.82). Significantly outperforms PageRank-based metrics (ΔF1 = 0.14, p<0.001).
- **Use for**: Quantify trust in StackExchange/Reddit communities using behavioral data (votes, comments, follows)
```

---

## Template 3: Benchmark/Critical Value

```markdown
**Benchmark**: [Task/dataset name]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Task**: [What is being measured/evaluated]
- **Results**: [Model performances, state-of-the-art, comparisons]
- **Critical values**: [Thresholds, phase transitions, performance tiers]
- **Use for**: [Your application]
```

**Example**:
```markdown
**Benchmark**: SocialSim-1K for LLM agent social fidelity

- **Paper**: Li et al. (2024). "SocialSim-1K: Benchmarking LLM Agents on Social Simulation." NeurIPS 2024 Datasets Track. DOI: 10.5555/neurips.2024.bench
- **Task**: 1000 multi-turn social scenarios (debate, negotiation, small talk, conflict resolution). Evaluated on behavioral fidelity (alignment with human transcripts), consistency, and emergent social dynamics.
- **Results**: GPT-4: 0.87 F1, Claude-Sonnet-4.5: 0.85, Llama-3.3-70B: 0.79, Mistral-Large: 0.76, Qwen-2.5-72B: 0.74. Open-source models lag proprietary by 8-13% absolute F1.
- **Critical values**: F1 > 0.80 considered "human-like" (expert evaluation). F1 < 0.65 exhibits noticeable artifacts. Performance scales log-linearly with parameter count (R²=0.91).
- **Use for**: Baseline for evaluating open-source LLMs on social simulation tasks
```

---

## Template 4: Citable Argument/Theoretical Framework

```markdown
**Citable Claim**: [Topic/framework name]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Argument**: [Well-crafted claim or theoretical framework, 3-5 sentences]
- **Evidence**: [Supporting empirical data, logical reasoning, prior work]
- **Citation context**: [When to cite this in your own writing]
```

**Example**:
```markdown
**Citable Claim**: Phase transitions in online community toxicity

- **Paper**: Martinez et al. (2023). "Critical Phenomena in Online Community Dynamics." Physical Review E. DOI: 10.1103/PhysRevE.108.044321
- **Argument**: Online communities exhibit first-order phase transitions in toxicity levels, analogous to liquid-gas transitions in thermodynamics. Below critical moderation threshold τc, communities exist in "civil phase" (low toxicity equilibrium). Above τc, rapid transition to "toxic phase" (high toxicity equilibrium). Hysteresis observed: restoring civility requires stronger moderation than preventing toxicity onset.
- **Evidence**: Analyzed 847 Reddit communities over 5 years. Identified τc = 0.23 (fraction of toxic comments). Measured correlation length ξ divergence near transition (ξ ~ |τ - τc|^(-ν), ν=0.63±0.08). Hysteresis width Δτ = 0.11 ± 0.03.
- **Citation context**: Cite when discussing moderation strategies, explaining sudden toxicity increases, or applying statistical physics to social systems
```

---

## Template 5: Interdisciplinary Bridge

```markdown
**Bridge**: [Domain A] → [Domain B]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Connection**: [How the domains are linked, what formalism enables transfer]
- **Formalism**: [Mathematical/conceptual framework bridging domains]
- **Implications**: [What this enables, new research directions]
- **Use for**: [Your application]
```

**Example**:
```markdown
**Bridge**: Statistical Mechanics → Online Community Dynamics

- **Paper**: Hernandez & Chen (2024). "Ising Model of Opinion Dynamics in Social Networks." Science Advances. DOI: 10.1126/sciadv.abcd1234
- **Connection**: Online community opinions map to Ising spin system. User opinion (+1/-1) equivalent to spin state. Social influence → spin coupling. External media → external magnetic field.
- **Formalism**: Hamiltonian H = -J Σ_{<i,j>} σᵢσⱼ - h Σᵢ σᵢ, where J=social influence strength, h=media bias, σᵢ=user i's opinion. Phase transition at critical temperature kT_c = J/tanh⁻¹(0). Mean-field solution predicts polarization order parameter m = tanh(Jm/kT + h/kT).
- **Implications**: Predicts critical points where communities polarize, enables quantitative modeling of opinion dynamics, suggests intervention strategies (analogous to cooling/heating).
- **Use for**: Model opinion dynamics in Reddit/StackExchange using statistical physics framework, predict polarization phase transitions
```

---

## Template 6: Open-Source LLM Performance

```markdown
**LLM Performance**: [Model name] on [Task/benchmark]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Model**: [Specific model name, size, quantization]
- **Task**: [Benchmark/evaluation task description]
- **Results**: [Scores, comparisons with other models]
- **Notes**: [Prompting strategies, fine-tuning, context length, hardware]
- **Use for**: [Your application]
```

**Example**:
```markdown
**LLM Performance**: Llama-3.3-70B-Instruct on social role-playing

- **Paper**: Wang et al. (2024). "Evaluating Open-Source LLMs for Multi-Agent Social Simulation." ACL 2024. DOI: 10.18653/v1/2024.acl-long.789
- **Model**: Llama-3.3-70B-Instruct, 4-bit GPTQ quantization
- **Task**: Multi-turn social role-playing across 500 scenarios (debate, negotiation, collaboration). Evaluated on behavioral consistency (self-consistency), social appropriateness (human judgment), and task success rate.
- **Results**: Consistency: 0.81, Appropriateness: 0.78, Success: 0.72. Outperforms Mistral-Large-2 (0.76/0.74/0.68) and Qwen-2.5-72B (0.74/0.71/0.65). Approaches Claude-Sonnet-4.5 (0.84/0.82/0.79) within 3-7% absolute.
- **Notes**: 8K context window, temperature=0.7 optimal. Role-playing system prompt crucial (+12% appropriateness). 4-bit quantization degradation <3% vs FP16. Runs on single A100 40GB.
- **Use for**: Select Llama-3.3-70B for cost-effective social agent simulations, benchmark against this baseline
```

---

## Template 7: Novel Use Case/Application

```markdown
**Novel Use Case**: [Method/model] applied to [new domain/task]

- **Paper**: [Authors] ([Year]). [Title]. [Journal/Venue]. DOI: [doi]
- **Method**: [Original method and its typical use]
- **New application**: [How it's applied in new context]
- **Results**: [Performance, insights, advantages]
- **Why interesting**: [What makes this transfer novel or surprising]
- **Use for**: [Your potential application]
```

**Example**:
```markdown
**Novel Use Case**: Graph Neural Networks for hate speech detection

- **Paper**: Park et al. (2023). "Contextual Hate Speech Detection via Conversation Graph Neural Networks." EMNLP 2023. DOI: 10.18653/v1/2023.emnlp-main.456
- **Method**: Graph Neural Networks (GNNs), typically used for molecular property prediction or social network analysis, applied to hate speech detection by modeling conversations as graphs.
- **New application**: Conversation structure → graph (messages=nodes, replies=edges). GNN propagates context through reply chains. Captures long-range dependencies and conversational dynamics that BERT-based models miss.
- **Results**: F1=0.89 on Reddit hate speech (vs BERT F1=0.81, +8%). Especially strong on context-dependent hate speech (+15% over BERT). Generalizes across subreddits better (transfer F1=0.82 vs 0.74).
- **Why interesting**: Unexpected application of GNNs to NLP task. Shows conversation structure provides orthogonal signal to text content. Architectural innovation transferring molecular AI to social content moderation.
- **Use for**: Implement GNN-based toxicity detection for Reddit/StackExchange with conversational structure
```

---

## Quick Selection Guide

**Use Template 1** when: Novel algorithm, architecture, or mechanism is introduced

**Use Template 2** when: New quantitative measure or metric is defined

**Use Template 3** when: Benchmark dataset, evaluation results, or critical thresholds are reported

**Use Template 4** when: Strong theoretical argument or framework is presented

**Use Template 5** when: Methods/concepts transfer between disciplines (especially info theory ↔ social science)

**Use Template 6** when: Open-source LLM performance data is reported

**Use Template 7** when: Familiar method used in surprising new way

---

## Combining Templates

Some findings span multiple categories. Create multiple notes or use hybrid format:

**Example: Novel metric with benchmark results**

Combine Template 2 (Quantitative Measure) with Template 3 (Benchmark):

```markdown
**Information-Theoretic Toxicity Measure + Benchmark**

**Metric**: Conditional entropy toxicity score

- **Paper**: Lee et al. (2024). "Entropy-Based Toxicity Metrics for Context-Aware Content Moderation." ICWSM 2024. DOI: 10.1609/icwsm.v18i1.12345
- **Definition**: Toxicity_entropy(m | C) = H(toxic | message_m, context_C) - H(toxic | context_C), where H is Shannon entropy. Measures surprise in toxicity given context.
- **Interpretation**: High H → message is surprisingly toxic given context. Accounts for context norms (profanity acceptable in some communities).
- **Benchmark**: Tested on 3 datasets: Reddit (n=100K), Twitter (n=80K), StackExchange (n=50K).
  - Reddit: AUC=0.93 (vs Perspective API 0.87)
  - Twitter: AUC=0.91 (vs Perspective 0.85)
  - StackExchange: AUC=0.88 (vs Perspective 0.79)
  - Largest gains on context-dependent toxicity (+12% AUC)
- **Use for**: Implement context-aware toxicity detection for community-specific norms
```

---

## Notes on Note-Taking

### Best Practices

1. **One finding per note**: Don't combine multiple unrelated findings
2. **Standalone completeness**: Include enough context that the note is useful months later
3. **Full citation**: Always include authors, year, title, venue, DOI
4. **Quantitative specificity**: Report exact numbers, not "significant improvement"
5. **Localization**: Note where to find details (section, equation, table, figure number)
6. **Action-oriented**: Always include "Use for" with concrete application

### Common Mistakes

❌ **Vague**: "They propose a new memory mechanism for agents"
✅ **Specific**: "Entropy-driven decay where memories with KL divergence > 0.35 from context are pruned"

❌ **No numbers**: "Significant improvement on benchmark"
✅ **With numbers**: "F1 improved from 0.67 to 0.89 (+32% relative, Cohen's d=1.2, p<0.001)"

❌ **No citation**: "Recent work shows..."
✅ **With citation**: "Zhang et al. (2024, DOI: 10.1234/example) show..."

❌ **Too long**: Full paragraph summaries
✅ **Concise**: 3-5 bullet points, dense with information

❌ **No application**: Just describes what paper did
✅ **Applied**: "Use for: Implement in my Reddit simulation to..."

---

## Digital Workflow Tips

### Obsidian / Markdown Notes

- Tag notes: `#memory-mechanism #information-theory #llm-agents`
- Link related notes: `[[Entropy-based memory]] connects to [[Agent architecture]]`
- Use dataview queries to aggregate findings by tag/topic

### Zotero / Reference Manager

- Attach extracted notes to paper entry
- Use tags/collections aligned with your 6 research areas
- Export notes alongside BibTeX for integrated workflow

### Plain Text / Git

- Commit each note as you extract it
- Use consistent filenames: `YYYY-MM-DD_FirstAuthor_KeyTopic.md`
- grep/ripgrep to search across all notes

---

## Summary

These templates provide structure for rapid, high-quality note extraction. Copy-paste the appropriate template, fill in the blanks, and you have a citation-ready research note.

**Key principles**:
- Specificity over generality
- Quantitative over qualitative
- Action-oriented over passive description
- Standalone completeness over brevity

Use these templates to build a curated, high-signal research knowledge base.
