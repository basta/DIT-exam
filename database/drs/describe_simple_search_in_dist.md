---
id: drs_084
course: Dynamics and Control of Networks
tags: [distributed-systems, search-complexity, information-retrieval]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe simple search in distributed databases. What is its complexity if the file is present only on a single computer in the network? How does the complexity change if the file exists on a fixed fraction of computers in the network?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** For a single instance, the complexity is $O(N)$. For a fixed fraction $f$, the complexity is $O(1)$.

## Explanation
Simple search in a distributed database (often modeled as a peer-to-peer network or a decentralized system without a global index) typically involves a broadcast or "flooding" mechanism where a query is sent through the network until the desired file (or resource) is located. In this context, complexity is usually measured by the number of nodes that must be queried or the number of messages generated to find the target.

If a specific file exists on only a single computer in a network of $N$ computers, the search is an unstructured probe. In the worst-case scenario, the search must visit every node to guarantee finding the file. Even if we consider the average case in a random search, on average, one would need to check approximately $N/2$ nodes. Therefore, the search complexity scales linearly with the size of the network: $O(N)$. This makes simple broadcast search inefficient for very large scales when the resource is rare.

However, if the file exists on a fixed fraction $f$ of the computers (where $0 < f < 1$), the dynamics of the search change significantly. In this scenario, the probability that any randomly selected node contains the file is $f$. The probability that a file is *not* found after querying $k$ independent nodes is $(1-f)^k$. To ensure a successful find with a constant probability (e.g., $95\%$), the number of nodes $k$ required does not depend on the total number of nodes $N$ in the network, as long as $N$ is sufficiently large. Specifically, $k \approx \frac{\ln(1-P)}{\ln(1-f)}$. Since $f$ is a constant fraction, the number of steps required to find the file is a constant, resulting in a complexity of $O(1)$ relative to the network size $N$.

### Steps / Derivation
1. **Case 1: Single Instance.** 
   The total number of nodes is $N$. If the file is only at one location, the probability of finding it in $k$ searches (without replacement) is $k/N$. To find it with certainty, $k$ must equal $N$.
   $$
   Complexity = O(N)
   $$

2. **Case 2: Fixed Fraction.**
   Let $f$ be the fraction of nodes containing the file (e.g., $f = 0.01$ for 1%). 
   The probability $P$ of failing to find the file after $k$ random samples is:
   $$
   P(fail) = (1 - f)^k
   $$

3. **Determining $k$ for Success.**
   To achieve a target success probability $S = 1 - P(fail)$:
   $$
   1 - S = (1 - f)^k \implies \ln(1 - S) = k \ln(1 - f) \implies k = \frac{\ln(1 - S)}{\ln(1 - f)}
   $$
   Since $S$ and $f$ are constants, $k$ is a constant independent of $N$.
   $$
   Complexity = O(1)
   $$

## Related Concepts
- [[distributed_hash_tables]]
- [[flooding_algorithms]]
- [[random_walks_on_graphs]]