---
id: ssu_batch4_001
course: Statistical Machine Learning
tags: [generative-model, linear-classifier, approximation-error, consistency, multivariate-normal]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(6p) Let the observation $x \in \mathcal{X} = \mathbb{R}^n$ and the hidden state $y \in \mathcal{Y} = \{+1, -1\}$ be generated from a multivariate normal distribution
$$ p(x, y) = p(y) \frac{1}{(2\pi)^{\frac{n}{2}}\det(C_y)^{\frac{1}{2}}} e^{-\frac{1}{2}(x - \mu_y)^T C_y^{-1} (x - \mu_y)} \quad (1) $$
where $\mu_y \in \mathbb{R}^n, y \in \mathcal{Y}$, are mean vectors, $C_y \in \mathbb{R}^{n \times n}, y \in \mathcal{Y}$, are covariance matrices and $p(y)$ is a prior probability. Assume that the model parameters are unknown and we want to learn a strategy $h \in \mathcal{X} \to \mathcal{Y}$ which minimizes the probability of misclassification. To this end we use a learning algorithm $A: \cup_{m=1}^\infty (\mathcal{X} \times \mathcal{Y})^m \to \mathcal{H}$ which based on samples generated from the distribution (1) returns a strategy $h$ from the class $\mathcal{H} = \{h(x) = \text{sign}(\langle w, x \rangle + b) \mid w \in \mathbb{R}^n, b \in \mathbb{R}\}$ containing all linear classifiers.

**a)** What is the approximation error in case that $C_+ = C_-$?

**b)** Is the approximation error going to increase or decrease if $C_+ \neq C_-$?

**c)** Assume the algorithm finds a linear classifier which has the minimal classification error on the training examples. Is the algorithm statistically consistent? Explain your answers.

---
# Solution

## a) Approximation Error when $C_+ = C_-$
The approximation error is defined as $R(h^*) - R(h_{Bayes})$, where $h^* \in \mathcal{H}$ is the best classifier in the class, and $h_{Bayes}$ is the optimal Bayes classifier.
The Bayes classifier decides based on the log-likelihood ratio:
$$ \ln \frac{p(x|y=+1)p(y=+1)}{p(x|y=-1)p(y=-1)} \ge 0 $$
If $C_+ = C_- = C$, the quadratic terms $x^T C^{-1} x$ cancel out, and the decision boundary becomes linear (i.e., equation of a hyperplane).
Thus, the Bayes classifier is linear: $h_{Bayes} \in \mathcal{H}$.
Since the hypothesis class $\mathcal{H}$ contains the Bayes optimal classifier, the approximation error is **zero**.

## b) Approximation Error when $C_+ \neq C_-$
If the covariance matrices are different, the decision boundary of the Bayes classifier is **quadratic** (Quadratic Discriminant Analysis).
Since the true boundary is quadratic, a linear classifier (from $\mathcal{H}$) generally cannot perfectly approximate it.
Therefore, the best possible linear classifier $h^* \in \mathcal{H}$ will have a higher risk than the Bayes classifier $h_{Bayes}$.
The approximation error $R(h^*) - R(h_{Bayes})$ will be **strictly positive** (assuming the distributions are not trivial). Thus, the approximation error **increases** (from 0 to something positive).

## c) Statistical Consistency
An algorithm is statistically consistent if the risk of the learned classifier $R(h_m)$ converges to the Bayes risk $R(h_{Bayes})$ as $m \to \infty$.
Here, the algorithm finds the ERM minimizer in $\mathcal{H}$.
1.  **If $C_+ = C_-$:** The Bayes classifier is in $\mathcal{H}$. Under standard conditions (finite VC dimension of linear classifiers), ERM is consistent for the class $\mathcal{H}$. So $R(h_m) \to R(h^*) = R(h_{Bayes})$. The algorithm is **consistent**.
2.  **If $C_+ \neq C_-$:** The Bayes classifier is NOT in $\mathcal{H}$. The ERM algorithm will converge to the best linear classifier $h^*$, but $R(h^*) > R(h_{Bayes})$. The algorithm is **not consistent** with respect to the Bayes risk (it is only consistent w.r.t the best in class).
    *Technically, "statistically consistent" often refers to converging to the Bayes optimal. Since the question asks generally about the "algorithm" without specifying the scenario (a or b), but given the context of model mismatch in (b):*
    Generally, we say it is **not consistent** because the hypothesis space does not contain the target concept (the Bayes optimal classifier).

## Related Concepts
- [[generative-model]]
- [[linear-classifier]]
- [[approximation-error]]
- [[statistical-consistency]]
- [[bayes-classifier]]
