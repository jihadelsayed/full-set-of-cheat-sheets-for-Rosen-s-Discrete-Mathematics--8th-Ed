**📘 Discrete Math Cheat Sheet -- Rosen 8th Edition**

**📍 CHAPTER 1: Logic and Proofs**

**🧠 1.1 Propositional Logic**

- **Proposition**: A statement that\'s either *true (T)* or *false (F)*.

- **Logical Operators**:

  - ¬p: NOT p

  - p ∧ q: p AND q

  - p ∨ q: p OR q

  - p → q: IF p THEN q (implication)

  - p ↔ q: p IF AND ONLY IF q (biconditional)

**🧾 Truth Table Sample:**

  ----------------------------------------------------------------------------
  **p**   **q**   **p ∧ q**        **p ∨ q**        **p → q**        **¬p**
  ------- ------- ---------------- ---------------- ---------------- ---------
  T       T       T                T                T                F

  T       F       F                T                F                F

  F       T       F                T                T                T

  F       F       F                F                T                T
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

**🧠 1.2 Applications of Propositional Logic**

- **Logic Puzzles**

- **Bit Operations**: Bitwise AND, OR, NOT

------------------------------------------------------------------------

**🧠 1.3 Propositional Equivalences**

- **Laws**:

  - **De Morgan\'s**:

    - ¬(p ∧ q) ≡ ¬p ∨ ¬q

    - ¬(p ∨ q) ≡ ¬p ∧ ¬q

  - **Double Negation**: ¬(¬p) ≡ p

  - **Implication**: p → q ≡ ¬p ∨ q

------------------------------------------------------------------------

**🧠 1.4 Predicates and Quantifiers**

- **Predicate**: A statement with variables (e.g., P(x): x is even)

- **Quantifiers**:

  - ∀x P(x): \"For all x, P(x)\"

  - ∃x P(x): \"There exists an x such that P(x)\"

------------------------------------------------------------------------

**🧠 1.6 Methods of Proof**

- **Direct Proof**: Assume hypothesis, prove conclusion

- **Contrapositive**: Prove ¬q → ¬p instead of p → q

- **Contradiction**: Assume statement is false, show contradiction

- **Proof by Cases**: Split into multiple cases, prove each

------------------------------------------------------------------------

**🧠 1.7 Proof Strategy**

1.  Understand the theorem.

2.  Write what is **given** and what to **prove**.

3.  Choose method: direct, contradiction, contrapositive, cases.

4.  Write clear steps, justify each.

5.  End with \"∴ QED\" (optional but looks pro 😎).
