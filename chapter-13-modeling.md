**📘 Chapter 13: Modeling Computation**

------------------------------------------------------------------------

**⚙️ 13.1 Languages and Grammars**

- **Alphabet (Σ)**: finite set of symbols

- **String**: finite sequence of symbols

- **Language (L)**: set of strings over an alphabet

**Operations on Languages:**

- Union: L₁ ∪ L₂

- Concatenation: L₁L₂

- Kleene Star: L\* = {ε, w, ww, www, \...}

------------------------------------------------------------------------

**🔤 13.2 Finite-State Machines (FSM)**

- **Finite Automaton (FA)** = (Q, Σ, δ, q₀, F):\
   - Q = set of states\
   - Σ = alphabet\
   - δ = transition function\
   - q₀ = start state\
   - F = accepting states

- **Deterministic FA (DFA)**: exactly one transition per input/symbol

- **Nondeterministic FA (NFA)**: multiple transitions possible

✅ **NFA and DFA are equivalent** (can convert NFA → DFA)

------------------------------------------------------------------------

**🧠 13.3 Regular Expressions**

- Describe patterns in strings (like in grep, regex, etc.)

**Basic Building Blocks:**

- ε: empty string

- a: literal character

- - : union

- · : concatenation

- - : zero or more (Kleene star)

------------------------------------------------------------------------

**🔁 13.4 Turing Machines (TM)**

A Turing Machine is a theoretical model of a computer.

- TM = (Q, Σ, Γ, δ, q₀, B, F)\
   - Q: states\
   - Σ: input alphabet\
   - Γ: tape alphabet\
   - δ: transition function\
   - B: blank symbol\
   - F: final (accepting) states

✔️ Can **simulate any algorithm** → foundation of **what is computable**

------------------------------------------------------------------------

**⛔ 13.5 Limits of Computation**

- Some problems are **undecidable** --- no algorithm can solve them
  (e.g., the **Halting Problem**)

- **Halting Problem**: No general algorithm can decide whether a given
  TM halts on a given input

------------------------------------------------------------------------

**💡 Key Idea:**

"If a problem can be solved algorithmically, it can be solved by a
Turing Machine."
