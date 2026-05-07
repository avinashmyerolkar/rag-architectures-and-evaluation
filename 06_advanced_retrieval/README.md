# Module 6 — Advanced Retrieval Techniques

> **What:** Retrieval strategies that go beyond simple similarity search.
> **Why:** Real-world queries are ambiguous, multi-faceted, and require context-aware retrieval.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_contextual_compression.ipynb` | LLM-based and embeddings-based document compressors |
| 2 | `02_parent_document_retriever.ipynb` | Index small chunks, retrieve large parent context |
| 3 | `03_self_query_retriever.ipynb` | Natural-language metadata filtering via structured query generation |
| 4 | `04_multi_query_retriever.ipynb` | Generate query variants to overcome single-query blind spots |

## Key Concepts

- **Contextual Compression:** Strip irrelevant passages from retrieved docs before passing to LLM
- **Parent-Doc Retriever:** Small chunks = precise match; large parent = rich context for generation
- **Self-Query:** LLM converts natural language into structured filters (`year > 2022 AND author = "Smith"`)
- **Multi-Query:** One query often misses; generating 3–5 variants and merging results improves recall significantly
