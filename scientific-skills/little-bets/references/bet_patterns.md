# Common Little Bet Patterns

This document catalogs common experimental patterns for rapid prototyping. Each pattern includes a question template, code snippet, success criteria, and common pitfalls.

---

## 1. Method Validation Pattern

**Purpose**: Test if method X works at all for problem Y.

**Question Template**: "Does [method] work for [problem] using [simple case]?"

**When to Use**: You have a new method and want to verify it's not fundamentally broken.

**Code Pattern**:
```python
def create_toy_data():
    """Create data with known structure."""
    # Generate data where ground truth is recoverable
    X = np.random.randn(100, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)  # Known decision boundary
    return X, y

def test_method(X, y):
    """Simplest possible implementation."""
    model = SimpleClassifier()
    model.fit(X, y)
    accuracy = model.score(X, y)
    return accuracy

# Success: Should achieve > 90% on easy case
X, y = create_toy_data()
acc = test_method(X, y)
assert acc > 0.9, f"Method failed: {acc:.1%}"
```

**Success Criteria**:
- ✅ Method runs without errors
- ✅ Recovers known structure (accuracy > threshold)
- ✅ Produces reasonable outputs

**Common Pitfalls**:
- ❌ Making data too complex (defeats purpose)
- ❌ Testing on data method was designed for (circular)
- ❌ Not checking if ground truth is actually recoverable

---

## 2. Effect Size Estimation Pattern

**Purpose**: Quick bootstrap to determine if an effect is detectable.

**Question Template**: "Is there any detectable effect of [X] on [Y]?"

**When to Use**: You suspect an effect exists but don't know if it's large enough to matter.

**Code Pattern**:
```python
def estimate_effect_size(data, n_bootstrap=100):
    """Bootstrap to estimate effect size distribution."""
    effects = []
    
    for _ in range(n_bootstrap):
        # Resample with replacement
        sample = data.sample(n=len(data), replace=True)
        effect = compute_effect(sample)
        effects.append(effect)
    
    return {
        'mean': np.mean(effects),
        'std': np.std(effects),
        'ci_lower': np.percentile(effects, 2.5),
        'ci_upper': np.percentile(effects, 97.5)
    }

# Success: Effect size > 2*std (detectable)
result = estimate_effect_size(data)
detectable = abs(result['mean']) > 2 * result['std']
```

**Success Criteria**:
- ✅ Effect size > noise level (signal-to-noise > 2)
- ✅ Confidence interval doesn't include zero
- ✅ Effect is in expected direction

**Common Pitfalls**:
- ❌ Using too few bootstrap samples (< 50)
- ❌ Not checking for outliers skewing results
- ❌ Confusing statistical significance with practical significance

---

## 3. Feasibility Check Pattern

**Purpose**: Test if data can be obtained/generated before investing in full pipeline.

**Question Template**: "Can we obtain/generate [data type] for [use case]?"

**When to Use**: Before building infrastructure, verify data exists and is accessible.

**Code Pattern**:
```python
def check_data_feasibility():
    """Try to obtain small sample of data."""
    # Option 1: Try downloading
    try:
        data = download_sample(n_samples=10)
        return {'feasible': True, 'source': 'download', 'sample': data}
    except Exception as e:
        pass
    
    # Option 2: Try generating
    try:
        data = generate_sample(n_samples=10)
        return {'feasible': True, 'source': 'generation', 'sample': data}
    except Exception as e:
        pass
    
    # Option 3: Try manual collection
    manual_data = collect_manually(n_samples=5)
    if len(manual_data) > 0:
        return {'feasible': True, 'source': 'manual', 'sample': manual_data}
    
    return {'feasible': False, 'reason': 'No viable source found'}

result = check_data_feasibility()
assert result['feasible'], f"Data not feasible: {result.get('reason')}"
```

**Success Criteria**:
- ✅ Can obtain at least 5-10 examples
- ✅ Data format is usable
- ✅ Collection/generation time is reasonable

**Common Pitfalls**:
- ❌ Assuming full dataset will be as easy as sample
- ❌ Not checking data quality (just existence)
- ❌ Overlooking licensing/access restrictions

---

## 4. Baseline Establishment Pattern

**Purpose**: Measure naive baseline before trying advanced methods.

**Question Template**: "What does [simple method] achieve on [problem]?"

**When to Use**: Before implementing complex method, establish what you need to beat.

**Code Pattern**:
```python
def establish_baseline(X, y):
    """Test simplest possible approaches."""
    baselines = {}
    
    # Random baseline
    random_pred = np.random.randint(0, 2, len(y))
    baselines['random'] = accuracy_score(y, random_pred)
    
    # Majority class baseline
    majority = mode(y)[0]
    majority_pred = np.full(len(y), majority)
    baselines['majority'] = accuracy_score(y, majority_pred)
    
    # Simple heuristic (if applicable)
    heuristic_pred = simple_heuristic(X)
    baselines['heuristic'] = accuracy_score(y, heuristic_pred)
    
    return baselines

baselines = establish_baseline(X, y)
print(f"Random: {baselines['random']:.1%}")
print(f"Majority: {baselines['majority']:.1%}")
print(f"Heuristic: {baselines['heuristic']:.1%}")
# Your method needs to beat these!
```

**Success Criteria**:
- ✅ Have at least 2-3 baseline scores
- ✅ Understand what "good" means (e.g., > 70% accuracy)
- ✅ Baseline is reasonable (not trivially easy/hard)

**Common Pitfalls**:
- ❌ Using inappropriate baseline (e.g., random for imbalanced data)
- ❌ Not documenting baseline for future reference
- ❌ Comparing apples to oranges (different data splits)

---

## 5. Scaling Test Pattern

**Purpose**: Understand how method performance changes with scale.

**Question Template**: "Does [method] work at different scales (N=10, 100, 1000)?"

**When to Use**: Method works on small data, but will it scale?

**Code Pattern**:
```python
def test_scaling(method, scales=[10, 50, 100, 500]):
    """Test method at different data sizes."""
    results = []
    
    for n in scales:
        # Generate data of size n
        X, y = create_data(n_samples=n)
        
        # Time and run method
        start = time.time()
        result = method(X, y)
        elapsed = time.time() - start
        
        results.append({
            'n': n,
            'result': result,
            'time': elapsed,
            'time_per_sample': elapsed / n
        })
    
    return results

scaling_results = test_scaling(my_method)
for r in scaling_results:
    print(f"N={r['n']:4d}: {r['result']:.3f} in {r['time']:.2f}s ({r['time_per_sample']*1000:.1f}ms/sample)")
```

**Success Criteria**:
- ✅ Performance doesn't degrade catastrophically
- ✅ Runtime scales reasonably (O(n) or O(n log n))
- ✅ Method still works at target scale

**Common Pitfalls**:
- ❌ Testing only tiny scales (10, 20, 30)
- ❌ Not checking memory usage
- ❌ Assuming linear scaling continues indefinitely

---

## 6. Ablation Pattern

**Purpose**: Understand which components matter.

**Question Template**: "What happens if we remove [component X]?"

**When to Use**: Method works, but which parts are essential?

**Code Pattern**:
```python
def ablation_study(full_method, components):
    """Test method with each component removed."""
    results = {}
    
    # Full method
    results['full'] = full_method()
    
    # Remove each component
    for component in components:
        method_without = create_method_without(component)
        results[f'without_{component}'] = method_without()
    
    return results

components = ['feature_normalization', 'regularization', 'ensemble']
ablation = ablation_study(full_method, components)

for variant, score in ablation.items():
    diff = score - ablation['full']
    print(f"{variant:30s}: {score:.3f} ({diff:+.3f})")
```

**Success Criteria**:
- ✅ Identify critical vs. optional components
- ✅ Understand performance trade-offs
- ✅ Find minimal viable configuration

**Common Pitfalls**:
- ❌ Removing multiple components at once (confounding)
- ❌ Not checking if components interact
- ❌ Removing components that break the method

---

## 7. Comparison Pattern

**Purpose**: Quick A vs. B comparison.

**Question Template**: "Is [method A] better than [method B] on [problem]?"

**When to Use**: Choosing between two approaches.

**Code Pattern**:
```python
def compare_methods(method_a, method_b, X, y, n_trials=10):
    """Compare two methods with multiple trials."""
    scores_a = []
    scores_b = []
    
    for trial in range(n_trials):
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=trial
        )
        
        # Test method A
        model_a = method_a()
        model_a.fit(X_train, y_train)
        scores_a.append(model_a.score(X_test, y_test))
        
        # Test method B
        model_b = method_b()
        model_b.fit(X_train, y_train)
        scores_b.append(model_b.score(X_test, y_test))
    
    return {
        'method_a': {'mean': np.mean(scores_a), 'std': np.std(scores_a)},
        'method_b': {'mean': np.mean(scores_b), 'std': np.std(scores_b)},
        'difference': np.mean(scores_a) - np.mean(scores_b)
    }

comparison = compare_methods(method_a, method_b, X, y)
print(f"A: {comparison['method_a']['mean']:.3f} ± {comparison['method_a']['std']:.3f}")
print(f"B: {comparison['method_b']['mean']:.3f} ± {comparison['method_b']['std']:.3f}")
print(f"Difference: {comparison['difference']:+.3f}")
```

**Success Criteria**:
- ✅ Clear winner (difference > 2*std)
- ✅ Results are consistent across trials
- ✅ Difference is practically meaningful

**Common Pitfalls**:
- ❌ Not using same data splits for fair comparison
- ❌ Comparing on different metrics
- ❌ Drawing conclusions from single trial

---

## 8. Sensitivity Pattern

**Purpose**: Understand robustness to parameter changes.

**Question Template**: "How robust is [result] to changes in [parameter]?"

**When to Use**: Result looks good, but is it fragile?

**Code Pattern**:
```python
def sensitivity_analysis(method, param_name, param_values, X, y):
    """Test method across parameter range."""
    results = []
    
    for param_value in param_values:
        # Set parameter
        method.set_param(param_name, param_value)
        
        # Run method
        score = method.fit_score(X, y)
        
        results.append({
            'param_value': param_value,
            'score': score
        })
    
    return results

# Test sensitivity to regularization strength
lambda_values = [0.001, 0.01, 0.1, 1.0, 10.0]
sensitivity = sensitivity_analysis(
    method, 'lambda', lambda_values, X, y
)

for r in sensitivity:
    print(f"λ={r['param_value']:6.3f}: {r['score']:.3f}")
```

**Success Criteria**:
- ✅ Result is stable across reasonable parameter range
- ✅ Identify critical parameters (steep changes)
- ✅ Find robust parameter settings

**Common Pitfalls**:
- ❌ Testing too narrow parameter range
- ❌ Not checking if parameters interact
- ❌ Assuming robustness in one dimension means robustness overall

---

## Pattern Selection Guide

| Goal | Pattern | Time Estimate |
|------|---------|---------------|
| Verify method works | Method Validation | 30-60 min |
| Check if effect exists | Effect Size Estimation | 45-90 min |
| Can we get data? | Feasibility Check | 15-30 min |
| What to beat? | Baseline Establishment | 30-60 min |
| Will it scale? | Scaling Test | 60-120 min |
| What matters? | Ablation | 60-90 min |
| A vs. B? | Comparison | 45-90 min |
| Is it robust? | Sensitivity | 45-90 min |

---

## Combining Patterns

You can combine patterns in a single bet:

- **Baseline + Comparison**: Establish baseline, then compare new method
- **Method Validation + Scaling**: Verify it works, then test scaling
- **Feasibility + Baseline**: Check data exists, then establish baseline
- **Ablation + Sensitivity**: Find critical components, then test their parameters

Keep the total time under your budget (2-4 hours).
