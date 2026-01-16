---
id: drs_086
course: Dynamics and Control of Networks
tags: [small-world-phenomenon, kleinberg-model, hierarchical-networks, message-passing]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the two models of message passing, i.e., the Kleinberg's model and the hierarchical model, and enumerate their limitations (assumptions). What is the complexity of message passing in these models?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** 

The models describe how decentralized routing can achieve the "Six Degrees of Separation." **Kleinberg's Model** utilizes a 2D lattice grid where nodes have local links and one long-range link chosen with probability $P(u,v) \propto d(u,v)^{-\alpha}$. **The Hierarchical Model** organizes nodes in a tree structure where link probability depends on the height of the lowest common ancestor. Both models achieve $O(\log^2 n)$ or $O(\log n)$ delivery time under specific parameter tuning.

## Explanation
### 1. Kleinberg’s Model
Kleinberg addressed why individuals can find short paths using only local information. He augmented a $k$-dimensional lattice with long-range random edges. For a 2D grid, the probability of a long-range edge between nodes $u$ and $v$ is proportional to $d(u,v)^{-\alpha}$, where $d(u,v)$ is the Manhattan distance.
- **Mechanism:** A greedy algorithm is used where each holder of the message passes it to the neighbor (local or long-range) geographically closest to the target.
- **Complexity:** When $\alpha = \text{dimension}$ (e.g., $\alpha = 2$ for a 2D grid), the delivery time is $O(\log^2 n)$. If $\alpha$ is too small, the long-range links are too random; if too large, they are too local.

### 2. Hierarchical Model (Watts et al.)
This model posits that social networks are organized by "social distance" based on hierarchies (e.g., occupation, geography). Nodes are leaves in a $b$-ary tree. The distance $h(u,v)$ is the height of their lowest common ancestor.
- **Mechanism:** The probability of a link is $P(u,v) \propto e^{-\zeta h(u,v)}$. Message passing mirrors the search through functional groups.
- **Complexity:** In the searchable regime, the delivery time is $O(\log n)$ or $O(\text{poly}(\log n))$.

### 3. Limitations and Assumptions
- **Global Knowledge of Coordinates:** Both models assume nodes know the "position" or "category" of the target and their neighbors relative to that target. 
- **Greedy Consistency:** They assume every participant is cooperative and possesses the same mapping of the network's geometry.
- **Fixed Topology:** They often assume static networks, ignoring that social links evolve during the message-passing process.
- **Dimensionality:** Kleinberg’s result is highly sensitive to the match between the clustering exponent $\alpha$ and the lattice dimension.

### Steps / Derivation
1. **Kleinberg's Search Time:** To prove the $O(\log^2 n)$ bound, divide the distance to the target into $O(\log n)$ phases.
2. **Phase Completion:** In each phase, the probability of finding a long-range link that halves the distance to the target is calculated as:
$$
P(\text{halving distance}) \geq \frac{1}{\log n}
$$
3. **Total Time:** Summing the expected time for all phases yields:
$$
T \approx \sum_{i=1}^{\log n} \log n = O(\log^2 n)
$$

## Related Concepts
- [[small_world_networks]]
- [[decentralized_search]]
- [[navigability_of_networks]]