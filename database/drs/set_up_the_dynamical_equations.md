---
id: drs_091
course: Dynamics and Control of Networks
tags: [consensus-protocol, lti-systems, state-synchronization, cooperative-control]
difficulty: 3
type: derivation
status: to_learn
---

# Question
Set up the dynamical equations for continuous-time homogeneous LTI agents using local neighborhood error signal for state synchronization.

## Options
A) N/A (Open Derivation)
B) 
C) 
D) 

---
# Solution
**Correct Answer:** $\dot{x}_i(t) = Ax_i(t) + BK \sum_{j \in \mathcal{N}_i} a_{ij} (x_j(t) - x_i(t))$

## Explanation
In the study of multi-agent systems, state synchronization (or consensus) refers to the process where a group of autonomous agents reaches a common state through local interactions. When considering continuous-time homogeneous Linear Time-Invariant (LTI) systems, each agent $i$ (where $i=1, \dots, N$) possesses internal dynamics typically described by the state-space equations $\dot{x}_i = Ax_i + Bu_i$.

To achieve synchronization without a global controller, each agent must rely on a "local neighborhood error signal." This signal is derived from the difference between agent $i$'s state and the states of its neighbors $\mathcal{N}_i$, as defined by the network topology. The network is mathematically represented by an Adjacency Matrix $A = [a_{ij}]$, where $a_{ij} > 0$ if agent $i$ can receive information from agent $j$.

The control input $u_i$ is designed as a diffusive coupling law. Specifically, the agent scales the sum of the differences $(x_j - x_i)$ by a feedback gain matrix $K$. When these individual equations are stacked into a global state vector, the network's Graph Laplacian $L$ emerges. The Laplacian matrix $L = D - A$ (where $D$ is the degree matrix) effectively encodes the diffusive nature of the coupling. For synchronization to occur, the pair $(A, B)$ must be stabilizable, and the connectivity of the graph (e.g., having a spanning tree) must be sufficient to ensure that the eigenvalues of the Laplacian interact favorably with the feedback gain $K$.

### Steps / Derivation
1. **Define Individual Agent Dynamics:** Start with the standard LTI state equations for agent $i$:
$$
\dot{x}_i(t) = Ax_i(t) + Bu_i(t)
$$

2. **Define the Local Neighborhood Error:** The error signal relative to neighbors is the sum of differences in states:
$$
e_i(t) = \sum_{j=1}^{N} a_{ij} (x_j(t) - x_i(t))
$$

3. **Define the Control Law:** Apply a linear feedback gain $K$ to the accumulated error signal:
$$
u_i(t) = K \sum_{j=1}^{N} a_{ij} (x_j(t) - x_i(t))
$$

4. **Combine into Closed-Loop Form:** Substitute the control law back into the dynamics:
$$
\dot{x}_i(t) = Ax_i(t) + BK \sum_{j=1}^{N} a_{ij} (x_j(t) - x_i(t))
$$

5. **Express in Kronecker Form (Global Dynamics):** Using the Graph Laplacian $L$, where $L_{ii} = \sum a_{ij}$ and $L_{ij} = -a_{ij}$ for $i \neq j$:
$$
\dot{x}(t) = (I_N \otimes A - L \otimes BK)x(t)
$$

## Related Concepts
- [[graph_laplacian]]
- [[kronecker_product]]
- [[consensus_stability_analysis]]