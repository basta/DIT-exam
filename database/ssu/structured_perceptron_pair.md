---
id: ssu_batch7_001
course: Statistical Machine Learning
tags: [structured-output, perceptron, sample-complexity, hoeffding-bound]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(7p) Consider a linear classifier $h: \mathcal{X} \times \mathcal{X} \to \mathcal{Y} \times \mathcal{Y}$ predicting a pair of labels $(y_1, y_2) \in \mathcal{Y} \times \mathcal{Y}$ from a pair of inputs $(x_1, x_2) \in \mathcal{X} \times \mathcal{X}$ based on the rule
$$ h(x_1, x_2; \theta) = \arg\max_{y_1 \in \mathcal{Y}, y_2 \in \mathcal{Y}} (\langle \phi(x_1), w_{y_1} \rangle + \langle \phi(x_2), w_{y_2} \rangle + g(y_1, y_2)) \quad (1) $$
where $\phi: \mathcal{X} \to \mathbb{R}^n$ is a feature map, $w_y \in \mathbb{R}^n, y \in \mathcal{Y}$, are vectors and $g: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$ is a function. The vector $\theta \in \mathbb{R}^{n|\mathcal{Y}| + |\mathcal{Y}|^2}$ encapsulates all parameters of the classifier, that is, the vectors $\{w_y \in \mathbb{R}^n \mid y \in \mathcal{Y}\}$ and the function values $\{g(y, y') \in \mathbb{R} \mid y \in \mathcal{Y}, y' \in \mathcal{Y}\}$. Let $\mathcal{T}^m = \{(x_1^j, x_2^j, y_1^j, y_2^j) \in (\mathcal{X} \times \mathcal{X} \times \mathcal{Y} \times \mathcal{Y}) \mid j = 1, \dots, m\}$ and $\mathcal{S}^l = \{(x_1^j, x_2^j, y_1^j, y_2^j) \in (\mathcal{X} \times \mathcal{X} \times \mathcal{Y} \times \mathcal{Y}) \mid j = 1, \dots, l\}$ be a set of training and testing examples, respectively, both being drawn from i.i.d. random variables with the distribution $p(x_1, x_2, y_1, y_2)$.

**a)** Describe a variant of the Perceptron algorithm which finds the parameters $\theta$ such that the classifier (1) predicts all examples from $\mathcal{T}^m$ correctly provided such parameters exists.

**b)** Assume that $\mathcal{Y} = \{0, \dots, 9\}$ and that we want to measure the prediction accuracy of $h$ by computing the absolute deviation between the sum of the correct and the predicted labels. To this end, we define a loss function $\ell(y_1, y_2, \hat{y}_1, \hat{y}_2) = |y_1 + y_2 - \hat{y}_1 - \hat{y}_2|$ and its expected value
$$ R(h) = \mathbb{E}_{(x_1, x_2, y_1, y_2) \sim p} [\ell(y_1, y_2, h_1(x_1), h_2(x_2))] $$
As the distribution $p(x_1, x_2, y_1, y_2)$ is unknown we estimate $R(h)$ by the test error
$$ R_{\mathcal{S}^l}(h) = \frac{1}{l} \sum_{j=1}^l \ell(y_1^j, y_2^j, h_1(x_1^j), h_2(x_2^j)). $$
What is the minimal number of the test examples $l$ which we need to collect in order to guarantee with probability $\gamma$ that $R_{\mathcal{S}^l}(h)$ deviates from $R(h)$ by $\varepsilon$ at most? Write $l$ as a function of $\varepsilon$ and $\gamma$.

---
# Solution
## a) Structured Perceptron Algorithm
The goal is to find $\theta$ comprising $w_y$ and $g(y, y')$. We can treat this as a linear classification problem in a high-dimensional joint feature space. The score function is linear in parameters.
Let $\Psi(x_1, x_2, y_1, y_2)$ be the joint feature vector. The score is $\langle \theta, \Psi(x_1, x_2, y_1, y_2) \rangle$.

**Algorithm:**
1.  Initialize $\theta = 0$ (all $w_y=0$ and all $g(y,y')=0$).
2.  Repeat until convergence (no errors on $\mathcal{T}^m$):
    For each example $j = 1, \dots, m$:
    i.  Predict: $(\hat{y}_1, \hat{y}_2) = \arg\max_{y_1, y_2} (\langle \phi(x_1^j), w_{y_1} \rangle + \langle \phi(x_2^j), w_{y_2} \rangle + g(y_1, y_2))$.
    ii. If $(\hat{y}_1, \hat{y}_2) \neq (y_1^j, y_2^j)$:
        Update parameters:
        $$ w_{y_1^j} \leftarrow w_{y_1^j} + \phi(x_1^j) $$
        $$ w_{y_2^j} \leftarrow w_{y_2^j} + \phi(x_2^j) $$
        $$ g(y_1^j, y_2^j) \leftarrow g(y_1^j, y_2^j) + 1 $$
        $$ w_{\hat{y}_1} \leftarrow w_{\hat{y}_1} - \phi(x_1^j) $$
        $$ w_{\hat{y}_2} \leftarrow w_{\hat{y}_2} - \phi(x_2^j) $$
        $$ g(\hat{y}_1, \hat{y}_2) \leftarrow g(\hat{y}_1, \hat{y}_2) - 1 $$

Note: The update rule corresponds to $\theta \leftarrow \theta + \Psi(x^j, y^j) - \Psi(x^j, \hat{y})$.

## b) Sample Complexity (Hoeffding Bound)
We want $P(|R(h) - R_{\mathcal{S}^l}(h)| \le \varepsilon) \ge \gamma$.
Or equivalently $P(|R - R_S| \ge \varepsilon) \le 1 - \gamma$.
Hoeffding's inequality for sum of bounded random variables $Z_j \in [a, b]$:
$$ P(|\frac{1}{l}\sum Z_j - \mathbb{E}[Z]| \ge \varepsilon) \le 2 \exp\left( -\frac{2 l \varepsilon^2}{(b-a)^2} \right) $$

**Determine the Range of Loss:**
$\mathcal{Y} = \{0, \dots, 9\}$.
Let $S = y_1 + y_2$ and $\hat{S} = \hat{y}_1 + \hat{y}_2$.
Max possible sum is $9+9=18$. Min is $0+0=0$.
The loss is $\ell = |S - \hat{S}|$.
Maximum derivation occurs when $S=0, \hat{S}=18$ or vice versa.
Max loss value = $|0 - 18| = 18$.
Min loss value = $0$.
So the range is $R = b - a = 18 - 0 = 18$.

**Substitute into Hoeffding:**
$$ 2 \exp\left( -\frac{2 l \varepsilon^2}{18^2} \right) \le 1 - \gamma $$
$$ \exp\left( -\frac{2 l \varepsilon^2}{18^2} \right) \le \frac{1 - \gamma}{2} $$
$$ -\frac{2 l \varepsilon^2}{18^2} \le \ln\left( \frac{1 - \gamma}{2} \right) $$
$$ \frac{2 l \varepsilon^2}{324} \ge \ln\left( \frac{2}{1 - \gamma} \right) $$
$$ l \ge \frac{324}{2 \varepsilon^2} \ln\left( \frac{2}{1 - \gamma} \right) $$
$$ l \ge \frac{162}{\varepsilon^2} \ln\left( \frac{2}{1 - \gamma} \right) $$

**Answer:**
$l \ge \frac{162}{\varepsilon^2} \ln\left( \frac{2}{1 - \gamma} \right)$.
(Alternatively using range $R=18$).

## Related Concepts
- [[structured-prediction]]
- [[perceptron]]
- [[hoeffding-bound]]
- [[sample-complexity]]
