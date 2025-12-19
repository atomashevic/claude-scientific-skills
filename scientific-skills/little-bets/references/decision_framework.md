# Decision Framework: Continue, Pivot, or Park?

After completing a little bet, you need to decide: continue investing, pivot to a new direction, or park the idea. This framework helps make that decision systematically.

---

## Result Categories

### 🔥 Exciting

**Definition**: Results exceeded expectations, clear signal, strong potential.

**Indicators**:
- Key metric significantly exceeds minimum threshold
- Result is surprising in a good way
- Method works better than expected
- Clear path forward is obvious

**Example**: "Achieved 95% accuracy on toy data when 70% was the goal. Method is robust across 10 random seeds."

**Decision**: **Continue** - Design larger experiment, refine method, or test on real data.

---

### ✅ Promising

**Definition**: Met minimum criteria, shows potential, worth exploring further.

**Indicators**:
- Key metric meets or slightly exceeds minimum threshold
- Method works but needs refinement
- Some signal detected, though noisy
- Reasonable next steps identified

**Example**: "Achieved 72% accuracy (minimum was 70%). Method works but is sensitive to hyperparameters."

**Decision**: **Iterate** - Refine hypothesis, adjust parameters, or try a variation.

---

### 🤔 Unclear

**Definition**: Results are ambiguous, need more information to decide.

**Indicators**:
- Mixed signals (some good, some bad)
- Results depend heavily on parameters/data
- Not enough data to draw conclusion
- Method partially works but unclear why

**Example**: "Accuracy varies from 50% to 80% depending on random seed. Not sure if method is unstable or data is too small."

**Decision**: **Pivot** - Change approach, gather more information, or simplify the question.

---

### ❌ Dead End

**Definition**: Clear failure, method doesn't work, fundamental issue identified.

**Indicators**:
- Key metric well below minimum threshold
- Method fails catastrophically
- Fundamental flaw identified
- No clear path to improvement

**Example**: "Method achieves 45% accuracy (worse than random). The core assumption appears flawed."

**Decision**: **Park** - Document learnings, move on to next idea.

---

### 💡 Pivot

**Definition**: Found something different and interesting, not what you originally asked.

**Indicators**:
- Original question answered negatively, but discovered something else
- Method works for different problem than intended
- Side effect is more interesting than main result
- New question emerged that's more promising

**Example**: "Network topology doesn't affect convergence, but discovered that initial opinion distribution matters a lot."

**Decision**: **New Bet** - Spawn new bet with the discovered question.

---

## Decision Questions

Before deciding, answer these questions:

### 1. What Did We Learn?

- [ ] What worked?
- [ ] What didn't work?
- [ ] What surprised us?
- [ ] What assumptions were validated/invalidated?

**Example**: "Learned that the method works but only for balanced classes. Assumption that it would work for imbalanced data was wrong."

---

### 2. What Surprised Us?

Surprises often indicate:
- New directions to explore
- Flawed initial assumptions
- Hidden complexity
- Unexpected opportunities

**Example**: "Surprised that simple baseline outperformed complex method. This suggests the problem might be easier than thought, or we're overcomplicating."

---

### 3. What Would We Do Differently?

Reflection helps avoid repeating mistakes and identifies improvements.

**Example**: "Would start with larger toy dataset (100 vs 20 samples) to get more stable results. Also would test on multiple random seeds from the start."

---

### 4. Is the Idea Worth More Investment?

Consider:
- **Potential impact**: If this works, how valuable is it?
- **Feasibility**: How hard is it to make this work?
- **Uniqueness**: Is this a new idea or reinventing the wheel?
- **Interest**: Are you still excited about this?

**Scoring** (1-5 for each):
- Impact: [1-5]
- Feasibility: [1-5]
- Uniqueness: [1-5]
- Interest: [1-5]

**Total**: 12+ suggests continue, 8-11 suggests iterate, <8 suggests park.

---

## Time-Based Decisions

### Checkpoint Strategy

Set checkpoints during the bet:

| Time | Checkpoint Question | Action if Failing |
|------|---------------------|-------------------|
| 25% | Is data generation working? | Fix or pivot |
| 50% | Is method running? | Simplify or pivot |
| 75% | Do we have preliminary results? | Document and park if nothing |
| 100% | Make final decision | Use decision framework |

### When to Stop Early

Stop before time is up if:
- ✅ You've answered the core question (even if negative)
- ✅ You've hit a fundamental blocker that can't be fixed quickly
- ✅ You've discovered the idea isn't worth pursuing
- ✅ You've learned enough to make a decision

**Don't stop early if**:
- ❌ You're just frustrated (take a break, come back)
- ❌ Results are unclear (gather more info)
- ❌ Method needs debugging (that's part of the process)

### When to Extend

Rarely extend, but consider if:
- ✅ You're very close to answering the question (< 30 min away)
- ✅ You've found something exciting and want to verify
- ✅ A small extension would yield much more information

**Don't extend if**:
- ❌ You're just trying to "finish" (document what you have)
- ❌ You're optimizing prematurely
- ❌ You're avoiding making a decision

---

## Post-Mortem Template

After each bet, quickly answer:

### Quick Retrospective

1. **Time spent**: [Actual] vs [Budget]
2. **Question answered**: [Yes/Partially/No]
3. **Key finding**: [One sentence]
4. **Decision**: [Continue/Pivot/Park]
5. **Next action**: [Specific next step]

### Deeper Reflection (if bet was significant)

1. **What assumptions were wrong?**
2. **What would have saved time?**
3. **What should we remember for future bets?**
4. **What new ideas did this spawn?**

---

## Idea Evolution

### How to Refine Based on Results

**If continuing**:
- Make hypothesis more specific
- Increase dataset size
- Test on real data
- Add more sophisticated method components

**If pivoting**:
- Change the question (but keep domain)
- Try different approach to same question
- Simplify the problem
- Focus on a sub-problem

**If parking**:
- Document why it didn't work
- Note conditions that might make it worth revisiting
- Extract any reusable components/learnings

### When to Spawn New Ideas

Spawn new ideas when:
- ✅ You discovered something unexpected
- ✅ A side effect is more interesting than main result
- ✅ You identified a related but different question
- ✅ You found a new application domain

**Add to ideas inbox** with:
- Brief description
- Why it's interesting
- Quick test idea
- Priority (high/medium/low)

### How to Combine Insights

Multiple bets can combine into larger insights:

1. **Pattern recognition**: "All my network bets show that topology matters"
2. **Meta-learning**: "Methods that work on synthetic data don't work on real data"
3. **Domain understanding**: "This problem is harder/easier than I thought"

Document these insights separately—they're valuable.

---

## Decision Matrix

| Result Category | Signal Strength | Next Step | Time Investment |
|----------------|-----------------|-----------|-----------------|
| 🔥 Exciting | Strong | Continue | 4-8 hours |
| ✅ Promising | Moderate | Iterate | 2-4 hours |
| 🤔 Unclear | Weak | Pivot | 1-2 hours |
| ❌ Dead End | None | Park | 0 hours |
| 💡 Pivot | Different | New Bet | 2-4 hours |

---

## Examples

### Example 1: Exciting → Continue

**Bet**: "Does method X work for problem Y?"
**Result**: 95% accuracy on toy data (target was 70%)
**Finding**: Method works exceptionally well, robust across seeds
**Decision**: Continue
**Next Step**: Test on real dataset (1000 samples), compare to baselines

---

### Example 2: Promising → Iterate

**Bet**: "Is there an effect of X on Y?"
**Result**: Effect size = 0.3 ± 0.2 (detectable but noisy)
**Finding**: Effect exists but needs more data to confirm
**Decision**: Iterate
**Next Step**: Increase sample size to 500, reduce noise

---

### Example 3: Unclear → Pivot

**Bet**: "Does network topology affect convergence?"
**Result**: Results vary wildly (std = 0.4) across random seeds
**Finding**: Too much variance, can't draw conclusion
**Decision**: Pivot
**Next Step**: Try different question—maybe initial conditions matter more?

---

### Example 4: Dead End → Park

**Bet**: "Can we generate synthetic data for domain X?"
**Result**: Generated data doesn't capture key properties
**Finding**: Fundamental mismatch between synthetic and real data
**Decision**: Park
**Next Step**: Move to next idea, note that synthetic data generation is hard for this domain

---

### Example 5: Pivot → New Bet

**Bet**: "Does method A work better than method B?"
**Result**: Methods are equivalent, but discovered method C is much faster
**Finding**: Speed matters more than accuracy for this use case
**Decision**: New Bet
**Next Step**: Create new bet: "Is method C fast enough for real-time use?"

---

## Remember

- **No bet is wasted**: Even failures teach you something
- **Document everything**: Future you will thank present you
- **Time-boxing forces decisions**: Don't let perfect be the enemy of done
- **Compound learning**: Each bet builds intuition
- **Action over analysis**: Make a decision and move forward

> "The goal isn't to be right every time—it's to learn quickly and compound that learning."
