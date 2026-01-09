---
id: ssu_batch6_002
course: Statistical Machine Learning
tags: [svm, unconstrained-optimization, hinge-loss, regularization, convex-optimization]
difficulty: 3
type: derivation
status: to_learn
---

# Question
(4p) Given a training set of examples $\mathcal{T}^m = \{(x^i, y^i) \in (\mathcal{X} \times \{+1, -1\}) \mid i = 1, \dots, m\}$ the SVM algorithm finds parameters of a linear classifier $h(x) = \text{sign}(\langle w, x \rangle + b)$ by solving an unconstrained problem
$$ (w^*, b^*) \in \arg\min_{(w, b) \in \mathbb{R}^{d+1}} F(w, b) $$
where $F: \mathbb{R}^d \times \mathbb{R} \to \mathbb{R}$ is a convex function of the parameters.
**a)** Define the objective function $F(w, b)$ and describe all its components.
**b)** How is the objective function $F(w, b)$ related to the number of training errors?

---
# Solution
## a) Objective Function
The unconstrained formulation of Soft-Margin SVM (C-SVM) minimizes:
$$ F(w, b) = \frac{1}{2} ||w||^2 + C \sum_{i=1}^m \max(0, 1 - y^i(\langle w, x^i \rangle + b)) $$
**Components:**
1.  **Regularization Term ($\frac{1}{2} ||w||^2$):** Minimizes the norm of the weights, which corresponds to maximizing the geometric margin ($\gamma = 1/||w||$). This controls model complexity and prevents overfitting (structural risk minimization).
2.  **Hinge Loss ($\sum \max(0, 1 - y^i f(x^i))$):** Measures the data fit. For each example, it penalizes misclassifications and correct classifications that are within the margin (i.e., functional margin $< 1$).
    -   If $y^i f(x^i) \ge 1$ (correctly classified and outside margin), loss is 0.
    -   If $y^i f(x^i) < 1$ (inside margin or misclassified), loss grows linearly.
3.  **Hyperparameter $C$:** Controls the trade-off between maximizing the margin (small $w$) and minimizing the training error (hinge loss).

## b) Relation to Training Errors
The hinge loss $\ell(y, f(x)) = \max(0, 1 - yf(x))$ is a **convex upper bound** on the 0/1 loss (classification error indicator $\mathbb{I}[y \neq \text{sign}(f(x))]$).
Specifically:
$$ \mathbb{I}[y^i \neq \text{sign}(\langle w, x^i \rangle + b)] \le \max(0, 1 - y^i(\langle w, x^i \rangle + b)) $$
Minimizing $F(w, b)$ minimizes the sum of hinge losses, which acts as a proxy for minimizing the number of training errors (misclassified examples), while simultaneously enforcing a large margin.
So, $F(w, b)$ minimizes an upper bound on the number of training errors plus a regularization term.

## Related Concepts
- [[svm]]
- [[hinge-loss]]
- [[regularization]]
- [[convex-optimization]]
