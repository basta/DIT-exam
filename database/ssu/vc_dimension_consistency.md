---
id: ssu_batch6_001
course: Statistical Machine Learning
tags: [vc-dimension, statistical-consistency, hypothesis-space, linear-classifier, threshold-classifier]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(6p) Assume you are going to learn a two-class classifier $h: \mathcal{X} \to \{+1, -1\}$ from examples with the goal to minimize the expected classification error. The classifier is selected from a hypothesis space $\mathcal{H}$ based on the minimal training error defined as the number of misclassified examples. Consider the following three cases of hypothesis space:
(1) $\mathcal{H}_1 = \{h(x) = \text{sign}(x - \theta) \mid \theta \in \mathbb{R}\}$.
(2) $\mathcal{H}_2 = \{h(x) = \text{sign}(|x - \mu_1| - |x - \mu_2|) \mid \mu_1 \in \mathbb{R}, \mu_2 \in \mathbb{R}\}$.
(3) $\mathcal{H}_3 = \{h(x) = \text{sign}(\langle w, x \rangle + b) \mid w \in \mathbb{R}^d, b \in \mathbb{R}\}$.

**a)** What is the Vapnik-Chervonenkis dimension of $\mathcal{H}_1, \mathcal{H}_2$ and $\mathcal{H}_3$?

**b)** Assume that in all three cases your algorithm can find a classifier with the minimal training error. In which cases is the algorithm statistically consistent?

---
# Solution
## a) VC Dimensions
1.  **$\mathcal{H}_1$ (Thresholds in 1D):**
    These are classifiers that split the line at $\theta$. They can distinguish at most 1 point (shatter 1 point). With 2 points, say $x_1 < x_2$, we cannot label them $(+1, -1)$ because everything left of $\theta$ is $-1$ (or $+1$ depending on sign convention, but here it's fixed $\text{sign}(x-\theta)$, so $x>\theta \implies +1$, $x<\theta \implies -1$). Wait, the definition is fixed.
    -   If $\text{sign}(x-\theta)$ is fixed, we can only label $(-1, +1)$ pattern (0, 1). We cannot do $(+1, -1)$. So VC dim might be 1?
    -   Actually, for VC-dim calculation, usually the set includes both directions ($\text{sign}(s \cdot (x-\theta))$) or just one.
    -   Given exactly $\{h(x) = \text{sign}(x - \theta)\}$, we can ONLY classify points as $(- \dots - | + \dots +)$. We cannot classify a single point as $-1$ and another as $+1$ if the order is flipped?
    -   Let's check 1 point: $x_1$. Can we give it $+1$? Yes, pick $\theta < x_1$. Can we give it $-1$? Yes, pick $\theta > x_1$. So $VC \ge 1$.
    -   Let's check 2 points: $x_1 < x_2$.
        -   $(-1, -1)$: $\theta > x_2$.
        -   $(-1, +1)$: $x_1 < \theta < x_2$.
        -   $(+1, +1)$: $\theta < x_1$.
        -   $(+1, -1)$: Impossible, because $\text{sign}(x-\theta)$ is monotone.
    -   So **VC($\mathcal{H}_1$) = 1**.

2.  **$\mathcal{H}_2$ (Nearest Mean / Interval):**
    Classifier decides based on distance to two centers.
    $|x - \mu_1| - |x - \mu_2| < 0 \iff |x - \mu_1| < |x - \mu_2|$. Closer to $\mu_1$ is class $+1$ (assuming sign convention).
    This essentially defines simple intervals or unions?
    In 1D, the decision boundary is the perpendicular bisector (midpoint) between $\mu_1$ and $\mu_2$.
    The condition $|x - \mu_1| < |x - \mu_2|$ means $x$ is closer to $\mu_1$.
    -   If $\mu_1 < \mu_2$, $x < \frac{\mu_1+\mu_2}{2}$. (Class +1 on left).
    -   If $\mu_1 > \mu_2$, $x > \frac{\mu_1+\mu_2}{2}$. (Class +1 on right).
    So this class effectively is "Thresholds in either direction".
    -   Checking 2 points $x_1 < x_2$:
        -   $(+1, -1)$: Use $\mu_1 < \mu_2$ with split in between.
        -   $(-1, +1)$: Use $\mu_1 > \mu_2$ with split in between.
        -   $(+1, +1)$: Put both $\mu$ far right? No, if $\mu_1 = \mu_2$, score is 0. If $\mu_1 = x_1, \mu_2 = \text{far}$, then $x_1$ is closer.
    This class is equivalent to linear classifiers in 1D (unions of rays).
    **VC($\mathcal{H}_2$) = 2**.

3.  **$\mathcal{H}_3$ (Linear Hyperplanes in $\mathbb{R}^d$):**
    This is the standard set of linear classifiers in $d$ dimensions.
    The VC dimension of affine hyperplanes in $\mathbb{R}^d$ is **$d+1$**.

## b) Statistical Consistency
ERM is statistically consistent (converges to the best in class) if the VC dimension is **finite**.
-   **$\mathcal{H}_1$**: VC=1 (Finite) $\implies$ Consistent.
-   **$\mathcal{H}_2$**: VC=2 (Finite) $\implies$ Consistent.
-   **$\mathcal{H}_3$**: VC=d+1 (Finite for finite $d$) $\implies$ Consistent.

All three algorithms are statistically consistent (w.r.t their hypothesis class).

## Related Concepts
- [[vc-dimension]]
- [[statistical-consistency]]
- [[linear-classifier]]
