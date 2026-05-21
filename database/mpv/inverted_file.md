---
id: mpv_016
course: Methods of Computer Vision
tags: [inverted-file, BoW, retrieval, memory, indexing]
difficulty: 4
type: open
status: to_learn
---

# Question
What is an **inverted-file structure** and how is it used to perform retrieval with BoW? In which cases is it better to use an inverted file instead of directly storing the original BoW vectors? What are the factors affecting the memory requirements for performing retrieval on a dataset of images **with BoW and an inverted-file**? What are the factors affecting the memory requirements for performing retrieval on a dataset of images **with BoW when an inverted-file is not used**?

---
# Solution

## Inverted File (Inverted Index)
Borrowed from text retrieval. For each visual word $i \in \{1, \dots, K\}$, store a **posting list**: the IDs of database images that contain at least one feature assigned to word $i$, together with the count (or tf-idf weight, and optionally per-feature metadata such as position, scale, orientation).

```
word 1: [(img_42, 3), (img_17, 1), (img_211, 2), ...]
word 2: [(img_7,  1), (img_42, 1), ...]
...
word K: ...
```

## Retrieval with an Inverted File
1. For the query image, compute the BoW vector $\mathbf{h}_q$. Its support is the set of non-zero words $W_q$.
2. For each $i \in W_q$, look up the posting list and **accumulate** scores for every database image that appears in it: $s_d \mathrel{+}= \tilde{h}_q^{(i)} \cdot \tilde{h}_d^{(i)}$.
3. The final score $s_d$ equals the dot product $\langle \tilde{\mathbf{h}}_q, \tilde{\mathbf{h}}_d \rangle$ (assuming normalized vectors), but is computed **without** ever materializing $\tilde{\mathbf{h}}_d$ for all $d$.
4. Sort images by $s_d$ to obtain the ranked list.

Complexity: $O(\sum_{i \in W_q} |L_i|)$ where $|L_i|$ is the posting-list length.

## When the Inverted File Wins
- **Sparse** BoW vectors (large $K$, $K \gg F$): only a few thousand words are non-zero per image; an inverted file lets us touch only those.
- **Large databases** ($N$ of order $10^5$–$10^9$): storing dense $K$-dim vectors for all images is infeasible, and a brute-force dot product is too slow.
- **Many queries** with similar sparsity properties.

The inverted file is **not** beneficial when $K$ is small (dense vectors): then the posting lists are huge and contain virtually every image, so the index degenerates to the dense matrix.

## Memory Requirements

### With inverted file
- $O(K) \cdot c_w$: array of posting-list pointers, plus idf table.
- $O(F_{\text{total}}) = O(\sum_d F_d)$: each *feature* (or each (image, word) pair) contributes one entry in some posting list. Equivalently, the total number of entries equals the total number of non-zero $(d, i)$ pairs (or, if features rather than image-tf pairs are stored, the total number of features).
- Per-entry size: image ID + count (or weight) + optional per-feature metadata (position, scale, orientation). Larger if metadata is kept (e.g., for spatial verification or Hamming embedding).
- **Driving factors:** number of features per image $\bar F$, total number of images $N$, codebook size $K$ (affects pointer overhead but not the total bulk much), metadata per feature.

### Without inverted file (dense BoW vectors)
- Need to store $N$ vectors, each of dimension $K$, plus pointers.
- If stored densely: $N \cdot K \cdot c$ bytes ($c =$ bytes per component). E.g., $N = 10^6, K = 10^6, c = 4 \Rightarrow 4$ TB — infeasible.
- If stored as sparse pairs $(i, h_i)$: cost $O(\sum_d |\text{supp}(\mathbf{h}_d)|)$. This is essentially the same as the inverted file but with the *image* as the outer index instead of the *word* — equally compact, but does not support efficient query-driven lookup.
- **Driving factors:** $N$, $K$, sparsity of each BoW vector.
- Retrieval time is $O(N \cdot |W_q|)$ with sparse storage, or $O(N \cdot K)$ with dense storage — typically far worse than the inverted file because each query must touch every database image.

## Summary
- The inverted file is the standard data structure for BoW retrieval; it is essentially the *transpose* of the sparse $(image \times word)$ matrix.
- Memory: dominated by total number of features (with metadata) regardless of approach. The advantage of the inverted file is access pattern and **query speed**, not raw space.
- Use it whenever $K$ is large and BoW vectors are sparse; skip it when $K$ is small enough that brute-force dense scoring is fast.

## Related Concepts
- [[BoW]]
- [[posting-list]]
- [[tf-idf]]
- [[hamming-embedding]]
