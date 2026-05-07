# Module 5 — Basic Retrieval Techniques

> **What:** The core methods for finding relevant documents given a query.
> **Why:** Most RAG systems start here — understanding these fundamentals is essential before adding complexity.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_similarity_search_fundamentals.ipynb` | k-NN search, top-k selection, and score interpretation |
| 2 | `02_similarity_score_thresholds.ipynb` | Filtering low-confidence results dynamically |
| 3 | `03_mmr_retrieval.ipynb` | Maximal Marginal Relevance — balancing relevance and diversity |
| 4 | `04_hybrid_search.ipynb` | Dense + sparse (BM25) fusion with reciprocal rank fusion |
| 5 | `05_ensemble_retriever.ipynb` | Combining multiple retrievers with weighted aggregation |

## Key Concepts

- **MMR:** Penalizes redundant results — retrieves diverse, relevant documents
- **BM25:** Classic keyword-based ranking — excels at exact match and rare terms
- **Hybrid Search:** Dense vectors catch semantic matches; BM25 catches exact keywords — combining both beats either alone
