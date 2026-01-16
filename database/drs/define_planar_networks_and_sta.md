---
id: drs_011
course: Dynamics and Control of Networks
tags: [graph-theory, topology, planar-graphs, vertex-coloring]
difficulty: 2
type: open
status: to_learn
---

# Question
Define planar networks and state the "four color" theorem.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A planar network is a graph that can be embedded in the plane without edges crossing; the Four Color Theorem states that any such graph can be colored with at most four colors such that no two adjacent vertices share the same color.

## Explanation
In the study of network dynamics and topology, a **planar network** (or planar graph) is defined as a graph $G = (V, E)$ that can be drawn in a two-dimensional plane $\mathbb{R}^2$ such that its edges intersect only at their endpoints (the vertices). This property is purely topological; a graph may be drawn with crossings in one instance but still be considered "planar" if there exists at least one mapping where no edges cross. Planarity is often characterized by **Kuratowski's Theorem**, which states that a graph is planar if and only if it does not contain a subgraph that is a subdivision of the complete graph $K_5$ or the complete bipartite graph $K_{3,3}$. Planar networks are critical in physical infrastructure modeling, such as integrated circuit design and urban road networks, where physical crossings are costly or impossible.

The **Four Color Theorem** is one of the most famous results in graph theory. It asserts that, given any separation of a plane into contiguous regions (forming a map), the regions can be colored using at most four colors so that no two adjacent regions have the same color. Translated into network terms, it states that the vertices of any planar graph can be assigned a color from a set of four colors such that no two vertices connected by an edge share the same color (this is known as the chromatic number $\chi(G) \leq 4$). Originally proposed in 1852 by Francis Guthrie, it was famously the first major theorem to be proved using a computer (by Appel and Haken in 1976), as it required checking 1,936 specific configurations.

### Steps / Derivation
1. **Definition of Planarity**: A graph $G$ is planar if there exists an embedding $\phi: G \to \mathbb{R}^2$ such that for all distinct edges $e_1, e_2 \in E$, $\phi(e_1) \cap \phi(e_2) \subseteq \phi(V)$.
2. **Euler's Formula**: For a connected planar graph with $V$ vertices, $E$ edges, and $F$ faces:
$$
V - E + F = 2
$$
3. **Four Color Statement**: For a planar graph $G$, the chromatic number $\chi(G)$ satisfies:
$$
\chi(G) \leq 4
$$

## Related Concepts
- [[chromatic_number]]
- [[euler_characteristic]]
- [[kuratowski_theorem]]