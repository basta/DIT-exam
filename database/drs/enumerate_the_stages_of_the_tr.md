---
id: drs_081
course: Dynamics and Control of Networks
tags: [web-search, ranking-algorithms, page-rank, information-retrieval]
difficulty: 3
type: open
status: to_learn
---

# Question
Enumerate the stages of the traditional (offline) web search. Explain how the algorithms used in modern web search engines such as Google differ from the traditional web search.

## Options
N/A (This is an open-ended descriptive question)

---
# Solution
**Correct Answer:** The traditional search process follows three main stages: Crawling, Indexing, and Query Processing (Ranking). Modern search engines differ primarily by utilizing the link structure of the network (global centrality) rather than relying solely on local content similarity.

## Explanation
The traditional (classical information retrieval) approach to web search primarily focuses on the content of individual documents. The three stages are:
1. **Crawling:** Specialized software (spiders/bots) traverses the web by following links from one page to another to discover content.
2. **Indexing:** The engine creates an "inverted index," which is a mapping from keywords to the documents containing those words. This behaves like the index at the back of a textbook.
3. **Query Processing/Ranking:** When a user enters a query, the engine identifies all documents containing those terms and ranks them based on relevance scores, traditionally using measures like TF-IDF (Term Frequency-Inverse Document Frequency).

The fundamental shift introduced by modern engines like Google is the transition from **content-based ranking** to **network-based ranking**. Traditional methods suffered as the web grew because keyword matching was easily manipulated (spammed) and did not account for the quality or authority of a page. 

Modern algorithms, most notably **PageRank**, treat the web as a directed graph $G = (V, E)$. They interpret a hyperlink from page $i$ to page $j$ as a "vote" of confidence. The importance of a page is defined recursively: a page is important if it is pointed to by other important pages. This is mathematically represented as the stationary distribution of a random walk on the graph, often expressed as:
$$
P(i) = \frac{1-d}{N} + d \sum_{j \in M(i)} \frac{P(j)}{L(j)}
$$
where $d$ is a damping factor, $N$ is the total number of nodes, $M(i)$ is the set of pages linking to $i$, and $L(j)$ is the number of out-links from $j$. This leverages the **eigenvector centrality** of the network dynamics to provide a global objective measure of quality that is independent of the specific query.

### Steps / Derivation
1. **Identify the Traditional Pipeline:** Define Crawling (discovery), Indexing (storage/mapping), and Ranking (matching).
2. **Contrast with Network Logic:** Explain that traditional ranking used local text statistics (TF-IDF), while modern ranking uses the global topology of the web graph.
3. **Apply Algebraic Connectivity:** Describe how modern engines solve the "authority" problem by calculating the principal eigenvector of a modified adjacency matrix (the Google Matrix).

## Related Concepts
- [[pagerank_algorithm]]
- [[inverted_index]]
- [[eigenvector_centrality]]