---
id: drs_093
course: Dynamics and Control of Networks
tags: [algebraic-riccati-equation, synchronization, lqr-control, network-dynamics]
difficulty: 4
type: open
status: to_learn

---
# Question
Show that with the distributed feedback gain designed from the single-agent Algebraic Riccati Equation the resulting synchronizing region is an unbounded left-hand half-plane in the complex plane.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The synchronizing region is defined by $Re(\lambda_i \sigma) > \frac{1}{2}$ (or similar threshold depending on scaling), which corresponds to an open, unbounded half-plane in the complex plane that ensures the stability of the synchronization error dynamics.

## Explanation
In the context of multi-agent systems, synchronization involves ensuring that the states of all agents converge to a common trajectory. For a network of linear agents $\dot{x}_i = Ax_i + Bu_i$, a common distributed control law is $u_i = K \sum_{j=1}^N a_{ij}(x_i - x_j)$, where $K$ is the feedback gain. The stability of the synchronization error is determined by the eigenvalues $\lambda_i$ of the graph Laplacian $L$. Specifically, the error dynamics are stable if the matrices $A - \sigma \lambda_i BK$ are Hurwitz for all non-zero eigenvalues $\lambda_i$.

When $K$ is designed using the Linear Quadratic Regulator (LQR) approach via the Algebraic Riccati Equation (ARE), we solve $A^T P + PA - PBR^{-1}B^T P + Q = 0$ and set $K = R^{-1}B^T P$. The synchronizing region represents the set of complex numbers $z$ for which the matrix $A - zBK$ is stable. By applying the properties of LQR and the Kalman-Yakubovich-Popov (KYP) inequality, it can be shown that the closed-loop system is robust against certain perturbations in the feedback path. Specifically, the optimal gain $K$ provides a guaranteed gain margin. In the complex plane, this translates to the requirement that the eigenvalues of the Laplacian must fall within a region where the "effective gain" maintains the stability of the Hamiltonian structure underlying the ARE. Because the LQR design ensures stability for any gain $\sigma \geq 1/2$ (assuming $R=I$ and specific scaling), the region extends infinitely to the right (or left depending on sign conventions of the Laplacian) in the complex plane, forming an unbounded half-plane.

### Steps / Derivation
1. Define the single-agent ARE and the feedback gain $K$:
$$
A^T P + PA - PBR^{-1}B^T P + Q = 0, \quad K = R^{-1}B^T P
$$
2. Decompose the network error dynamics using the Laplacian eigenvalues $\lambda_i$. The stability of the network depends on the stability of:
$$
\dot{\tilde{x}}_i = (A - \sigma \lambda_i BK)\tilde{x}_i
$$
3. Use the LQR return difference inequality derived from the ARE:
$$
(I + K(sI - A)^{-1}B)^* R (I + K(sI - A)^{-1}B) = R + B^T (-sI - A^T)^{-1} Q (sI - A)^{-1} B
$$
4. For $s = j\omega$, the right-hand side is $\geq R$. This implies that for a scalar coupling gain $\alpha$, the system $A - \alpha BK$ is stable if $Re(\alpha) > 1/2$.
5. Generalizing to complex eigenvalues $z = \sigma \lambda_i$, the Lyapunov function $V = \tilde{x}^* P \tilde{x}$ yields a derivative $\dot{V} < 0$ as long as $z$ stays within the half-plane defined by the LQR robustness margins.
6. Conclusion: The region $\mathcal{S} = \{ z \in \mathbb{C} : Re(z) > \alpha \}$ is an unbounded half-plane.

## Related Concepts
- [[algebraic_riccati_equation]]
- [[laplacian_spectrum]]
- [[linear_quadratic_regulator]] transport