---
id: drs_009
course: Dynamics and Control of Networks
tags: [citation-networks, bibliometrics, similarity-measures, graph-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
Compare the co-citation and bibliographic coupling.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Co-citation and bibliographic coupling are both similarity measures used in citation network analysis to determine the relatedness of papers, but they differ in their temporal stability and the direction of the citation links they analyze.

## Explanation
In the study of complex networks, specifically citation networks, we represent papers as nodes and citations as directed edges. Since edges are generally directed from newer papers to older ones, we use specific metrics to quantify how "related" two nodes are based on their connectivity patterns.

**Bibliographic Coupling** occurs when two works, $A$ and $B$, both cite the same third work, $C$. The degree of bibliographic coupling is defined by the number of shared references between two papers. Mathematically, if $O_i$ is the set of papers cited by $i$, the coupling strength between $i$ and $j$ is $|O_i \cap O_j|$. Notably, bibliographic coupling is a **static** measure. Once two papers are published, their reference lists are fixed; therefore, the bibliographic coupling strength between them never changes over time. It is a prospective measure, often used to identify researchers working in the same field at a specific point in time.

**Co-citation**, on the other hand, occurs when two works, $A$ and $B$, are both cited by a third work, $C$. The co-citation strength is the number of papers that cite both $A$ and $B$. If $I_i$ is the set of papers that cite paper $i$, the co-citation strength is $|I_i \cap I_j|$. Unlike bibliographic coupling, co-citation is a **dynamic** measure. Even decades after papers $A$ and $B$ are published, their co-citation strength can increase as new research continues to cite them together. This metric is retrospective and is frequently used to map the intellectual structure or "core" of a scientific discipline as perceived by the community over time.

### Steps / Derivation
1. **Define the Adjacency Matrix:** Let $A$ be the adjacency matrix of a citation network where $A_{ij} = 1$ if paper $i$ cites paper $j$, and $0$ otherwise.
2. **Bibliographic Coupling (O):** Represented by the matrix $C = AA^T$. The element $C_{ij}$ indicates the number of common neighbors paper $i$ and $j$ point to.
$$
C_{ij} = \sum_{k} A_{ik} A_{jk}
$$
3. **Co-citation (P):** Represented by the matrix $D = A^T A$. The element $D_{ij}$ indicates the number of common neighbors that point to both $i$ and $j$.
$$
D_{ij} = \sum_{k} A_{ki} A_{kj}
$$
4. **Conclusion:** Bibliographic coupling represents shared "out-neighbors," while co-citation represents shared "in-neighbors."

## Related Concepts
- [[directed_acyclic_graphs]]
- [[adjacency_matrix_properties]]
- [[jaccard_similarity_coefficient]]