---
id: drs_077
course: Dynamics and Control of Networks
tags: [network-robustness, scale-free-networks, percolation-theory]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe uniform and non-uniform vertex removal. Comment on the robustness of power law networks to vertex removal.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Open-ended descriptive response.

## Explanation
Vertex removal is a central theme in the study of network robustness and vulnerability, formulated mathematically through percolation theory. 

**Uniform vertex removal** (also known as random failure) occurs when nodes are removed from the network with equal probability $1-p$, regardless of their topological properties. In this scenario, every node is equally likely to be deleted. In Erdős-Rényi (random) graphs, the network exhibits a phase transition at a critical threshold $p_c$; if the fraction of remaining nodes is below this, the giant component disintegrates.

**Non-uniform vertex removal** (also known as targeted attack) involves removing nodes based on specific criteria, typically their importance to the network's connectivity. The most common strategy is **high-degree removal**, where "hubs" (nodes with the highest degree $k$) are targeted first. Because hubs act as the primary bridges between different clusters, their removal is far more damaging to the network's global connectivity than random removal.

**Robustness of Power Law Networks:**
Power law (scale-free) networks, characterized by a degree distribution $P(k) \sim k^{-\gamma}$, exhibit a "robust-yet-fragile" property. Due to the high variance in their degree distribution:
1. **Robustness to random failure:** They are exceptionally resilient to uniform removal. Since the vast majority of nodes have small degrees, random deletion is highly unlikely to hit a hub. Mathematically, for $2 < \gamma < 3$, the critical threshold $p_c$ approaches zero as $N \to \infty$, meaning the giant component persists even after a large fraction of nodes are removed.
2. **Fragility to targeted attacks:** They are highly vulnerable to non-uniform removal. Removing even a tiny percentage (typically $<5\%$) of the highest-degree hubs causes the network to fracture into small, isolated clusters, leading to a total loss of global communication.

### Steps / Derivation
1. **Define Percolation Threshold:** The condition for the existence of a giant component in a configuration model is given by the Molloy-Reed criterion:
$$
\kappa = \frac{\langle k^2 \rangle}{\langle k \rangle} > 2
$$
2. **Random Removal Impact:** In random removal, the new degree distribution becomes $P'(k)$. For power law networks with $\gamma < 3$, the second moment $\langle k^2 \rangle$ diverges in the limit of large $N$. This divergence ensures that the criterion $\kappa > 2$ remains satisfied even for very small $p$.
3. **Targeted Removal Impact:** When hubs are removed, we effectively truncate the tail of the power law distribution. This causes the second moment $\langle k^2 \rangle$ to collapse rapidly:
$$
\langle k^2 \rangle = \int_{k_{min}}^{k_{max}} k^2 P(k) dk
$$
The removal of the upper limit $k_{max}$ (the hubs) reduces $\kappa$ below 2 almost immediately, leading to network fragmentation.

## Related Concepts
- [[scale_free_networks]]
- [[percolation_theory]]
- [[error_and_attack_tolerance]]