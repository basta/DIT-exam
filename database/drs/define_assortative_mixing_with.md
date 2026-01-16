---
id: drs_043
course: Dynamics and Control of Networks
tags: [assortativity, network-topology, homophily, scalar-characteristics]
difficulty: 3
type: open
status: to_learn
---

# Question
Define assortative mixing with respect to scalar characteristics. Explain how does it differ from that for enumerative characteristics.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Assortative mixing for scalar characteristics measures the correlation between continuous/ordered attributes (like age or income) of connected nodes, whereas for enumerative characteristics, it measures the tendency of nodes to connect to others with the exact same discrete category (like race or language).

## Explanation
Assortative mixing, or homophily, is a fundamental property of networks where nodes with similar properties tend to link with one another. When dealing with **scalar characteristics**, we are concerned with properties that take on numerical values (e.g., node degree, age, or wealth). In this context, assortativity is quantified by the correlation between the values of these characteristics at the ends of an edge. If the correlation is positive, the network is assortative (high-value nodes connect to high-value nodes); if negative, it is disassortative.

The primary difference between scalar and **enumerative (discrete) characteristics** lies in how similarity is defined and measured:

1.  **Measurement Metric**: For enumerative characteristics (like gender or nationality), there is typically no inherent ordering. We simply measure the fraction of edges that connect nodes of the same type versus a random distribution. This is often calculated using a modularity-like coefficient $r$. For scalar characteristics, because the values have an inherent order and magnitude, we use the **Pearson correlation coefficient** to measure the relationship.
2.  **The Nature of Similarity**: In the enumerative case, a node is either "the same" or "different." In the scalar case, nodes can be "close" or "far apart" in value. For example, in a network mixed by age, a 20-year-old connecting to a 21-year-old contributes to positive assortativity more significantly than a 20-year-old connecting to a 70-year-old, whereas in enumerative mixing, both might simply be categorized as "different" if the categories are discrete age brackets.
3.  **The Degree Distribution**: A special case of scalar assortativity is **degree assortativity**, where the scalar value is the degree of the node itself. This is a structural property of the graph, unlike enumerative characteristics which are usually external metadata applied to the nodes.

### Steps / Derivation
1. For scalar characteristics, let $x_i$ and $y_i$ be the values of the characteristic at the ends of the $i$-th edge. The assortativity coefficient $r$ is defined as:
$$
r = \frac{\sum_i (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_i (x_i - \bar{x})^2} \sqrt{\sum_i (y_i - \bar{y})^2}}
$$
2. For enumerative characteristics, define a mixing matrix $e_{ij}$ representing the fraction of edges connecting type $i$ to type $j$. The coefficient is:
$$
r = \frac{\text{Tr}(\mathbf{e}) - \sum e_{ij}^2}{1 - \sum e_{ij}^2}
$$

## Related Concepts
- [[degree_correlation]]
- [[homophily_coefficient]]
- [[mixing_matrix]]