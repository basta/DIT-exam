---
id: 2016_ssu_005
course: Statistical Machine Learning
tags: [reinforcement-learning, greedy-policy, value-function]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(2p) Give a formal definition of a *greedy* policy $\pi(a|s)$ by means of the corresponding state-value function $v_\pi(s)$.

---
# Solution
A greedy policy $\pi(a|s)$ with respect to a state-value function $v_\pi(s)$ is a deterministic policy that selects the action maximizing the expected return from the current state, assuming the current value estimates $v_\pi$ for the successor states are correct.
Formally, assuming a partial model $p(s'|s, a)$ and reward $r(s, a, s')$ (or expected reward $R(s, a)$), the greedy policy is defined as:

$$ \pi(a|s) = \begin{cases} 1 & \text{if } a = \arg\max_{a' \in \mathcal{A}} \sum_{s' \in \mathcal{S}} p(s'|s, a') [r(s, a', s') + \gamma v_\pi(s')] \\ 0 & \text{otherwise} \end{cases} $$

If we denote the action-value function as $q_\pi(s, a) = \sum_{s'} p(s'|s, a) [r(s, a, s') + \gamma v_\pi(s')]$, then:
$$ \pi(s) = \arg\max_{a \in \mathcal{A}} q_\pi(s, a) $$

*Note: The question asks for the definition "by means of the corresponding state-value function", implying the use of the Bellman consistency equation to relate $v$ to the action selection.*

## Related Concepts
- [[reinforcement-learning]]
- [[bellman-equation]]
- [[policy-iteration]]
