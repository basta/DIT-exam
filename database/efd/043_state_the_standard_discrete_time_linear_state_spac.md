---
id: efd_043
course: Estimation, Filtration, and Detection
tags: [state-space, discrete-time, linear-systems, kalman-filter]
difficulty: 2
type: open
status: to_learn
---

# Question
State the standard discrete-time linear state-space model equations (Process and Measurement). Define all matrices and vectors involved.

## Options
N/A (Open question)

---
# Solution
**Correct Answer:** 
The discrete-time linear state-space model is defined by:
1. Process Equation (State Transition): $x_k = A_{k-1}x_{k-1} + B_{k-1}u_{k-1} + w_{k-1}$
2. Measurement Equation (Observation): $z_k = H_k x_k + v_k$

## Explanation
The state-space representation is a mathematical model of a physical system as a set of input, output, and state variables related by first-order difference equations. In the context of Estimation and Filtration (like the Kalman Filter), it provides a structured way to describe how a system evolves over time and how we observe its internal state through noisy sensors.

- **Process Equation**: This describes the dynamics of the system. It predicts the next state $x_k$ based on the previous state $x_{k-1}$ and a control input $u_{k-1}$. The term $w_{k-1}$ represents process noise, which accounts for modeling inaccuracies or unmeasured disturbances.
- **Measurement Equation**: This describes the relationship between the internal state $x_k$ and the actual observations $z_k$. Since we rarely measure the state directly or perfectly, the matrix $H_k$ maps the state space into the measurement space, and $v_k$ represents the measurement noise (sensor error).

In standard filtering applications, $w_k$ and $v_k$ are usually assumed to be mutually independent, zero-mean white Gaussian noise sequences with covariance matrices $Q_k$ and $R_k$ respectively.

### Steps / Derivation
1. **Define the State Vector**:
$x_k \in \mathbb{R}^n$ is the state vector at time step $k$.
2. **Define the Transition Matrix**:
$A_{k-1} \in \mathbb{R}^{n \times n}$ is the state transition matrix (or system matrix).
3. **Define the Control Architecture**:
$u_{k-1} \in \mathbb{R}^m$ is the control input vector, and $B_{k-1} \in \mathbb{R}^{n \times m}$ is the input coupling matrix.
4. **Define the Measurement Vector and Matrix**:
$z_k \in \mathbb{R}^p$ is the measurement (or observation) vector. $H_k \in \mathbb{R}^{p \times n}$ is the observation matrix.
5. **Define Noise Terms**:
$w_{k-1} \sim N(0, Q_{k-1})$ is the process noise. $v_k \sim N(0, R_k)$ is the measurement noise.
$$
x_k = A_{k-1}x_{k-1} + B_{k-1}u_{k-1} + w_{k-1}
$$
$$
z_k = H_k x_k + v_k
$$

## Related Concepts
- [[kalman_filter]]
- [[stochastic_processes]]
- [[system_identification]]