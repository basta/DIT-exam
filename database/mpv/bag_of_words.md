---
id: mpv_015
course: Methods of Computer Vision
tags: [bag-of-words, idf, codebook, sparsity, retrieval]
difficulty: 4
type: open
status: to_learn
---

# Question
How is the **Bag-of-Words representation** (histogram) constructed? What is the **idf weighting**, how is it estimated, and what problem is it handling? How is **image-to-image similarity** estimated with the BoW representation? How is the **codebook size** affecting the sparsity of the BoW histogram and what are other factors affecting its sparsity?

---
# Solution

## Constructing the BoW Histogram
1. **Visual vocabulary (codebook).** Cluster a large pool of local descriptors (e.g., SIFT) from a training set into $K$ clusters by $k$-means (or hierarchical $k$-means / approximate $k$-means). The $K$ cluster centers are the **visual words**.
2. **Assignment.** For each local descriptor $\mathbf{x}$ of an image, find its nearest visual word $w(\mathbf{x}) \in \{1, \dots, K\}$.
3. **Histogram.** Count: $\mathbf{h} \in \mathbb{R}^K$ with $h_i = \#\{\text{descriptors assigned to word }i\}$.
4. **(Optional) Normalization.** $L_2$ or $L_1$ normalize $\mathbf{h}$ to remove dependence on the number of detected features.

Soft assignment, multiple-NN assignment or hierarchical vocabularies can be used to improve quantization.

## tf-idf Weighting
Plain counts overweight visual words that appear in *many* images and carry little information (analogous to stop words like "the"). The **inverse document frequency** weight downweights them:
$$
\text{idf}(i) = \log \frac{N}{n_i},
$$
where $N$ is the total number of database images and $n_i$ is the number of database images containing word $i$ at least once. Estimated offline from the database. The tf component is the count $h_i$ (sometimes log-scaled).

**Weighted vector:** $\tilde{h}_i = h_i \cdot \text{idf}(i)$, then $L_2$-normalize.

idf handles **non-discriminativeness of common words**: words that fire on every image (sky, repetitive patterns) dominate the dot product without bringing useful information; idf attenuates their contribution.

## Image-to-Image Similarity
With $L_2$-normalized weighted vectors $\tilde{\mathbf{h}}_q, \tilde{\mathbf{h}}_d$, similarity is the cosine
$$
s(q, d) = \langle \tilde{\mathbf{h}}_q, \tilde{\mathbf{h}}_d \rangle = \sum_i \tilde{h}_q^{(i)} \tilde{h}_d^{(i)}.
$$
Equivalently, the Euclidean distance $\|\tilde{\mathbf{h}}_q - \tilde{\mathbf{h}}_d\|_2^2 = 2 - 2 s(q, d)$.

Because each $\tilde{\mathbf{h}}$ is very sparse (most words don't appear), the dot product can be computed efficiently using an **inverted file**: only words present in $q$ are looked up; only their posting lists contribute.

## Effect of Codebook Size $K$ on Sparsity
- A typical image has $F \approx 10^3$–$10^4$ local features.
- The histogram has $K$ bins, of which **at most $F$** can be non-zero (each feature votes for exactly one bin in hard assignment, often into a bin that already has votes from other features).
- **Small $K$** (e.g., $K = 100$): essentially all bins are non-zero → dense histogram, low discriminative power, many random collisions, slower retrieval (inverted file useless).
- **Large $K$** (e.g., $K = 10^5$–$10^6$): far fewer features than bins → highly sparse histogram, descriptors are quantized more finely → more discriminative, faster retrieval, but quantization noise increases (true matches may be assigned to *different* nearby words → loss of recall).

## Other Factors Affecting Sparsity
- **Number of detected features $F$ per image** — more features → more populated bins → less sparse.
- **Assignment scheme** — soft / multiple assignment (each descriptor votes for several nearest words) reduces sparsity (more non-zeros) but improves robustness to quantization.
- **Image content / repeatability** — repetitive textures land many descriptors in the same bin → fewer non-zeros, but each bin has a large count.
- **Vocabulary quality** — well-spread centroids give more uniform usage of bins; degenerate vocabularies concentrate descriptors in a few bins.

## Related Concepts
- [[visual-vocabulary]]
- [[tf-idf]]
- [[inverted-file]]
- [[quantization]]
- [[soft-assignment]]
