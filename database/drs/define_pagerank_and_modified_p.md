---
id: drs_029
course: Dynamics and Control of Networks
tags: [centrality-measures, pagerank, random-walks, spectral-analysis]
difficulty: 3
type: open
status: to_learn
---

# Question
Define PageRank and modified PageRank.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** PageRank is a centrality measure based on the stationary distribution of a random walk on a graph. Modified PageRank (Google PageRank) introduces a teleportation factor to ensure the walk is ergodic on any graph topology.

## Explanation
PageRank is a spectral centrality metric originally designed to rank web pages. The fundamental intuition is that a node is important if it is pointed to by other important nodes. In its simplest form, it represents the probability that a random surfer, following edges at random, will be at a specific node in the long run. Mathematically, this corresponds to the leading eigenvector of the transition matrix $P$, where $P = D^{-1}A$ (for a row-stochastic matrix) and $A$ is the adjacency matrix.

However, basic PageRank faces two major issues in real-world networks: **dead ends** (nodes with no out-degree) and **spider traps** (cycles that "trap" the random walker). If a graph is not strongly connected or is periodic, the transition matrix may not have a unique, strictly positive stationary distribution.

To solve this, **Modified PageRank** (often called the Google PageRank) introduces a "teleportation" mechanism. It assumes that with probability $\alpha$ (the damping factor, typically 0.85), the surfer follows an outgoing link, and with probability $(1 - \alpha)$, the surfer jumps to a random node in the network. This modification ensures that the resulting Google Matrix $G$ is stochastic, irreducible, and aperiodic. According to the Perron-Frobenius theorem, this guarantees a unique stationary distribution (the PageRank vector) with all positive components, regardless of the initial graph structure.

### Steps / Derivation
1. **Define the Transition Matrix:** For a graph with $n$ nodes, let $M$ be the transitions where $M_{ij} = 1/d_{out}(j)$ if there is an edge from $j$ to $i$.
2. **Handle Dangling Nodes:** If a node has no outgoing edges, replace its column in $M$ with $1/n$ for all entries.
3. **Introduce Damping Factor:** Add the teleportation term to create the Google Matrix $G$:
$$
G = \alpha M + \frac{(1 - \alpha)}{n} \mathbf{1}\mathbf{1}^T
$$
4. **Solve for Eigenvector:** The PageRank vector $\mathbf{r}$ is the principal eigenvector of $G$ satisfying:
$$
\mathbf{r} = G\mathbf{r}
$$

## Related Concepts
- [[random_walks]]
- [[eigenvector_centrality]]
- [[perron_frobenius_theorem]]