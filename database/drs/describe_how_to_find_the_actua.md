---
id: drs_057
course: Dynamics and Control of Networks
tags: [shortest-paths, dijkstra-algorithm, path-reconstruction, graph-theory]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe how to find the actual shortest paths. Assume first single shortest paths, then generalize to possible multiple shortest paths.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Shortest path reconstruction using a predecessor (parent) pointer array and extending it to a list of predecessors for multiple paths.

## Explanation
Finding the distance (the value of the shortest path) is computationally distinct from finding the actual path (the sequence of nodes). Most algorithms, such as **Dijkstra’s** or **Breadth-First Search (BFS)**, compute the minimum distance $d(s, v)$ from a source $s$ to all target nodes $v$. To reconstruct the actual path, we must record the traversal history during the algorithm's execution.

**1. Single Shortest Path:**
In the case where we only require a single shortest path, we maintain an auxiliary array called the **predecessor array**, often denoted as $p[v]$ or $\pi[v]$. Whenever an edge $(u, v)$ is relaxed—meaning we find a shorter way to reach $v$ via $u$ such that $d(s, u) + w(u,v) < d(s, v)$—we set $p[v] = u$. Once the algorithm terminates, the path is reconstructed in reverse by following the pointers from the target node $t$ back to the source $s$: $t \to p[t] \to p[p[t]] \dots \to s$. Reversing this sequence yields the shortest path.

**2. Multiple Shortest Paths:**
In many networks, multiple paths may share the same minimum total weight. To generalize the approach, the predecessor array $p[v]$ is transformed into a **predecessor list** (or a set of parents). During the relaxation step, if $d(s, u) + w(u,v) < d(s, v)$, we update the distance and reset the list: $p[v] = \{u\}$. However, if $d(s, u) + w(u,v) = d(s, v)$, we **append** $u$ to the existing list: $p[v] = p[v] \cup \{u\}$. The result is a Directed Acyclic Graph (DAG) representing all shortest paths. To retrieve all paths, one can perform a Depth-First Search (DFS) or backtracking starting from the target $t$ through all nodes in the predecessor lists until $s$ is reached.

### Steps / Derivation
1. **Initialize:** Set $d(s) = 0$, $d(v) = \infty$ for all other $v$, and $p[v] = \text{empty list}$.
2. **Relaxation:** For an edge $(u, v)$ with weight $w_{uv}$:
   - If $d(u) + w_{uv} < d(v)$:
     - Update $d(v) = d(u) + w_{uv}$
     - Update $p[v] = \{u\}$
   - If $d(u) + w_{uv} == d(v)$:
     - Update $p[v] = p[v] \cup \{u\}$
3. **Reconstruction:**
   - To find one path: Follow $p[v]$ until reaching $s$.
   - To find all paths: Perform a recursive traversal of the predecessor sets.
$$
\text{Path}(v) = \{(u, v) : u \in p[v]\}
$$

## Related Concepts
- [[dijkstra_algorithm]]
- [[breadth_first_search]]
- [[predecessor_graph]]