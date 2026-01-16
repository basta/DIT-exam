---
id: drs_066
course: Dynamics and Control of Networks
tags: [graph-partitioning, community-detection, combinatorial-optimization]
difficulty: 3
type: open
status: to_learn

---
# Question
Describe the Kernighan-Lin algorithm for graph partitioning. What is its computational complexity? What is roughly the size of the network for which it can be reasonably expected to work?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** 
The Kernighan-Lin (KL) algorithm is a heuristic, iterative search algorithm for the balanced bisection of a graph. Its complexity is approximately $O(n^2 \log n)$ (or $O(n^3)$ depending on implementation), and it is effective for networks up to a few thousand nodes.

## Explanation
The Kernighan-Lin algorithm is one of the foundational methods in graph partitioning, originally designed for electronic circuit layout to minimize the number of connections between physical boards. It addresses the $min$-cut problem with a constraint on cluster sizes: given a graph $G = (V, E)$, it seeks to divide the vertices into two disjoint sets $A$ and $B$ of equal size (or a pre-specified ratio) such that the sum of the weights of the edges crossing between $A$ and $B$ is minimized.

The algorithm operates by starting with an initial random partition of the nodes into sets $A$ and $B$. It then iteratively identifies pairs of nodes—one from $A$ and one from $B$—that, if swapped, would result in the greatest reduction (or smallest increase) in the cut size. Unlike a purely greedy algorithm, KL records a sequence of swaps even if a swap temporarily increases the cut cost. After all nodes have been "locked" into a suggested swap, the algorithm looks back through the sequence of $n/2$ swaps and identifies the point where the cumulative reduction in cut size was at its maximum. This state becomes the starting point for the next pass. The algorithm continues until no further improvement can be found in a pass.

While the KL algorithm is significantly better at avoiding local minima than simple greedy swapping, it is still a heuristic and does not guarantee a global optimum. 

### Steps / Derivation
1. **Initialization:** Partition the set of nodes into two sets $A$ and $B$ such that $|A| = |B| = n/2$.
2. **Compute Gains:** For each pair $(a, b)$ where $a \in A, b \in B$, calculate the gain $g = D_a + D_b - 2w_{ab}$, where $D_i$ is the difference between external and internal edge weights for node $i$.
3. **Sequential Swapping:** Find the pair $(a_i, b_i)$ that maximizes the gain, record it, and temporarily "lock" these nodes. Update the gains for all remaining unlocked nodes.
4. **Select Optimal Prefix:** After $n/2$ pairs are recorded, find the integer $k$ that maximizes the partial sum of gains $G = \sum_{i=1}^k g_i$. 
5. **Update and Repeat:** If $G > 0$, perform the first $k$ swaps permanently and return to Step 2. If $G \leq 0$, terminate.
$$
D_x = \sum_{y \in \text{External}} w_{xy} - \sum_{y \in \text{Internal}} w_{xy}
$$

## Related Concepts
- [[spectral_partitioning]]
- [[combinatorial_optimization]]
- [[community_detection_heuristics]]