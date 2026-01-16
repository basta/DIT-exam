---
id: drs_039
course: Dynamics and Control of Networks
tags: [structural-balance, clusterable-networks, signed-graphs]
difficulty: 3
type: open
status: to_learn

---
# Question
Show by counterexample that a clusterable network need not be structurally balanced.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A signed complete graph with 3 nodes ($K_3$) where all three edges are negative.

## Explanation
In the study of signed graphs (graphs where edges are labeled as positive $+$ or negative $-$), a network is **structurally balanced** (according to Heider's theory) if every cycle has an even number of negative edges. This implies the nodes can be partitioned into two sets such that all edges within each set are positive and all edges between the sets are negative.

A network is **clusterable** (according to Davis's theory) if it can be partitioned into $k$ clusters such that all edges within clusters are positive and all edges between different clusters are negative. 

Every structurally balanced network is clusterable (where $k=1$ or $k=2$), but the converse is not true. Structural balance is a stricter condition because it prohibits a specific type of cycle: the all-negative triangle. In a clusterable network, an all-negative triangle is perfectly acceptable because it implies that each of the three nodes belongs to a distinct cluster (i.e., they all dislike each other). However, in a structurally balanced network, an all-negative triangle is "unbalanced" because it violates the "friend of my enemy is my enemy" logic or the requirement that a partition into only two groups exists.

By providing a network with an all-negative cycle of length 3, we demonstrate a graph that is clusterable into three groups ($n_1=\{v_1\}, n_2=\{v_2\}, n_3=\{v_3\}$) but fails the criteria for structural balance.

### Steps / Derivation
1. **Define the Counterexample:** Consider a signed complete graph $G = (V, E)$ with three nodes $V = \{1, 2, 3\}$.
2. **Assign Edge Weights:** Let all edges be negative:
   $$ e_{12} = -, \quad e_{23} = -, \quad e_{31} = - $$
3. **Test for Structural Balance:** A graph is balanced if and only if the product of signs in every cycle is positive. For this triangle:
   $$ (-1) \times (-1) \times (-1) = -1 $$
   Since the product is negative, the graph is **not** structurally balanced.
4. **Test for Clusterability:** A graph is clusterable if there are no cycles containing exactly one negative edge. In our triangle, the number of negative edges is 3. Since there are no cycles with exactly one negative edge (all cycles here have 3), the graph is **clusterable**.
5. **Conclusion:** We have found a partition $C_1 = \{1\}, C_2 = \{2\}, C_3 = \{3\}$ where all within-cluster edges are positive (vacuously true) and all between-cluster edges are negative. Thus, the network is clusterable but not balanced.

## Related Concepts
- [[structural_balance_theory]]
- [[harary_balance_theorem]]
- [[signed_graph_clustering]]