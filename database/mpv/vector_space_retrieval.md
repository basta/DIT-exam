---
id: mpv_021
course: Methods of Computer Vision
tags: [global-descriptors, retrieval, embedding, ANN]
difficulty: 2
type: open
status: to_learn
---

# Question
For a retrieval task, what are the benefits of mapping images to a **vector space** and how is retrieval performed then?

---
# Solution

## Setting
Represent every database image (and query) as a *single* fixed-dimensional vector $\mathbf{f}(I) \in \mathbb{R}^d$ — a **global image descriptor**. Examples: VLAD, Fisher Vector, GeM-pooled CNN features, NetVLAD, CLIP embeddings.

## Retrieval Procedure
1. **Offline.** For every database image $I_d$, compute $\mathbf{f}_d = \mathbf{f}(I_d)$ and store. Usually $L_2$-normalize so cosine = dot product.
2. **Online.** Given query $q$, compute $\mathbf{f}_q$. Score each database image by similarity:
$$
s(q, d) = \langle \mathbf{f}_q, \mathbf{f}_d \rangle \quad \text{or} \quad -\|\mathbf{f}_q - \mathbf{f}_d\|_2^2.
$$
3. Return the top-$k$.
4. (Optional) **Re-rank** the top-$N$ with a more expensive method (spatial verification, local-feature matching, cross-encoder).

Top-$k$ retrieval in $\mathbb{R}^d$ is a maximum-inner-product / nearest-neighbor problem.

## Benefits
- **Single, fixed-size representation per image** — independent of how many features were detected, image resolution, etc.
- **Sub-linear retrieval** via approximate nearest neighbor (ANN) data structures:
  - **Product Quantization** (PQ, IVFPQ) — compress vectors to bytes; search in $O(\sqrt{N})$ effective steps.
  - **HNSW, FAISS-IVF, ScaNN** — graph- or tree-based ANN; query in sub-millisecond on $10^8$ vectors.
  - **LSH** — sub-linear with theoretical guarantees.
- **Memory-efficient**: PQ-coded vectors are 16–256 bytes per image → billions of images on a single server.
- **GPU-friendly** batched inner-product retrieval.
- **Aggregation across modalities**: same retrieval engine works for image, text (CLIP), audio embeddings.
- **End-to-end learnable**: the embedding can be trained directly to optimize retrieval metrics (triplet loss, AP loss).
- **Composable**: vector arithmetic enables query expansion, aggregation of multiple queries, semantic search.

## Trade-offs
- One global vector may miss local detail (clutter, occlusion, sub-image search) — partial-matching tasks need local features or re-ranking.
- Quality is bounded by what the embedding network was trained for.
- ANN methods are approximate — recall vs. memory/latency trade-off.

## Related Concepts
- [[ANN]]
- [[product-quantization]]
- [[HNSW]]
- [[NetVLAD]]
- [[CLIP]]
