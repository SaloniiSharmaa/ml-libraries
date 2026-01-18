# Pandas — Data Manipulation & Analysis Foundations

This folder contains structured experiments and code snippets created while
learning **Pandas**, with a focus on understanding *how tabular data is modeled,
indexed, and transformed* in real-world data workflows.

The emphasis is on building intuition for DataFrames as **labeled, column-oriented
data structures built on top of NumPy**, rather than treating Pandas as a black box.

---

## What I Covered

### 1. Series vs DataFrame
- Creating Series and DataFrames from different sources
- Understanding labels, indices, and alignment
- Differences between 1D and 2D data structures
- When to use each and why

**Key insight:** Pandas operations are label-aware, not position-first.

---

### 2. Indexing & Selection
- Column selection and row slicing
- `loc` vs `iloc` and when each is appropriate
- Boolean indexing and conditional filtering
- Common indexing pitfalls and silent errors

**Key insight:** most Pandas bugs come from index confusion, not syntax.

---

### 3. Data Cleaning & Missing Values
- Detecting missing data (`isna`, `notna`)
- Dropping vs imputing values
- Type conversions and inconsistent data
- Cleaning messy, real-world datasets

**Key insight:** data cleaning is a modeling decision, not a preprocessing afterthought.

---

### 4. Vectorized Operations & Column-wise Logic
- Applying functions across columns and rows
- Avoiding Python loops in favor of vectorized operations
- Chained operations and readability trade-offs

---

### 5. GroupBy & Aggregation
- Split–apply–combine mental model
- Aggregations across groups
- Multi-level grouping
- Practical use cases (summaries, statistics)

**Key insight:** `groupby` is a declarative transformation pipeline, not a loop.

---

### 6. Merging & Joining
- `merge`, `join`, and `concat`
- Understanding keys and join types
- Handling mismatched or missing keys
- Common join mistakes

---

### 7. Basic Exploratory Analysis
- Descriptive statistics
- Sorting and filtering for insight
- Preparing data for visualization or modeling

---

## How This Folder Is Organized
- Each file or notebook focuses on **one core concept**
- Experiments are small, reproducible, and isolated
- Code prioritizes clarity and correctness over clever tricks
- Comments explain *why* operations behave the way they do

---

## Why This Matters for ML & Data Science
Pandas is the primary interface for:
- data ingestion
- cleaning and transformation
- feature preparation

A solid understanding of Pandas reduces friction when working with:
- scikit-learn
- visualization libraries
- real-world datasets that are imperfect by default

---

## Current Status
This is a **learning-focused repository**, not a production codebase.
Concepts are revisited and refined as understanding deepens.

Future additions may include:
- performance considerations
- memory usage patterns
- common anti-patterns in Pandas workflows

---
