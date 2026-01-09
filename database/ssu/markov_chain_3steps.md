---
id: ssu_batch7_003
course: Statistical Machine Learning
tags: [markov-chain, transition-matrix, numerical-calculation]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(3p) Consider a homogeneous Markov chain model with three states $k = 1, 2, 3$ and the transition probability matrix
$$ P_{k, k'} = 0.5 \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix} = \begin{pmatrix} 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 \\ 0 & 0.5 & 1 \end{pmatrix} $$
(Note: The matrix notation $P_{k, k'}$ usually implies row $k$ to col $k'$? Or col $k$ to row $k'$? Let's check stochasticity.
Rows must sum to 1?
Row 1: $0.5+0+0 = 0.5 \neq 1$.
Row 3: $0+0.5+1 = 1.5 \neq 1$.
Columns sum to 1?
Col 1: $0.5+0.5+0 = 1$. OK.
Col 2: $0+0.5+0.5 = 1$. OK.
Col 3: $0+0+1 = 1$. OK.
So $P$ is a column-stochastic matrix where $P_{ij} = P(s_{t+1}=i \mid s_t=j)$.
State vector $v_{t+1} = P v_t$. Or $v_{t+1} = v_t P$ if row vectors.
Given the columns sum to 1, this represents $P(i \mid j)$.
We are given row index $k$ and column index $k'$.
Usually $P_{ij} = P(j \mid i)$ for row vectors. But here columns sum to 1.
So we assume $P_{ij} = P(\text{to } i \mid \text{from } j)$.
State update: $\mathbf{p}_{t+1} = P \mathbf{p}_t$ (matrix-vector multiplication).

It starts in state $k=1$. Compute the marginal probabilities for its state after three transitions.

---
# Solution
Let $\mathbf{p}_0 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ (Starting in state 1).
Transition Matrix $M = \begin{pmatrix} 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 \\ 0 & 0.5 & 1 \end{pmatrix}$.

**Step 1:**
$$ \mathbf{p}_1 = M \mathbf{p}_0 = \begin{pmatrix} 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 \\ 0 & 0.5 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0.5 \\ 0.5 \\ 0 \end{pmatrix} $$

**Step 2:**
$$ \mathbf{p}_2 = M \mathbf{p}_1 = \begin{pmatrix} 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 \\ 0 & 0.5 & 1 \end{pmatrix} \begin{pmatrix} 0.5 \\ 0.5 \\ 0 \end{pmatrix} $$
Row 1: $0.5(0.5) = 0.25$
Row 2: $0.5(0.5) + 0.5(0.5) = 0.25 + 0.25 = 0.5$
Row 3: $0(0.5) + 0.5(0.5) + 1(0) = 0.25$
$$ \mathbf{p}_2 = \begin{pmatrix} 0.25 \\ 0.5 \\ 0.25 \end{pmatrix} $$
Check sum: $0.25+0.5+0.25 = 1$. Correct.

**Step 3:**
$$ \mathbf{p}_3 = M \mathbf{p}_2 = \begin{pmatrix} 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 \\ 0 & 0.5 & 1 \end{pmatrix} \begin{pmatrix} 0.25 \\ 0.5 \\ 0.25 \end{pmatrix} $$
Row 1: $0.5(0.25) = 0.125$
Row 2: $0.5(0.25) + 0.5(0.5) = 0.125 + 0.25 = 0.375$
Row 3: $0(0.25) + 0.5(0.5) + 1(0.25) = 0.25 + 0.25 = 0.5$
$$ \mathbf{p}_3 = \begin{pmatrix} 0.125 \\ 0.375 \\ 0.5 \end{pmatrix} $$
Check sum: $0.125 + 0.375 + 0.5 = 1$. Correct.

**Result:**
After 3 transitions, the marginal probabilities are:
$P(k=1) = 0.125$
$P(k=2) = 0.375$
$P(k=3) = 0.5$

## Related Concepts
- [[markov-chain]]
- [[matrix-multiplication]]
- [[marginal-probability]]
