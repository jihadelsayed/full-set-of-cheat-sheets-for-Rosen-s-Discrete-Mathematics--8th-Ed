**📘 Chapter 12: Boolean Algebra**

------------------------------------------------------------------------

**🔣 12.1 Boolean Functions and Logic Gates**

- **Boolean variables**: take values 0 (false) or 1 (true)

**Basic Gates:**

  ------------------------------------------------------------------------
  **Gate**      **Symbol**           **Operation**
  ------------- -------------------- -------------------------------------
  AND           ⋅                    x AND y → x⋅y

  OR            \+                   x OR y → x + y

  NOT           ¬                    NOT x → ¬x

  XOR           ⊕                    x XOR y → x ⊕ y
  ------------------------------------------------------------------------

------------------------------------------------------------------------

**🧠 12.2 Identities in Boolean Algebra**

- **Identity laws**:

  - x + 0 = x

  - x ⋅ 1 = x

- **Domination**:

  - x + 1 = 1

  - x ⋅ 0 = 0

- **Complement**:

  - x + ¬x = 1

  - x ⋅ ¬x = 0

- **Double Negation**:

  - ¬(¬x) = x

- **De Morgan's Laws**:

  - ¬(x ⋅ y) = ¬x + ¬y

  - ¬(x + y) = ¬x ⋅ ¬y

------------------------------------------------------------------------

**🧮 12.3 Simplification Techniques**

- Use **Boolean identities** to reduce expressions

- Can also use **truth tables** to verify equivalence

------------------------------------------------------------------------

**🛠️ 12.4 Karnaugh Maps (K-Maps)**

- Visual method to simplify Boolean expressions

- Plot 1's in a truth table grid

- Group 1s in powers of 2 (1, 2, 4, 8, \...)

- Write minimized expression from grouped terms

------------------------------------------------------------------------

**🔗 12.5 Logic Circuits**

- Build circuits from Boolean expressions (or vice versa)

- Circuit → expression = **trace gate connections**

- Expression → circuit = **use AND, OR, NOT gates**

------------------------------------------------------------------------

**🧠 12.6 Adders & Multiplexers (Optional Section)**

- **Half Adder**: adds two bits → outputs sum & carry

- **Full Adder**: adds two bits and carry-in

- **Multiplexer (MUX)**: selects one input from many based on select
  lines
