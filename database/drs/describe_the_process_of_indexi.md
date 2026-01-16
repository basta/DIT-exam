---
id: drs_083
course: Dynamics and Control of Networks
tags: [web-search, information-retrieval, indexing-algorithms]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the process of indexing in web search, both the simple version and its possible extensions.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Open-ended descriptive response regarding Inverted Indices and their enhancements.

## Explanation
Indexing is the core process that allows a search engine to perform sub-second queries over billions of documents. Instead of scanning every document for a keyword (which would be $O(N)$ where $N$ is the corpus size), the engine pre-computes a data structure that maps terms to the documents containing them.

### The Simple Version: The Inverted Index
The fundamental structure is the **Inverted Index**. Imagine a table where each row corresponds to a unique word (a term) found in the crawl. For each term, there is a list (often called a "postings list") containing the IDs of all documents where that word appears.
- **Vocabulary:** A sorted list of all unique terms.
- **Postings:** A linked list or variable-length array for each term containing Document IDs ($DocID$).

### Extensions and Advanced Features
The simple model is insufficient for modern relevance ranking and complex queries. Extensions include:
1. **Frequency Information:** Storing the Term Frequency ($tf$) within each posting. This is crucial for calculating weights like $tf-idf$ or using probabilistic models like BM25.
2. **Proximity/Position Indexing:** Rather than just storing the $DocID$, the index stores the exact positions of the word in the text. This allows for phrase searches (e.g., "Network Dynamics") and proximity operators.
3. **Metadata/Fields:** Indices are often partitioned by fields (title, headers, body, URL) to give more weight to terms appearing in prominent locations.
4. **Compression:** Postings lists are massive. Techniques like Delta Encoding (storing $DocID_{n} - DocID_{n-1}$) and variable-byte encoding are used to minimize disk I/O.
5. **Distributed Indexing:** The index is partitioned (sharded) across thousands of nodes, either by document (local index) or by term (global index), to allow for parallel query processing.

### Steps / Derivation
1. **Tokenization:** Convert raw HTML/text into a stream of individual tokens or words.
2. **Linguistic Processing:** Apply normalization, such as stemming (reducing "running" to "run") and removing stop words (e.g., "the", "a").
3. **Sort and Merge:**
$$
\text{Term} \rightarrow \{DocID_1, DocID_2, \dots, DocID_k\}
$$
4. **Weighting:** Calculate the importance of a term $i$ in document $j$ using schemes like:
$$
w_{i,j} = \text{tf}_{i,j} \times \log\left(\frac{N}{\text{df}_i}\right)
$$
where $N$ is the total number of documents and $\text{df}_i$ is the number of documents containing term $i$.

## Related Concepts
- [[inverted_index]]
- [[tf_idf_weighting]]
- [[search_engine_architecture]]