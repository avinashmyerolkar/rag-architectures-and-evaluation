# Module 3 — Embeddings and Vector Representations

> **What:** Converting text into dense numerical vectors that capture semantic meaning.
> **Why:** The quality of your embeddings is the ceiling on retrieval quality — a better model finds better matches.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_how_embeddings_work.ipynb` | Vector spaces, cosine similarity, dot product, and Euclidean distance |
| 2 | `02_embedding_models_overview.ipynb` | OpenAI `text-embedding-3`, HuggingFace MTEB leaders, Cohere Embed |
| 3 | `03_choosing_right_embedding_model.ipynb` | Cost vs quality trade-offs, benchmarking on your own data |
| 4 | `04_langchain_embeddings_implementation.ipynb` | Drop-in LangChain `Embeddings` interface with multiple providers |

## Key Concepts

- **Cosine Similarity:** Measures angle between vectors — independent of magnitude, preferred for text
- **MTEB Benchmark:** Standard leaderboard for comparing embedding model quality
- **Dimensionality:** Higher dims (1536, 3072) = more expressive but slower and costlier
