# NumPy — Core Numerical Computing Foundations

This folder contains structured experiments and code snippets created while
learning **NumPy**, with an emphasis on *how and why* NumPy works rather than
surface-level syntax.

The focus is on building intuition for array-based computation, memory layout,
and vectorized thinking — skills that directly translate to data science,
machine learning, and scientific computing workflows.

---

## What I Covered

### 1. Array Creation & Data Types
- Creating arrays from Python lists and ranges
- Understanding `dtype` and why it matters
- Type casting and precision trade-offs
- Differences between Python lists and NumPy arrays

**Key insight:** performance gains come from homogeneous, contiguous memory.

---

### 2. Array Shape, Dimensions & Axes
- `ndim`, `shape`, `size`
- Reshaping arrays and when it is a view vs a copy
- Axis-based thinking (rows vs columns)
- Common mistakes with axis interpretation

**Key insight:** most bugs come from misunderstanding axes, not syntax.

---

### 3. Indexing & Slicing
- Basic slicing vs advanced indexing
- Boolean masks and conditional selection
- Views vs copies and their side effects
- Modifying arrays in-place safely

**Key insight:** slicing usually returns views; advanced indexing returns copies.

---

### 4. Broadcasting Rules
- How NumPy aligns arrays of different shapes
- Broadcasting mechanics step-by-step
- Writing code without explicit loops
- When broadcasting silently fails or explodes memory

**Key insight:** broadcasting is a shape-alignment algorithm, not magic.

---

### 5. Vectorization & Performance
- Replacing Python loops with vectorized operations
- Element-wise vs aggregate operations
- Why vectorized code is faster (C-level execution)
- Time comparisons between loops and vectorized solutions

**Key insight:** performance comes from *fewer Python instructions*, not clever math.

---

### 6. Universal Functions (ufuncs)
- Element-wise operations (`add`, `multiply`, `sqrt`, etc.)
- Reduction operations (`sum`, `mean`, `std`)
- Chaining ufuncs efficiently
- Numerical stability considerations

---

### 7. Aggregation & Statistics
- Axis-aware aggregations
- Difference between global and axis-wise operations
- Handling missing values (`NaN`)
- Practical statistical summaries for datasets

---

### 8. Linear Algebra Basics
- Dot product vs element-wise multiplication
- Matrix multiplication and shape compatibility
- Transpose and its effect on dimensions
- Solving simple linear systems

---

### 9. Random Module
- Generating reproducible random data
- Distributions commonly used in ML
- Setting seeds and why reproducibility matters
- Simulating data for experiments

---

## How This Repo Is Organized
- Each file/notebook focuses on **one concept**
- Experiments are small and isolated
- Code prioritizes clarity over cleverness
- Comments explain *why* something behaves a certain way

---

## Why This Matters for ML & Data Science
NumPy forms the computational backbone of:
- Pandas
- scikit-learn
- PyTorch / TensorFlow (at a conceptual level)

Understanding NumPy deeply makes higher-level libraries predictable rather than opaque.

---

## Current Status
This is a **learning-focused repository**, not a production library.
Concepts are revisited and refined as understanding improves.

Future additions may include:
- Memory layout experiments
- Strides and views
- Numerical precision edge cases

---
