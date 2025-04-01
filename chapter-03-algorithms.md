**📘 Chapter 3: Algorithms**

------------------------------------------------------------------------

**⚙️ 3.1 What is an Algorithm?**

- **Algorithm**: A finite, step-by-step procedure for solving a problem.

- Must be:

  - **Input-defined**

  - **Output-defined**

  - **Definite (clear steps)**

  - **Effective (can be computed)**

  - **Finite (must end)**

------------------------------------------------------------------------

**💻 3.2 Pseudocode Basics**

- High-level representation of an algorithm (not actual code).

- Example:

css

CopyEdit

Algorithm Max(A\[1..n\])

max ← A\[1\]

for i ← 2 to n

if A\[i\] \> max then

max ← A\[i\]

return max

------------------------------------------------------------------------

**🔢 3.3 Algorithm Analysis (Time Complexity)**

- Measure time using **basic operations** (e.g., comparisons).

- Express growth with **Big-O notation**.

**🧠 3.4 Big-O Notation**

Describes upper-bound growth rate:

- O(1): Constant time

- O(log n): Logarithmic

- O(n): Linear

- O(n log n): Linearithmic

- O(n²): Quadratic

- O(2ⁿ): Exponential

✅ **f(n) is O(g(n))** if ∃ c, n₀ such that for all n \> n₀:\
  f(n) ≤ c \* g(n)

------------------------------------------------------------------------

**⚖️ 3.5 Big-Omega (Ω) & Big-Theta (Θ)**

- **Ω(g(n))**: Lower bound

- **Θ(g(n))**: Tight bound (both upper and lower)

------------------------------------------------------------------------

**📈 3.6 Complexity of Common Algorithms**

  -----------------------------------------------------------------------
  **Algorithm**                                  **Time Complexity**
  ---------------------------------------------- ------------------------
  Linear Search                                  O(n)

  Binary Search                                  O(log n)

  Bubble Sort                                    O(n²)

  Merge Sort                                     O(n log n)

  Quick Sort (avg)                               O(n log n)

  Quick Sort (worst)                             O(n²)
  -----------------------------------------------------------------------
