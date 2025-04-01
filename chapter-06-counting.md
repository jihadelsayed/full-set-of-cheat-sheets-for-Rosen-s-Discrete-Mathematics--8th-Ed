**📘 Chapter 6: Counting**

------------------------------------------------------------------------

**🧮 6.1 Basics of Counting**

**Rule of Sum (Addition Principle):**

If A can happen in *m* ways and B in *n* ways (and they can\'t both
happen), total = m + n

**Rule of Product (Multiplication Principle):**

If A can happen in *m* ways, and B in *n* ways **after** A, total = m ×
n

------------------------------------------------------------------------

**♻️ 6.2 Permutations**

**Without Repetition:**

- n! = n × (n - 1) × \... × 1

- Example: 3 elements → 3! = 6 permutations

**With Repetition:**

- If n items, with groups of duplicates:\
  n! / (k₁! × k₂! × \... × kᵣ!)\
  (used when you have repeated elements like in "MISSISSIPPI")

------------------------------------------------------------------------

**📦 6.3 Combinations**

**n Choose r:**

- C(n, r) = n! / \[r!(n - r)!\]

- Order **doesn\'t** matter

"How many ways can I choose r items from n without caring about order?"

------------------------------------------------------------------------

**📊 6.4 Binomial Theorem**

- (x + y)ⁿ = ∑ C(n, k) xⁿ⁻ᵏ yᵏ, for k = 0 to n

- Coefficients = Pascal's Triangle

**Example:**

(x + y)³ =\
C(3,0)x³ + C(3,1)x²y + C(3,2)xy² + C(3,3)y³\
= x³ + 3x²y + 3xy² + y³

------------------------------------------------------------------------

**🧠 6.5 Generalized Permutations and Combinations**

- **r-permutations with repetition**: nʳ

- **r-combinations with repetition**:\
   C(n + r - 1, r)

------------------------------------------------------------------------

**🎲 6.6 Pigeonhole Principle**

- If you put *n* items into *k* boxes and *n \> k*, then at least one
  box has **≥ 2 items**.

**Strong version:**

At least ⌈n/k⌉ items in one box
