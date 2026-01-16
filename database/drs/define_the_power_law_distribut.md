---
id: drs_046
course: Dynamics and Control of Networks
tags: [power-law, scale-free-networks, statistical-mechanics, heavy-tailed-distributions]
difficulty: 3
type: open
status: to_learn
---

# Question
Define the power law distributions, explain how to calculate their moments.

## Options
N/A (This is an open-answer question).

---
# Solution
**Correct Answer:** 
A power law distribution follows $P(k) = Ck^{-\gamma}$. Moments are calculated by integrating $k^m P(k)$ from a minimum value $k_{min}$ to infinity.

## Explanation
In the study of complex networks, a power law distribution describes a relationship where the probability of a variable (such as the degree $k$ of a node) follows a functional form $P(k) \propto k^{-\gamma}$, where $\gamma$ is the scaling exponent (typically $2 < \gamma < 3$). These are often called "scale-free" distributions because they lack a characteristic scale; scaling the argument by a constant results in a proportional scaling of the function itself ($f(ax) = a^{-\gamma}f(x)$).

Unlike Gaussian distributions, power laws are "heavy-tailed," meaning that nodes with extremely high degrees (hubs) have a non-negligible probability of occurring. This has profound implications for network robustness and synchronization.

To calculate the moments of a power law distribution, we look at the expected value of $k$ raised to the $m$-th power. For a continuous approximation, we consider the distribution starting from a minimum value $k_{min}$ to avoid divergence at zero. The $m$-th moment is defined as the integral of $k^m$ weighted by the probability density function. 

A critical property of power laws is that their moments do not always converge. Specifically, the $m$-th moment only exists if $\gamma > m + 1$. In Many real-world networks where $2 < \gamma < 3$, the first moment (average degree) is finite, but the second moment (variance-related) and higher moments diverge as the system size $N \to \infty$. This divergence is why scale-free networks are highly sensitive to targeted attacks on hubs.

### Steps / Derivation
1. **Define the Normalized Distribution:**
Start with the probability density function $P(k)$. To ensure $\int_{k_{min}}^{\infty} P(k) dk = 1$, we find the normalization constant $C$:
$$
P(k) = \frac{\gamma - 1}{k_{min}} \left( \frac{k}{k_{min}} \right)^{-\gamma}
$$

2. **Set up the Moment Integral:**
The $m$-th moment $\langle k^m \rangle$ is calculated as:
$$
\langle k^m \rangle = \int_{k_{min}}^{\infty} k^m P(k) dk
$$

3. **Solve the Integral:**
Substitute the definition of $P(k)$ into the integral:
$$
\langle k^m \rangle = C \int_{k_{min}}^{\infty} k^{m-\gamma} dk = \frac{\gamma - 1}{k_{min}^{-\gamma+1}} \left[ \frac{k^{m-\gamma+1}}{m-\gamma+1} \right]_{k_{min}}^{\infty}
$$

4. **Determine Convergence:**
If $m - \gamma + 1 < 0$ (i.e., $\gamma > m + 1$), the term at infinity vanishes:
$$
\langle k^m \rangle = \frac{\gamma - 1}{\gamma - 1 - m} k_{min}^m
$$
If $\gamma \leq m + 1$, the integral diverges, implying the moment is infinite in the thermodynamic limit.

## Related Concepts
- [[scale_free_property]]
- [[degree_distribution]]
- [[moment_generating_functions]]