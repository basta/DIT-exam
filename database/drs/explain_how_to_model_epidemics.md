---
id: drs_079
course: Dynamics and Control of Networks
tags: [epidemiology, network-topology, compartmental-models]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain how to model epidemics on networks. What is the role of vertices and vertex variables?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Open-ended conceptual explanation.

## Explanation
Modeling epidemics on networks involves representing a population as a graph $G = (V, E)$, where $V$ is the set of vertices (nodes) and $E$ is the set of edges (links). Unlike classical "well-mixed" mass-action models, network-based models account for the contact structure between individuals, which significantly impacts how a pathogen spreads.

The **role of vertices** is to represent individual entities within the population (e.g., people, computers, or cities). In this framework, the connectivity of a vertex—defined by its degree $k_i$—determines its potential to transmit or receive the infection. High-degree hubs in a network are particularly critical, as they can accelerate the spread and lower the epidemic threshold.

**Vertex variables** are used to track the epidemiological state of each individual at a given time $t$. Typically, these are discrete or continuous indicators. For a discrete stochastic model, the state of vertex $i$ might be $X_i(t) \in \{S, I, R\}$, representing Susceptible, Infectious, or Recovered status. In a mathematical "mean-field" or deterministic approximation, the vertex variable $x_i(t)$ often represents the probability that vertex $i$ is infected at time $t$. The dynamics are then governed by a system of differential equations that describe the probability transitions based on the states of neighbors $j \in \mathcal{N}_i$.

### Steps / Derivation
1. **Define the Network Topology**: Represent the population using an adjacency matrix $A$, where $A_{ij} = 1$ if a contact exists between $i$ and $j$, and $0$ otherwise.
2. **Assign Vertex Variables**: For each vertex $i$, define a state variable (e.g., $x_i$ for the probability of infection in an SIS model).
3. **Formulate Transition Dynamics**: Express the rate of change based on infection rate $\beta$ and recovery rate $\gamma$:
$$
\frac{dx_i}{dt} = \beta (1 - x_i) \sum_{j=1}^{N} A_{ij} x_j - \gamma x_i
$$
4. **Analyze the Threshold**: Determine the conditions under which an epidemic persists, typically related to the spectral radius $\rho(A)$ of the adjacency matrix, where the epidemic persists if $\frac{\beta}{\gamma} > \frac{1}{\rho(A)}$.

## Related Concepts
- [[epidemic_threshold]]
- [[degree_distribution]]
- [[mean_field_approximation]]