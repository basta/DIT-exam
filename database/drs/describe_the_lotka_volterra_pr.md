---
id: drs_080
course: Dynamics and Control of Networks
tags: [lotka-volterra, population-dynamics, networked-ecology, metapopulations]
difficulty: 4
type: open
status: to_learn
---

# Question
Describe the Lotka-Volterra predator-prey model. Explain various ways how it extends to the network setting.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** The Lotka-Volterra model is a system of nonlinear first-order differential equations describing the interaction between two species. On networks, it extends via spatial patches (metapopulations) with migration, or through multi-species food webs where nodes represent species and edges represent trophic interactions.

## Explanation
The classical Lotka-Volterra predator-prey model is defined by two coupled equations:
$$ \frac{dx}{dt} = \alpha x - \beta xy $$
$$ \frac{dy}{dt} = \delta xy - \gamma y $$
where $x$ is the prey population, $y$ is the predator population, $\alpha$ is the prey growth rate, $\beta$ is the predation rate, $\gamma$ is the predator death rate, and $\delta$ describes predator growth based on consumption. This model produces periodic oscillations in population sizes.

When extending this to a network setting, there are two primary paradigms:

1. **Metapopulation Networks (Spatial Extension):** Here, each node $i$ represents a physical patch or habitat containing its own predator-prey pairs. The edges represent migration paths between these patches. The equations are modified to include a Laplacian-like diffusion term:
$$ \dot{x}_i = f(x_i, y_i) + D_x \sum_{j} A_{ij}(x_j - x_i) $$
where $D$ is the diffusion coefficient and $A$ is the adjacency matrix. This approach studies how spatial connectivity leads to synchronization or pattern formation (e.g., Turing instabilities).

2. **Food Webs (Trophic Networks):** In this paradigm, each node is a different species, and the edges represent "who eats whom." The model becomes a high-dimensional system where the growth of node $i$ depends on its interactions with all its neighbors:
$$ \dot{x}_i = x_i (r_i + \sum_{j=1}^N M_{ij} x_j) $$
where $M_{ij}$ represents the interaction matrix (positive for prey, negative for predators). Network topology (degree distribution, modularity) significantly impacts the stability and resilience of the ecosystem.

### Steps / Derivation
1. **Classic Stability Analysis:** Linearize the system around the non-trivial equilibrium $(x^*, y^*) = (\frac{\gamma}{\delta}, \frac{\alpha}{\beta})$ to find purely imaginary eigenvalues, explaining the neutral stability/oscillations.
2. **Coupling through Diffusion:** Introduce the discrete Laplacian $L = D - A$ to model migration between patches:
$$ \dot{\mathbf{x}} = F(\mathbf{x}, \mathbf{y}) - D_x L \mathbf{x} $$
3. **Complexity vs. Stability:** Analyze the interaction matrix $M$ in large networks. In random networks (May’s Theorem), stability decreases as complexity (number of nodes and link density) increases, unless specific structural properties (like omnivory or weak links) are present.

## Related Concepts
- [[metapopulation_dynamics]]
- [[stability_of_large_complex_ecosystems]]
- [[reaction_diffusion_systems]]