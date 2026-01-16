---
id: drs_082
course: Dynamics and Control of Networks
tags: [web-crawling, graph-traversal, information-retrieval, network-topology]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain the web crawling procedure. Give examples of advanced techniques that facilitate the web crawling process.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Web crawling is the automated process of traversing the World Wide Web to index content. Advanced techniques include focused crawling, distributed crawling, and politeness policies.

## Explanation
Web crawling is the systematic process by which "bots" or "spiders" browse the World Wide Web to create a copy of all visited pages for later processing by a search engine. At its core, the World Wide Web can be modeled as a directed graph $G = (V, E)$, where $V$ represents the set of web pages (nodes) and $E$ represents the hyperlinks (edges) connecting them.

The basic procedure involves:
1. **Seed Selection:** Starting with a list of known URLs (seeds).
2. **Queueing:** Adding these URLs to a frontier (a "to-visit" queue).
3. **Fetching:** Downloading the page content.
4. **Parsing:** Extracting new links from the page.
5. **Recursion:** Adding new, unvisited links back into the frontier.

In the context of network dynamics, the efficiency of this process depends on the traversal strategy. A Breadth-First Search (BFS) is often used to ensure discovery of high-authority pages, while Depth-First Search (DFS) is rarely used due to the risk of getting stuck in deep, irrelevant sub-structures.

Advanced techniques used to optimize this process include:
- **Focused Crawling:** Instead of an exhaustive search, the crawler uses a classifier to determine the relevance of a page before following its links, effectively pruning the graph.
- **Distributed Crawling:** Utilizing multiple nodes to crawl different segments of the web simultaneously. This requires a hashing function to map URLs to specific crawlers to avoid duplication.
- **Incremental Crawling:** Periodically revisiting pages to update the index based on the estimated change frequency $\lambda$ of a page.
- **Politeness and Robots.txt:** Implementing delays and respecting server-side constraints to prevent Denial of Service (DoS) effects on target servers.

### Steps / Derivation
1. **Selection:** A URL is picked from the Frontier $Q$.
2. **DNS Resolution:** The hostname is resolved to an IP address.
3. **Robot Exclusion:** Check `robots.txt` for permissions.
4. **Fetch and Parse:** The HTML is fetched; links are extracted and normalized.
5. **Duplicate Detection:** Fingerprinting (e.g., using Shingling or Min-Hash) is performed to ensure the same content isn't indexed twice.
$$
P(page) = \frac{1 - d}{N} + d \sum_{i \in Inbound} \frac{PR(i)}{C(i)}
$$
*(Note: PageRank is often used to prioritize the crawl frontier).*

## Related Concepts
- [[page_rank_algorithm]]
- [[graph_traversal_strategies]]
- [[web_graph_topology]]