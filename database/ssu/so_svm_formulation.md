---
id: 2016_ssu_002
course: Statistical Machine Learning
tags: [structured-output-svm, quadratic-programming, optimization, convex-optimization]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(5p) A generic linear classifier $h: \mathcal{X} \to \mathcal{Y}$ reads
$$ h(x; w) = \arg\max_{y \in \mathcal{Y}} \langle w, \phi(x, y) \rangle \quad (1) $$
where $w \in \mathbb{R}^n$ are parameters and $\phi: \mathcal{X} \times \mathcal{Y} \to \mathbb{R}^n$ is a joint feature map. Given a training set $\mathcal{T}^m = \{(x^i, y^i) \in \mathcal{X} \times \mathcal{Y} \mid i = 1, \dots, m\}$, the SO-SVM algorithm learns the parameters of the classifier (1) by solving a convex problem
$$ w^* = \arg\min_{w \in \mathbb{R}^n} \left( \frac{\lambda}{2} \|w\|^2 + F(w) \right) \quad (2) $$
where $\lambda > 0$ is a regularization constant, the empirical risk proxy $F(w)$ is defined by
$$ F(w) = \frac{1}{m} \sum_{i=1}^m \max \{0, \max_{y \in \mathcal{Y} \setminus \{y^i\}} (\ell(y^i, y) + \langle w, \phi(x^i, y) \rangle - \langle w, \phi(x^i, y^i) \rangle) \} $$
and $\ell: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_+$ is a target loss function.

Assume we want to use the SO-SVM for learning a classifier predicting age from a face. In particular, let $x \in \mathcal{X} = \mathbb{R}^n$ be a feature descriptor of an input facial image, $\mathcal{Y} = \{1, \dots, 100\}$ be a set of age categories and $\ell(y, y') = |y - y'|$ a loss penalizing the predictions. The age is to be predicted by a linear classifier
$$ h'(x; v, b_1, \dots, b_Y) = \arg\max_{y \in \mathcal{Y}} (y \langle x, v \rangle + b_y) \quad (3) $$
where $v \in \mathbb{R}^n$ and $b_y \in \mathbb{R}, y \in \mathcal{Y}$, are unknown parameters.

**a)** Define the joint feature map $\phi(x, y)$ so that the classifier (3) becomes an instance of the generic classifier (1).

**b)** Reformulate the problem (2) for learning the parameters ($v \in \mathbb{R}^n, b_y \in \mathbb{R}, y \in \mathcal{Y}$) of the age classifier (3) as a convex quadratic program.
*Hint: Replace the non-linear terms in (2) by slack variables.*

**c)** What is the number of variables and the number of linear constraints of the quadratic program?

---
# Solution

## a) Joint Feature Map
We define the parameter vector $w$ as the concatenation of $v$ and the vector of biases $b = [b_1, \dots, b_{100}]^\top$. Thus $w \in \mathbb{R}^{n + 100}$.
To match the form $\langle w, \phi(x, y) \rangle = y \langle x, v \rangle + b_y$, we define the feature map $\phi(x, y)$ as:
$$ \phi(x, y) = \begin{bmatrix} y x \\ e_y \end{bmatrix} $$
where $e_y \in \mathbb{R}^{100}$ is a standard basis vector with $1$ at the position corresponding to age $y$ and $0$ elsewhere.

Verification:
$$ \langle w, \phi(x, y) \rangle = \left\langle \begin{bmatrix} v \\ b \end{bmatrix}, \begin{bmatrix} y x \\ e_y \end{bmatrix} \right\rangle = v^\top (y x) + b^\top e_y = y \langle v, x \rangle + b_y $$
This matches equation (3).

## b) Quadratic Program Formulation
We introduce slack variables $\xi_i$ for each training example $i=1, \dots, m$ to upper bound the max term in $F(w)$.
The optimization problem becomes:

$$ \min_{v, b, \xi} \quad \frac{\lambda}{2} (\|v\|^2 + \|b\|^2) + \frac{1}{m} \sum_{i=1}^m \xi_i $$

Subject to the constraints:
1. $\xi_i \ge 0, \quad \forall i = 1, \dots, m$
2. $\xi_i \ge \ell(y^i, y) + \langle w, \phi(x^i, y) \rangle - \langle w, \phi(x^i, y^i) \rangle, \quad \forall i=1, \dots, m, \forall y \in \mathcal{Y} \setminus \{y^i\}$

Substituting $\ell(y, y') = |y - y'|$ and the inner product form derived in (a):
$$ \langle w, \phi(x^i, y) \rangle - \langle w, \phi(x^i, y^i) \rangle = (y \langle v, x^i \rangle + b_y) - (y^i \langle v, x^i \rangle + b_{y^i}) = (y - y^i)\langle v, x^i \rangle + b_y - b_{y^i} $$

The full set of constraints is:
$$ \xi_i \ge |y^i - y| + (y - y^i)\langle v, x^i \rangle + b_y - b_{y^i}, \quad \forall i=1, \dots, m, \quad \forall y \in \mathcal{Y} \setminus \{y^i\} $$
$$ \xi_i \ge 0, \quad \forall i=1, \dots, m $$

## c) Number of Variables and Constraints
**Variables:**
- $v$: $n$ variables.
- $b$: $100$ variables (one for each age category).
- $\xi$: $m$ variables (one slack variable for each training example).
**Total variables:** $n + m + 100$.

**Constraints:**
For each training example $i$:
- One non-negativity constraint: $\xi_i \ge 0$.
- One constraint for each incorrect label $y \in \mathcal{Y} \setminus \{y^i\}$. Since $|\mathcal{Y}| = 100$, there are 99 such labels.
- Total constraints per example: $1 + 99 = 100$.
**Total linear constraints:** $100m$.

## Related Concepts
- [[structured-output-svm]]
- [[convex-optimization]]
- [[feature-map]]
- [[slack-variables]]
