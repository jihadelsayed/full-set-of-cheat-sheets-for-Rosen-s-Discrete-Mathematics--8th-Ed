**📘 Chapter 8: Advanced Counting Techniques**

------------------------------------------------------------------------

**🔁 8.1 Recurrence Relations**

A **recurrence relation** defines a sequence based on earlier terms.

**Example:**

- Fibonacci:\
  F(n) = F(n−1) + F(n−2), with F(0) = 0, F(1) = 1

**Linear Homogeneous Recurrence:**

- Form:\
  aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + \... + cₖaₙ₋ₖ

------------------------------------------------------------------------

**🧠 8.2 Solving Linear Recurrence Relations**

**1. Characteristic Equation Method**

For homogeneous linear recurrences:

- Example:\
  aₙ = 3aₙ₋₁ − 2aₙ₋₂\
  → Solve r² − 3r + 2 = 0

**General solution:**

- Based on roots of the characteristic equation:

  - Distinct roots → aₙ = A·r₁ⁿ + B·r₂ⁿ

  - Repeated roots → include n multipliers (e.g., n·rⁿ)

------------------------------------------------------------------------

**🎯 8.3 Divide-and-Conquer Recurrences**

Used in algorithm analysis.

**Example:**

- Merge Sort: T(n) = 2T(n/2) + n

- Use **recursion tree** or **Master Theorem** to solve.

**Master Theorem (Simplified Form):**

For T(n) = aT(n/b) + f(n):

- If f(n) = O(n\^log_b a−ε) → T(n) = Θ(n\^log_b a)

- If f(n) = Θ(n\^log_b a) → T(n) = Θ(n\^log_b a · log n)

- If f(n) = Ω(n\^log_b a+ε) and regularity holds → T(n) = Θ(f(n))

------------------------------------------------------------------------

**🧮 8.4 Generating Functions (Intro Level)**

- Encodes sequences as power series:

  - For sequence a₀, a₁, a₂, ... →\
      G(x) = a₀ + a₁x + a₂x² + ...

Helps solve recurrences, count combinations.

------------------------------------------------------------------------

**📊 8.5 Inclusion-Exclusion Principle**

Used to count elements in overlapping sets.

**Formula:**

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

For 3 sets: P(A ∪ B ∪ C) = P(A) + P(B) + P(C)\
  − P(A ∩ B) − P(A ∩ C) − P(B ∩ C)\
  + P(A ∩ B ∩ C)

------------------------------------------------------------------------

**🧩 8.6 Applications: Counting Derangements**

- Derangement: permutation where no item is in its original place.

**Number of derangements of n:**

!n = n! × (1 − 1/1! + 1/2! − 1/3! + \... + (−1)ⁿ / n!)
