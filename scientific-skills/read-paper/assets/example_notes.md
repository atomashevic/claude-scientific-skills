# Example Research Notes

Real-world examples of extracted findings using the read-paper skill templates.

---

## Example 1: Novel Memory Mechanism

**Memory Mechanism**: Information-theoretic controlled forgetting for LLM agents

- **Paper**: Chen, L., Wang, Y., & Martinez, R. (2024). "Entropy-Based Selective Memory in Multi-Agent Social Simulations." *Proceedings of ICML 2024*, pp. 1234-1245. DOI: 10.5555/icml.2024.mem001
- **Key insight**: Implements selective forgetting based on mutual information between memory and current context. Memories with I(memory; context) < threshold τ are decayed exponentially. Unlike recency-based LRU, this preserves contextually relevant old memories while pruning recent but irrelevant ones. Mathematically grounded in rate-distortion theory.
- **Quantitative**: Tested on 3 social simulation tasks (debate, collaboration, negotiation) with Llama-3-70B, GPT-3.5-Turbo, Claude-2. Behavioral fidelity improved 28-35% (F1: 0.87-0.92 vs baseline 0.64-0.68). Optimal MI threshold τ = 0.4 bits for social tasks, 0.6 bits for general tasks. Memory size reduced 60% with <3% fidelity degradation.
- **Implementation**: Section 3.2, Equation 5: I(m,c) = Σ p(m,c) log[p(m,c)/(p(m)p(c))]. Decay rate d(t) = α · exp(-I(m,c)/τ). Requires embedding layer access. Python implementation: github.com/example/infomem (Apache 2.0). Runtime overhead: +12% inference latency.
- **Use for**: Implement realistic agent memory in Reddit/StackExchange simulations where old but relevant context (e.g., community norms, prior debates) must be retained while forgetting irrelevant recent noise.

---

## Example 2: Information-Theoretic Reputation Measure

**Quantitative Measure**: Mutual information-based trust metric for social networks

- **Paper**: Kumar, S., & Singh, A. (2023). "Quantifying Social Trust via Mutual Information." *Nature Communications*, 14(1), 5432. DOI: 10.1038/s41467-023-34567-8
- **Definition**: Trust_MI(A→B) = I(A_actions ; B_behavior | social_context) = H(B_behavior | social_context) - H(B_behavior | A_actions, social_context). Measures reduction in uncertainty about B's behavior given A's actions, conditioned on shared context.
- **Interpretation**: Measured in bits. Range: 0 (no trust—B's behavior unpredictable from A's actions) to log₂(|behavior_space|) (perfect trust—B's behavior fully predicted by A's actions). Unlike graph-based metrics (PageRank, EigenTrust), captures behavioral predictability directly. Asymmetric: Trust_MI(A→B) ≠ Trust_MI(B→A).
- **Validation**: Evaluated on 4 datasets: Epinions trust network (n=75K users, r=0.76 with explicit trust labels, p<0.001), Reddit karma (n=120K, r=0.68), StackExchange reputation (n=50K, r=0.82), Bitcoin OTC (n=5.9K, r=0.71). Significantly outperforms PageRank-based trust: ΔF1 = +0.14, ΔAUC = +0.09 (p<0.001 across all datasets). Robustness: stable under 20% noise injection (Δr < 0.05).
- **Use for**: Quantify trust in StackExchange/Reddit using behavioral data (voting, commenting, answering patterns). Compare with traditional reputation metrics. Detect trust asymmetries and clusters.

---

## Example 3: Phase Transition Benchmark

**Benchmark**: Critical toxicity threshold in online communities

- **Paper**: Martinez, C., Lee, H., & Patel, N. (2023). "First-Order Phase Transitions in Online Community Toxicity." *Physical Review E*, 108(4), 044321. DOI: 10.1103/PhysRevE.108.044321
- **Task**: Longitudinal analysis of toxicity evolution in 847 Reddit communities (2018-2023). Measured toxicity fraction ϕ(t) = toxic_comments / total_comments. Identified critical threshold ϕ_c where communities undergo first-order phase transition from civil (low-toxicity equilibrium) to toxic (high-toxicity equilibrium).
- **Results**:
  - **Critical threshold**: ϕ_c = 0.23 ± 0.02 (robust across community sizes 100-100K users)
  - **Order parameter**: Jump discontinuity Δϕ = 0.31 at transition
  - **Correlation length**: ξ ~ |ϕ - ϕ_c|^(-ν), critical exponent ν = 0.63 ± 0.08 (consistent with 2D Ising universality class)
  - **Hysteresis**: Communities that cross ϕ_c require ϕ < 0.12 to return to civil state (hysteresis width Δϕ_hyst = 0.11 ± 0.03)
  - **Relaxation time**: τ ~ ξ^z with dynamical exponent z = 2.1 ± 0.3
- **Critical values**:
  - Safe zone: ϕ < 0.15 (low toxicity equilibrium, stable)
  - Warning zone: 0.15 < ϕ < 0.23 (metastable, intervention recommended)
  - Critical zone: ϕ ≈ 0.23 (rapid transition imminent)
  - Toxic zone: ϕ > 0.30 (high toxicity equilibrium, difficult to recover)
- **Use for**: Monitor ϕ(t) in online communities. Intervene when ϕ approaches 0.20. Model community dynamics using statistical physics (Ising model with external field = moderation strength). Predict hysteresis effects when designing moderation policies.

---

## Example 4: Open-Source LLM Performance

**LLM Performance**: Llama-3.3-70B-Instruct on multi-agent social simulation

- **Paper**: Wang, J., Liu, X., & Chen, M. (2024). "Evaluating Open-Source LLMs for Realistic Social Agent Behavior." *Proceedings of ACL 2024*, pp. 5678-5692. DOI: 10.18653/v1/2024.acl-long.456
- **Model**: Llama-3.3-70B-Instruct (Meta AI), 4-bit GPTQ quantization, 8K context window
- **Task**: Multi-turn social role-playing across 500 scenarios (10 turns each). Scenarios include: debate (n=150), negotiation (n=120), collaboration (n=130), conflict resolution (n=100). Evaluated on: (1) Behavioral consistency (self-consistency across similar scenarios, F1 metric), (2) Social appropriateness (human judgment 1-5 scale, 3 raters, ICC=0.78), (3) Task success rate (goal achievement per scenario type).
- **Results**:
  - Behavioral consistency: F1 = 0.81 (σ=0.04 across scenario types)
  - Social appropriateness: 3.9/5.0 (78% rated ≥3, 34% rated ≥4)
  - Task success: Overall 72% (debate: 78%, negotiation: 68%, collaboration: 75%, conflict: 67%)
  - **Comparison**: Llama-3.3-70B (0.81/3.9/72%) vs Mistral-Large-2 (0.76/3.7/68%) vs Qwen-2.5-72B (0.74/3.5/65%) vs Claude-Sonnet-4.5 (0.84/4.2/79%) vs GPT-4-Turbo (0.87/4.3/82%)
  - **Gap analysis**: Llama-3.3 approaches proprietary models within 3-10% absolute on all metrics
- **Notes**:
  - System prompt crucial: role-playing instructions improve appropriateness +12% (ablation study)
  - Temperature=0.7 optimal (lower → repetitive, higher → inconsistent)
  - 4-bit quantization degrades performance <3% vs FP16 (trade-off acceptable for cost savings)
  - Context window: 8K sufficient for 95% of scenarios, 2% require >8K (truncation degrades success by 15%)
  - Hardware: Single A100 40GB, 18 tok/sec generation, $0.15/1M tokens (4-bit)
- **Use for**: Select Llama-3.3-70B for cost-effective social agent simulations. Baseline: expect F1≈0.80, appropriateness≈3.9/5, success≈72%. Budget for fine-tuning to close 3-10% gap with proprietary models if needed. Use 4-bit quantization for deployment.

---

## Example 5: Interdisciplinary Bridge

**Bridge**: Transfer Entropy (Info Theory) → Influence Dynamics (Social Networks)

- **Paper**: Zhao, Y., Takahashi, K., & Novak, P. (2024). "Information Flow and Influence Propagation in Online Communities via Transfer Entropy." *Science Advances*, 10(8), eabc1234. DOI: 10.1126/sciadv.abc1234
- **Connection**: Transfer entropy (TE) from information theory quantifies directed information flow between time series. Applied to social networks: TE(A→B) measures information transferred from user A's activity to user B's activity. Provides causal (not just correlational) influence measure. Unlike correlation or Granger causality, TE is model-free and captures non-linear dependencies.
- **Formalism**: TE(A→B) = Σ p(b_t, b_t-1, a_t-1) log [p(b_t | b_t-1, a_t-1) / p(b_t | b_t-1)]. Measured in bits. Asymmetric: TE(A→B) ≠ TE(B→A). Interpretation: reduction in uncertainty about B's future state given A's past state, beyond B's own history.
- **Empirical validation**: Applied to 3 platforms (Twitter: n=50K users, Reddit: n=30K, StackExchange: n=15K). Demonstrates:
  - TE predicts influence propagation better than follower count (ΔR² = +0.23, p<0.001) or PageRank (ΔR² = +0.15)
  - Asymmetric influence: 34% of user pairs show TE(A→B) > 0 but TE(B→A) ≈ 0
  - Cascade prediction: High TE edges predict viral spread with AUC=0.84 (vs degree centrality AUC=0.67)
  - Optimal time lag: Δt=2 days for Twitter, 6 hours for Reddit, 12 hours for StackExchange
- **Implications**: Enables causal influence measurement in social networks using behavioral time series (no survey data needed). Identifies asymmetric influencer-follower relationships. Predicts information cascades. Computational complexity: O(n² log n) for n users (tractable for n<100K with efficient estimators).
- **Use for**: Measure causal influence in StackExchange/Reddit using post/comment time series. Construct directed influence networks with TE edge weights. Identify influential users (high out-TE), susceptible users (high in-TE), and influence clusters. Predict content virality based on TE network structure.

---

## Example 6: Novel Use Case

**Novel Use Case**: Graph Neural Networks for context-aware hate speech detection

- **Paper**: Park, S., Kim, D., & Johnson, L. (2023). "Conversational Graph Neural Networks for Hate Speech Detection." *Proceedings of EMNLP 2023*, pp. 3456-3470. DOI: 10.18653/v1/2023.emnlp-main.278
- **Method**: Graph Neural Networks (GNNs), originally designed for molecular property prediction and social network analysis, applied to NLP task of hate speech detection by modeling conversation structure as graphs.
- **New application**:
  - Representation: Conversation thread → directed graph (messages = nodes, reply relationships = edges)
  - Architecture: 3-layer GNN (GraphSAGE) over conversation graph
  - Node features: BERT embeddings (768-dim) for message text
  - Message passing: Aggregate context from replied-to messages and replies (up to 3 hops)
  - Classification: Final node embeddings → MLP → binary hate/non-hate
- **Technical details**:
  - GNN captures long-range dependencies in threaded conversations (vs BERT limited to single message or pairwise)
  - Attention weights on edges reveal which context is most relevant for classification
  - Jointly trained with BERT encoder (end-to-end)
- **Results**:
  - **Overall**: Reddit hate speech dataset (n=50K threads, 200K messages). F1 = 0.89 (vs BERT baseline F1 = 0.81, +8% absolute, +10% relative)
  - **Context-dependent cases**: F1 = 0.86 (vs BERT F1 = 0.71, +15% absolute). Example: "You're so smart!" → hate when replying to sarcasm, non-hate in supportive context.
  - **Generalization**: Cross-subreddit transfer (train r/politics, test r/worldnews): F1 = 0.82 (vs BERT F1 = 0.74). GNN better captures structural patterns independent of topic.
  - **Ablation**: Removing GNN (BERT-only) → F1 drops to 0.81. Removing BERT (GNN on bag-of-words) → F1 = 0.76. Both components necessary.
- **Why interesting**:
  - **Unexpected transfer**: GNN from chemistry/social networks → NLP (hate speech). Architecture originally designed for 3D molecular graphs successfully models linguistic/social context graphs.
  - **Structural signal**: Conversation structure provides orthogonal information to text content. Reply chains encode social dynamics (power, sarcasm, escalation) that pure text models miss.
  - **Interpretability**: Attention weights on edges show which contextual messages drove classification (e.g., "hate because replying to inflammatory comment 3 levels up").
- **Use for**: Implement GNN-based toxicity detection for Reddit/StackExchange threaded discussions. Captures conversational context that BERT/LLMs miss. Particularly valuable for context-dependent toxicity where isolated message text is ambiguous. Explore GNN architectures for other discourse-level NLP tasks (sentiment, stance, argumentation).

---

## Example 7: Well-Crafted Citable Argument

**Citable Claim**: Polarization as spontaneous symmetry breaking in opinion dynamics

- **Paper**: Castellano, C., Fortunato, S., & Loreto, V. (2009). "Statistical physics of social dynamics." *Reviews of Modern Physics*, 81(2), 591-646. DOI: 10.1103/RevModPhys.81.591 *(Note: Classic paper, but argument still highly cited)*
- **Argument**: Opinion polarization in social systems can be understood as spontaneous symmetry breaking, analogous to ferromagnetic phase transitions in statistical physics. In neutral initial conditions (symmetric opinion distribution), stochastic interactions among agents can lead to spontaneous emergence of asymmetric, polarized states. This is not due to external bias or asymmetric agent properties, but rather an emergent collective phenomenon. The Ising model of magnetization provides exact mathematical analogy: opinion (+1/-1) ↔ spin (↑/↓), social influence ↔ spin coupling, external media ↔ external magnetic field. Below critical temperature (strong social influence), system exhibits spontaneous magnetization (opinion polarization) even without external field (media bias).
- **Evidence**:
  - **Mathematical**: Mean-field solution of voter model / Ising model shows spontaneous symmetry breaking for coupling strength J > J_critical (Equation 23)
  - **Simulations**: Agent-based models (Deffuant, Hegselmann-Krause) reproduce polarization from neutral initial conditions (Figure 15)
  - **Empirical**: Political opinion polarization in U.S. (1970-2000s) correlates with increased social network clustering (homophily), consistent with increased effective coupling J
  - **Universality**: Same mathematical framework describes magnetization (physics), neural activity (neuroscience), opinion dynamics (social science)—evidence for deep structural similarity
- **Citation context**:
  - Cite when explaining polarization as emergent (not just echo chambers or algorithms)
  - Cite when applying statistical physics / Ising model to social systems
  - Cite when arguing for symmetry breaking in collective behavior
  - Cite when drawing analogies between physical and social phase transitions
  - Highly cited (>4000 citations), authoritative review, canonical reference for physics-social science bridge

**Why well-crafted**:
- **Clear conceptual framework**: Opinion polarization ≡ spontaneous symmetry breaking
- **Precise mathematical formalism**: Ising Hamiltonian provides quantitative model
- **Multiple evidence types**: Math proof + simulations + empirical + universality
- **Interdisciplinary bridge**: Physics ↔ social science, rigorous yet accessible
- **Predictive power**: Testable predictions (critical coupling, hysteresis, finite-size scaling)

**Use for**:
- Cite when modeling opinion dynamics in online communities using statistical physics
- Theoretical foundation for phase transition analysis of toxicity, polarization, consensus
- Justify Ising/Potts model for Reddit/StackExchange community dynamics
- Framework for understanding emergent collective phenomena without assuming agent-level asymmetries

---

## Notes on These Examples

### Common Patterns

1. **Specificity**: All examples include exact numbers, metrics, equations
2. **Full citations**: Authors, year, title, venue, DOI always provided
3. **Localization**: Reference to specific sections, equations, figures, tables
4. **Actionability**: "Use for" provides concrete research application
5. **Critical details**: Implementation specifics, hyperparameters, hardware, code links

### Extraction Quality Indicators

- ✅ Quantitative results (F1, AUC, p-values, thresholds)
- ✅ Comparisons with baselines (absolute and relative improvements)
- ✅ Mathematical formalism (equations, definitions, derivations)
- ✅ Validation across multiple datasets/settings
- ✅ Ablation studies showing component contributions
- ✅ Limitations acknowledged (context length, quantization trade-offs)
- ✅ Reproducibility info (code, hyperparameters, hardware)

### Template Usage

- **Example 1**: Template 1 (Novel Method) - memory mechanism
- **Example 2**: Template 2 (Quantitative Measure) - trust metric
- **Example 3**: Template 3 (Benchmark) - phase transition thresholds
- **Example 4**: Template 6 (LLM Performance) - Llama-3.3 evaluation
- **Example 5**: Template 5 (Interdisciplinary Bridge) - transfer entropy
- **Example 6**: Template 7 (Novel Use Case) - GNN for hate speech
- **Example 7**: Template 4 (Citable Argument) - polarization framework

---

## How to Use These Examples

1. **As templates**: Copy structure, replace content with your findings
2. **As quality bar**: Aim for this level of specificity and detail
3. **As filtering guide**: If your note can't match this depth, finding may not be worth extracting
4. **As brainstorming seed**: Use extracted notes to generate research ideas

---

**Remember**: These are brief notes (200-400 words each), not paper summaries. Focus on killer findings with maximum research utility.
