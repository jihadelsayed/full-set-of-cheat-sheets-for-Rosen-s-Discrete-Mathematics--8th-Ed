**📘 Chapter 11: Trees**

------------------------------------------------------------------------

**🌳 11.1 Introduction to Trees**

- **Tree**: A connected graph with **no cycles**

- **Rooted Tree**: One designated root; every edge directs away from it

- **Leaf**: Node with no children

- **Internal Node**: Has at least one child

- **Subtree**: Tree formed from a node and its descendants

------------------------------------------------------------------------

**🧠 11.2 Terminology & Properties**

- **Height**: Longest path from root to a leaf

- **Level**: Distance from the root

- **Binary Tree**: Max 2 children per node

- **Full Binary Tree**: Every node has 0 or 2 children

- **Complete Binary Tree**: All levels full except possibly last, filled
  left to right

------------------------------------------------------------------------

**➕ 11.3 Tree Traversals**

- **Preorder**: Visit root → Left → Right

- **Inorder**: Left → Root → Right

- **Postorder**: Left → Right → Root

- **Level-order**: Breadth-first (use queue)

------------------------------------------------------------------------

**🧩 11.4 Binary Search Trees (BST)**

- Left subtree \< Root \< Right subtree

- Efficient for search, insert, delete:\
   **Average time**: O(log n), **Worst-case**: O(n)

**🌐 11.5 Applications of Trees**

- **Expression Trees**: parse arithmetic/logical expressions

- **File Systems**

- **Decision Trees** (AI)

- **Tries** (search prefixes)

------------------------------------------------------------------------

**⚙️ 11.6 Spanning Trees & Minimum Spanning Trees (MST)**

- **Spanning Tree**: Connects all vertices with no cycles

- **Minimum Spanning Tree**: Spanning tree with minimum edge weights

**Algorithms:**

- **Kruskal's Algorithm**: Greedy, adds smallest edge that doesn't form
  a cycle

- **Prim's Algorithm**: Greedy, builds MST from a starting node
