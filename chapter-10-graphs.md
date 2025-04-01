**📘 Chapter 10: Graphs**

------------------------------------------------------------------------

**🔗 10.1 Graph Terminology**

- **Graph (G)**: G = (V, E), where\
   V = set of vertices (nodes)\
   E = set of edges (pairs of vertices)

- **Undirected**: edges have no direction

- **Directed (digraph)**: edges are ordered (arrows)

**Key Terms:**

- **Adjacent**: connected by an edge

- **Degree**: number of edges connected to a vertex

- **Loop**: edge that connects a vertex to itself

- **Simple Graph**: no loops or multiple edges

- **Multigraph**: may have multiple edges

------------------------------------------------------------------------

**🧭 10.2 Graph Representations**

- **Adjacency List**: maps each vertex to a list of neighbors

- **Adjacency Matrix**: a 2D array where A\[i\]\[j\] = 1 if edge exists

- **Incidence Matrix**: rows = vertices, columns = edges

------------------------------------------------------------------------

**🔄 10.3 Graph Isomorphism**

- Two graphs G₁ and G₂ are **isomorphic** if:  - Same number of vertices
  and edges\
   - Same connections (structure preserved)

------------------------------------------------------------------------

**🔁 10.4 Paths and Connectivity**

- **Path**: sequence of vertices with connecting edges

- **Simple Path**: no repeated vertices

- **Cycle**: starts and ends at same vertex

- **Connected**: path exists between every pair of vertices

- **Strongly Connected (digraph)**: path exists in **both** directions
  for every pair

------------------------------------------------------------------------

**🔍 10.5 Euler and Hamilton Paths**

- **Euler Path**: visits every **edge** exactly once\
   ✔️ Exists if 0 or 2 vertices have odd degree

- **Hamilton Path**: visits every **vertex** exactly once\
   (no simple test --- harder problem)

------------------------------------------------------------------------

**🧠 10.6 Dijkstra's Algorithm (Shortest Path)**

- Finds shortest path from a start node to all others (non-negative
  weights)

- Uses a priority queue (min-heap logic)

------------------------------------------------------------------------

**🌐 10.7 Weighted Graphs & Applications**

- **Weighted graph**: edges have weights (costs, distance, time, etc.)

- Applications:\
   ✔️ Routing\
   ✔️ Network optimization\
   ✔️ GPS/pathfinding

------------------------------------------------------------------------

**🧱 10.8 Trees (Intro)**

- A **tree** is a connected acyclic graph

- **Rooted tree**: one vertex is root, all edges flow away

- **Spanning Tree**: subgraph that connects all vertices with no cycles
