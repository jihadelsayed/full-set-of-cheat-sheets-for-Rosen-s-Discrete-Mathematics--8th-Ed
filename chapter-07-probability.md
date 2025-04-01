**📘 Chapter 7: Discrete Probability**

------------------------------------------------------------------------

**🎲 7.1 Introduction to Probability**

**Sample Space (S):**

- Set of all possible outcomes.

**Event (E):**

- Subset of sample space.

**Probability of E:**

- P(E) = \|E\| / \|S\| (if outcomes are equally likely)

------------------------------------------------------------------------

**🧠 7.2 Probability Rules**

- 0 ≤ P(E) ≤ 1

- P(∅) = 0, P(S) = 1

- P(Eᶜ) = 1 - P(E)

- P(E ∪ F) = P(E) + P(F) - P(E ∩ F)

- If E and F are disjoint:\
    P(E ∪ F) = P(E) + P(F)

------------------------------------------------------------------------

**🔗 7.3 Conditional Probability**

- P(E \| F) = P(E ∩ F) / P(F)\
    (Probability of E given F happened)

**Independent Events:**

- E and F are independent if:\
    P(E ∩ F) = P(E) × P(F)

------------------------------------------------------------------------

**🧪 7.4 Bayes' Theorem**

- P(A \| B) = \[P(B \| A) × P(A)\] / P(B)

**Useful when:**

- You know P(B \| A) but need P(A \| B)

- Used heavily in AI, spam filters, etc.

------------------------------------------------------------------------

**🎯 7.5 Expected Value (Mean)**

- E\[X\] = ∑ \[xᵢ × P(xᵢ)\]\
  (weighted average of outcomes)

**Example:**

If X = outcome of rolling a die:\
E\[X\] = (1+2+3+4+5+6)/6 = 3.5
