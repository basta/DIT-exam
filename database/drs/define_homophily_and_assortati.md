---
id: drs_042
course: Dynamics and Control of Networks
tags: [network-topology, node-attributes, social-networks]
difficulty: 2
type: open
status: to_learn
---

# Question
Define homophily and assortative mixing in networks.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Homophily is the tendency of individuals to associate with similar others based on intrinsic attributes; Assortative mixing is the broader statistical tendency for nodes with similar properties (often degree) to be connected.

## Explanation
In the study of network science and complex systems, the patterns of connection between nodes are rarely random. Two fundamental concepts used to describe these non-random patterns are homophily and assortative mixing.

**Homophily** is a term primarily rooted in sociology, often summarized by the phrase "birds of a feather flock together." It refers to the empirical observation that individuals in a social network are more likely to form ties with others who share similar traits. These traits can be immutable characteristics (such as age, ethnicity, or gender) or acquired characteristics (such as education level, occupation, or interests). Homophily leads to the formation of dense clusters or communities where members share common attributes, which significantly impacts the dynamics of information diffusion and opinion formation within those groups.

**Assortative Mixing** (or Assortativity) is a more general mathematical and structural description of this phenomenon. While it can refer to discrete attributes (like homophily), in network control and dynamics, it most frequently refers to **degree assortativity**. A network exhibits assortative mixing if nodes with a high degree tend to be connected to other high-degree nodes, and low-degree nodes tend to connect to other low-degree nodes. Conversely, if high-degree nodes (hubs) tend to connect to low-degree nodes, the network is said to be **disassortative**. 

Quantitatively, assortativity is often measured using the assortativity coefficient $r$, which is a Pearson correlation coefficient of degree between pairs of linked nodes. The value ranges from $-1 \leq r \leq 1$.
- $r > 0$: Assortative network (typical of social networks).
- $r < 0$: Disassortative network (typical of biological and technological networks like the Internet).
- $r = 0$: Neutral/Random network.

### Steps / Derivation
1. Identify the basis of connection: Homophily usually looks at node "tags" or "labels" (qualitative), while assortative mixing often looks at degree (quantitative).
2. Calculate the Assortativity Coefficient $r$:
$$
r = \frac{\sum_{jk} jk(e_{jk} - q_j q_k)}{\sigma_q^2}
$$
where $e_{jk}$ is the joint probability distribution of the degrees of the nodes at either end of a randomly chosen edge.

## Related Concepts
- [[degree_correlation]]
- [[community_detection]]
- [[preferential_attachment]]