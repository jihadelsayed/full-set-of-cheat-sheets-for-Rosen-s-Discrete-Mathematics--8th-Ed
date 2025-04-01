**📘 Chapter 9: Relations**

------------------------------------------------------------------------

**🔗 9.1 Relations and Their Properties**

- A **relation** R from A to B: a subset of A × B (ordered pairs).

- A **relation on A** means R ⊆ A × A.

**Properties of Relations:**

- **Reflexive**: ∀a ∈ A, (a, a) ∈ R

- **Symmetric**: ∀a, b ∈ A, if (a, b) ∈ R → (b, a) ∈ R

- **Antisymmetric**: if (a, b) ∈ R and (b, a) ∈ R → a = b

- **Transitive**: if (a, b) ∈ R and (b, c) ∈ R → (a, c) ∈ R

------------------------------------------------------------------------

**🧩 9.2 Representing Relations**

- **Matrix Representation**:\
   - A 0/1 matrix where M\[i\]\[j\] = 1 if (aᵢ, aⱼ) ∈ R

- **Digraph (Directed Graph)**:\
   - Nodes represent elements, arrows show relations

------------------------------------------------------------------------

**🔁 9.3 Closures of Relations**

- **Reflexive Closure**: Add (a, a) for all a ∈ A

- **Symmetric Closure**: Add (b, a) for every (a, b) ∈ R

- **Transitive Closure**: Add (a, c) if (a, b) and (b, c) in R

🛠️ **Warshall's Algorithm**: Used to compute the transitive closure
(matrix-based)

------------------------------------------------------------------------

**📦 9.4 Equivalence Relations**

- A relation that is:\
   ✔️ Reflexive\
   ✔️ Symmetric\
   ✔️ Transitive

→ Partitions the set into **equivalence classes**

------------------------------------------------------------------------

**🧱 9.5 Partial Orderings**

- A **partial order** is a relation that is:\
   ✔️ Reflexive\
   ✔️ Antisymmetric\
   ✔️ Transitive

**Hasse Diagrams:**

- Visual representation of a partial order (omit loops/arrows implied by
  transitivity)

------------------------------------------------------------------------

**🏗️ 9.6 Lattices (optional in some courses)**

- A **lattice** is a poset where every pair of elements has:  - A
  **least upper bound** (join)\
   - A **greatest lower bound** (meet)
