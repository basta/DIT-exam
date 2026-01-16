---
id: drs_074
course: Dynamics and Control of Networks
tags: [clustering-algorithms, network-topology, unsupervised-learning]
difficulty: 2
type: open
status: to_learn
---

# Question
Define hierarchical clustering. What is a dendrogram? Explain the similarity-based hierarchical clustering with single-, complete- and average-linkage clustering.

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** See detailed explanation below for definitions of hierarchical clustering, dendrograms, and linkage methods.

## Explanation
**Hierarchical Clustering** is a method of cluster analysis which seeks to build a hierarchy of clusters. Unlike partition-based methods like K-means, it does not require a pre-defined number of clusters. Instead, it groups data points into a tree-like structure based on their proximity. This is typically achieved via an **agglomerative** (bottom-up) approach, where each observation starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.

A **Dendrogram** is a diagrammatic representation of this hierarchical structure. It is a tree-like diagram where the individual nodes are at the bottom and the vertical axis represents the distance or dissimilarity at which two clusters were merged. By cutting the dendrogram at a specific height (threshold), a partition of the data into a specific number of clusters is obtained.

The behavior of hierarchical clustering is determined by the **Linkage Criterion**, which defines how the distance between two sets (clusters) of observations is calculated:

1.  **Single-Linkage (Nearest Neighbor):** The distance between two clusters $A$ and $B$ is defined as the minimum distance between any single point in $A$ and any single point in $B$. 
    $$ d(A, B) = \min_{x \in A, y \in B} d(x, y) $$
    This method can result in "chaining," where clusters are forced together because of a single pair of close points, even if the overall shapes are distinct.

2.  **Complete-Linkage (Farthest Neighbor):** The distance is defined as the maximum distance between a point in $A$ and a point in $B$.
    $$ d(A, B) = \max_{x \in A, y \in B} d(x, y) $$
    This tends to produce more compact, spherical clusters of roughly equal diameters.

3.  **Average-Linkage (UPGMA):** The distance is defined as the average of all distances between every pair of points where one point is taken from each cluster.
    $$ d(A, B) = \frac{1}{|A| \cdot |B|} \sum_{x \in A} \sum_{y \in B} d(x, y) $$
    This provides a compromise between the extremes of single and complete linkage.

### Steps / Derivation
1. **Initialize:** Assign each data point to its own cluster (N clusters for N points).
2. **Compute Similarity:** Calculate the distance matrix containing the distances between all pairs of clusters using chosen linkage (e.g., Euclidean distance).
3. **Merge:** Find the two clusters with the smallest inter-cluster distance and merge them into a single cluster.
4. **Iterate:** Update the distance matrix to reflect the new cluster structure.
5. **Terminate:** Repeat steps 2-4 until all points are merged into a single root cluster, forming the dendrogram.

## Related Concepts
- [[community_detection]]
- [[modularity_optimization]]
- [[agglomerative_nesting]]