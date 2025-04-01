**📘 Chapter 5: Induction and Recursion**

------------------------------------------------------------------------

**🔁 5.1 Mathematical Induction**

**🧱 Principle of Mathematical Induction:**

To prove a statement **P(n)** is true for all n ≥ n₀:

1.  **Base Case**: Show P(n₀) is true

2.  **Inductive Step**:

    - Assume P(k) is true (Inductive Hypothesis)

    - Prove P(k+1) is true using P(k)

✔️ If both hold → P(n) is true ∀ n ≥ n₀

------------------------------------------------------------------------

**✨ Example:**

Prove: 1 + 2 + \... + n = n(n + 1)/2

- Base: n = 1 → LHS = 1, RHS = 1(1+1)/2 = 1 ✔️

- Assume: P(k): 1 + 2 + \... + k = k(k + 1)/2

- Show: P(k+1):\
  LHS = \[1 + 2 + \... + k\] + (k+1)\
    = k(k + 1)/2 + (k + 1)\
    = (k + 1)(k + 2)/2 ✔️

------------------------------------------------------------------------

**🔂 5.2 Strong Induction**

- Same as normal induction, **but** in inductive step: Assume **P(n₀),
  P(n₀+1), \..., P(k)** are all true, then prove P(k+1)

------------------------------------------------------------------------

**🧮 5.3 Recursive Definitions**

**Recursive Set Example:**

- Define set of even numbers:

  - Base: 0 ∈ S

  - Rule: If x ∈ S → x + 2 ∈ S

**Recursive Function Example:**

Factorial:

- Base: 0! = 1

- Rule: n! = n × (n - 1)!

------------------------------------------------------------------------

**🔁 5.4 Solving Recurrences (optional deeper topic)**

- Often used in algorithm analysis:

  - Example: T(n) = 2T(n/2) + n → Merge Sort → T(n) = O(n log n)
