---
id: drs_013
course: Dynamics and Control of Networks
tags: [graph-theory, topology, path-finding]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a path and explain the difference between an Eulerian and a Hamiltonian path.

![[question_image.png]]

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
In graph theory, a path is a sequence of distinct vertices and edges connecting them. An Eulerian path visits every edge exactly once, while a Hamiltonian path visits every vertex exactly once.

## Explanation
In the study of network dynamics, understanding the traversal properties of a graph $G = (V, E)$ is fundamental. 

**1. Definition of a Path:**
A path is a sequence of vertices $(v_1, v_2, \dots, v_k)$ such that $v_i \in V$ and each consecutive pair $(v_i, v_{i+1})$ is connected by an edge $e \in E$. In a standard "simple" path, all vertices (and consequently all edges) must be distinct. The length of the path is defined by the number of edges, $k-1$.

**2. Eulerian Path:**
An Eulerian path is a trail in a graph which visits every **edge** exactly once. This concept originates from the Seven Bridges of Königsberg problem. For an undirected graph to possess an Eulerian path, it must be connected and have exactly zero or two vertices of odd degree. If all vertices have an even degree, the path is an Eulerian circuit (it starts and ends at the same vertex).

**3. Hamiltonian Path:**
A Hamiltonian path is a path in an undirected or directed graph that visits every **vertex** exactly once. Unlike the Eulerian path, which focuses on edges, the Hamiltonian path focuses on nodes. 

**Key Differences:**
The primary difference lies in the constraint of "complete coverage." The Eulerian path is edge-centric; it must exhaust the edge set $E$. The Hamiltonian path is vertex-centric; it must exhaust the vertex set $V$. From a computational complexity perspective, determining if a graph has an Eulerian path is "easy" (it can be done in polynomial time, $O(|E|)$), whereas determining if a graph contains a Hamiltonian path is a classic NP-complete problem.

### Steps / Derivation
1. Identify the Edge Set $E$ and Vertex Set $V$ of the graph.
2. Check Eulerian conditions:
$$
\text{deg}(v) \text{ is odd for at most two } v \in V
$$
3. Check Hamiltonian conditions: No simple necessary and sufficient algebraic condition exists for all graphs, but Dirac's Theorem provides a sufficient condition:
$$
\text{deg}(v) \geq \frac{n}{2} \text{ for all } v \in V
$$

## Related Concepts
- [[graph_traversal]]
- [[degree_distribution]]
- [[np_completeness]]