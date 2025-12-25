# Research Focus Keywords and Patterns

Comprehensive keyword lists for identifying relevant findings across your 6 research areas.

---

## Area 1: Toxic Language and Hate Speech

### Primary Keywords
- toxicity, toxic language, hate speech, abusive language
- harassment, trolling, cyberbullying, online abuse
- offensive language, harmful content, violent language
- content moderation, moderation policy, automated moderation
- hate speech detection, toxicity detection, abuse detection

### Methods & Measures
- Perspective API, toxicity score, hate speech classifier
- BERT-based toxicity models, RoBERTa hate speech
- multilabel toxicity (severe toxicity, identity attack, threat, obscenity)
- precision, recall, F1 for toxicity detection
- false positive rate, false negative rate
- inter-annotator agreement (Krippendorff's α, Cohen's κ)

### Datasets & Benchmarks
- CivilComments, Jigsaw Toxic Comments
- HateXplain, COLD (Content moderation in Online Discussions)
- Reddit toxicity dataset, Twitter hate speech
- Stormfront, Gab hate speech corpora

### Interesting Patterns
- "controlled toxicity generation" → synthetic data for training
- "context-aware toxicity" → same text, different toxicity based on context
- "toxicity propagation" → how toxic comments spread influence
- "counter-speech effectiveness" → responses that reduce toxicity
- "platform-specific norms" → toxicity thresholds vary by community

---

## Area 2: LLM Agent Social Simulation

### Primary Keywords
- LLM agent, large language model agent, AI agent
- multi-agent simulation, agent-based modeling (ABM)
- social simulation, behavioral simulation, agent interaction
- emergent behavior, collective phenomena, social dynamics
- agent memory, belief state, agent reasoning
- behavioral fidelity, simulation realism, validation

### Agent Architectures
- memory mechanisms (short-term, long-term, episodic, semantic)
- planning algorithms (ReACT, chain-of-thought, tree-of-thought)
- perception modules, action selection, belief updating
- inter-agent communication, message passing
- personality modeling, trait-based agents

### Memory Mechanisms (High Priority)
- **Controlled forgetting**: decay functions, selective retention
- working memory, episodic memory, semantic memory
- memory retrieval strategies (recency, relevance, importance)
- forgetting curves, Ebbinghaus decay
- information-theoretic memory (entropy-based pruning)

### Validation Metrics
- behavioral fidelity (how realistic are agent behaviors?)
- Turing test variants, human-AI indistinguishability
- correlation with human data (opinion dynamics, conversation flow)
- emergent macro-patterns (polarization, consensus, fragmentation)
- agent-based model calibration

### Datasets & Benchmarks
- Tachikuma (multi-agent social simulation benchmark)
- AgentBench (LLM agent capabilities)
- social dilemma games (prisoner's dilemma, public goods, trust games)
- opinion dynamics datasets, debate transcripts

---

## Area 3: Network Science + Statistical Physics + Information Theory

### Network Science Keywords
- network evolution, temporal networks, dynamic networks
- network topology, degree distribution, scale-free, small-world
- centrality (degree, betweenness, closeness, eigenvector, PageRank)
- community detection, modularity, Louvain algorithm, label propagation
- network motifs, triadic closure, clustering coefficient
- assortativity, homophily, preferential attachment
- cascades, diffusion, influence propagation, viral spread
- network resilience, percolation, fragmentation

### Statistical Physics Keywords
- phase transitions, critical phenomena, criticality
- order parameters, correlation length, susceptibility
- Ising model, spin glass, Potts model applied to social systems
- mean-field approximation, renormalization group
- self-organized criticality (SOC)
- scaling laws, power laws, universality classes
- thermodynamic analogies (social temperature, entropy)

### Information Theory Keywords
- entropy (Shannon entropy, Rényi entropy, von Neumann entropy)
- mutual information, conditional entropy, joint entropy
- KL divergence (Kullback-Leibler), Jensen-Shannon divergence
- transfer entropy, Granger causality
- information flow, information bottleneck
- surprisal, self-information
- channel capacity, rate-distortion
- cross-entropy (for models/predictions)

### Interdisciplinary Bridges (High Priority)
- "information-theoretic network measures"
- "statistical mechanics of social networks"
- "entropy maximization in social systems"
- "phase transitions in online communities"
- "information flow in social networks"
- "thermodynamics of opinion dynamics"
- "critical slowing down" before tipping points

### Quantitative Measures to Extract
- Critical exponents (β, γ, ν)
- Phase transition thresholds (critical temperature Tc, percolation threshold pc)
- Entropy values for network states
- Mutual information between variables
- Transfer entropy rates
- Scaling exponents for power laws
- Modularity Q scores
- Clustering coefficients (local, global)

---

## Area 4: Open-Source LLM Capabilities

### Model Names (Check Performance Data)
- **Llama family**: Llama 3.3, Llama 3.2, Llama 3.1, Llama 3, Llama 2
- **Mistral family**: Mistral Large, Mistral Medium, Mistral Small, Mixtral MoE
- **Qwen family**: Qwen 2.5, QwQ, Qwen-VL
- **Phi**: Phi-4, Phi-3
- **DeepSeek**: DeepSeek-V3, DeepSeek-Coder
- **Yi**: Yi-Lightning, Yi-Large
- **Other**: Gemma, OLMo, Falcon, MPT, StableLM

### Tasks & Benchmarks
- **Social understanding**: ToMi (Theory of Mind), SocialIQA, SOCKET
- **Instruction following**: IFEval, MT-Bench
- **Reasoning**: GPQA, MATH, GSM8K, ARC, HellaSwag
- **Agent capabilities**: AgentBench, WebShop, ScienceWorld
- **Long context**: RULER, LongBench, InfiniteBench
- **Conversational**: AlpacaEval, Arena Hard, Chatbot Arena Elo

### What to Extract
- Exact model name and size (e.g., "Llama-3-70B-Instruct")
- Quantization details if mentioned (4-bit, 8-bit, FP16)
- Benchmark scores (report exact numbers)
- Comparison to baselines (GPT-4, Claude, other open models)
- Prompting strategies used (few-shot, chain-of-thought, system prompts)
- Fine-tuning details (LoRA, full fine-tuning, dataset size)

### Interesting Patterns
- "small models outperform large models on [specific task]"
- "fine-tuning on [small dataset] achieves [X]% of GPT-4 performance"
- "open-source model achieves SOTA on [benchmark]"
- "mixture-of-experts architecture improves [capability]"
- "context length extension to [X] tokens maintains quality"

---

## Area 5: Trust and Reputation Quantification

### Primary Keywords
- trust, reputation, credibility, trustworthiness
- reputation systems, trust metrics, reputation score
- social capital, social trust, interpersonal trust
- trust propagation, trust transitivity
- reputation decay, reputation dynamics
- trust network, web of trust
- credibility assessment, source credibility

### Quantitative Measures (High Priority)
- PageRank-based trust (EigenTrust, TrustRank)
- Bayesian reputation systems
- Beta reputation systems
- Information-theoretic reputation (entropy-based)
- Graph-based trust metrics (Advogato, Appleseed)
- Feedback aggregation (eBay-style star ratings)
- Trustworthiness scores (0-1 normalized)

### Information-Theoretic Approaches (Very High Priority)
- Mutual information between user actions and reputation
- Entropy of reputation distribution
- KL divergence for trust belief updates
- Information gain from trust evidence
- Surprisal-based reputation updates
- Channel capacity for trust signals

### Datasets & Benchmarks
- Epinions trust network
- Slashdot Zoo (friend/foe relationships)
- Wikipedia admin elections (trust votes)
- Reddit karma, StackExchange reputation points
- Bitcoin OTC trust network

### Interesting Patterns
- "reputation inflation/deflation over time"
- "trust asymmetry" (A trusts B but B doesn't trust A)
- "reputation bubbles" (localized high-trust clusters)
- "Sybil attack resistance" in reputation systems
- "cold start problem" for new users

---

## Area 6: Niche Online Communities

### Platform Keywords
- StackExchange, Stack Overflow, MathOverflow, Cross Validated
- Reddit (especially Q&A subreddits: r/AskScience, r/ExplainLikeImFive, r/AskHistorians)
- Quora, Yahoo Answers (historical data)
- Discord servers, Slack communities
- GitHub discussions, issue trackers
- HackerNews, Lobsters

### Community Structure
- expertise networks, expert identification
- askers vs. answerers, knowledge contributors
- moderator networks, moderation patterns
- core-periphery structure
- community evolution (growth, decline, stabilization)
- subcommunity formation, topic clustering

### Content Quality
- answer quality metrics (votes, accepted answers, edits)
- question quality (clarity, upvotes, answers received)
- duplicate detection, canonical questions
- edit patterns, quality improvement over time
- spam detection, low-quality content filtering

### Moderation Patterns
- moderation actions (close, delete, edit, migrate)
- community norms, site-specific policies
- moderator workload, burnout
- user sanctions (warnings, suspensions, bans)
- appeals and reversals

### Comparative Analyses
- cross-platform comparisons (Reddit vs StackExchange)
- topic-specific community differences (CS vs biology SE sites)
- evolution patterns across different communities
- moderation style differences
- content quality metrics across platforms

### Interesting Patterns
- "Matthew effect" (rich get richer in reputation)
- "expert retention" vs "churn"
- "question-answer cycles" and temporal patterns
- "community fragmentation" events
- "knowledge preservation" strategies

---

## High-Value Finding Indicators

### Signals of Novelty
- "We introduce a new [method/metric/model]"
- "To the best of our knowledge, this is the first"
- "Unlike previous approaches, our method"
- "We propose a novel"
- Mathematical formulations (equations, algorithms)
- Ablation studies showing component contributions

### Signals of Quantitative Findings
- Tables with performance metrics
- Figures with error bars, confidence intervals
- Statistical significance tests (p-values, effect sizes)
- Benchmarks with multiple baselines
- Equations defining new metrics
- Threshold values, critical points

### Signals of Interdisciplinary Work
- References to multiple fields in abstract/intro
- Cross-domain vocabulary (physics + social, info theory + agents)
- Analogies between fields
- Transfer of methods across domains
- Unified frameworks spanning disciplines

### Signals of High-Quality Arguments
- "We argue that" followed by logical reasoning
- Well-structured theoretical frameworks
- Clear definitional work
- Strong empirical support for claims
- Acknowledged limitations and caveats
- Comparison with alternative explanations

---

## Red Flags (Skip These)

### Low-Value Content
- Pure literature review without novel contributions
- Vague claims without quantification
- "Future work will explore" (without current results)
- Incremental improvements without theoretical insight
- Standard practices presented as novel
- Results without statistical validation

### Out-of-Scope
- Purely technical infrastructure (unless it enables social simulation)
- Application domains unrelated to social systems
- Pure NLP without social context
- General machine learning without social application
- Hardware optimization
- Purely commercial applications

---

## Extraction Heuristics

### When Scanning Papers

1. **Abstract**: Does it mention your keywords? Novel methods? Quantitative results?
2. **Introduction**: Problem statement clarity, gap identification
3. **Related Work**: What's missing from prior work? (Motivation for novelty)
4. **Methods**: Look for equations, algorithms, novel architectures
5. **Results**: Tables with numbers, figures with comparisons
6. **Discussion**: Interdisciplinary connections, theoretical insights
7. **Conclusion**: Quantitative summary, main takeaways

### Grep-Friendly Patterns

Use these regex patterns to search markdown:

```bash
# Find equations
grep -E "\$\$|\\begin\{equation\}" paper.md

# Find tables
grep -E "^\|.*\|.*\|" paper.md

# Find metrics
grep -iE "(accuracy|precision|recall|f1|auc|entropy|mutual information)" paper.md

# Find model names
grep -iE "(llama|mistral|qwen|gpt|claude)" paper.md

# Find statistical tests
grep -iE "(p\s*[<>=]\s*0\.|cohen|effect size|confidence interval)" paper.md

# Find novelty claims
grep -iE "(novel|new|first|introduce|propose)" paper.md

# Find benchmarks
grep -iE "(benchmark|dataset|baseline|state-of-the-art|SOTA)" paper.md
```

---

## Summary

Use this reference to:
1. **Identify** relevant papers quickly by scanning for keywords
2. **Navigate** to high-value sections (Methods, Results, equations)
3. **Extract** quantitative findings with precision
4. **Filter** out low-value or out-of-scope content
5. **Recognize** novelty, interdisciplinary work, and citable arguments

Remember: **Ruthless selectivity**. If a finding doesn't match your research areas AND finding types, skip it. Only extract killer insights.
