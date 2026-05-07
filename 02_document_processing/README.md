# Module 2 — Document Processing and Chunking

> **What:** Preparing raw documents so they can be reliably retrieved.
> **Why:** Chunking strategy is the single biggest lever on retrieval quality — chunk too large and you dilute signal; too small and you lose context.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_document_loaders.ipynb` | LangChain loaders for PDFs, web pages, CSV, JSON, and databases |
| 2 | `02_text_splitting_strategies.ipynb` | Recursive, character, semantic, Markdown, and code splitters compared |
| 3 | `03_chunking_best_practices.ipynb` | Optimal chunk sizes, overlap strategies, and benchmarks |
| 4 | `04_metadata_management.ipynb` | Attaching, storing, and filtering metadata for precise retrieval |

## Key Concepts

- **Chunk Size:** Typical sweet spot is 256–1024 tokens depending on embedding model and use case
- **Overlap:** 10–20% overlap prevents context from being cut at chunk boundaries
- **Metadata:** Source, page number, date — enables filtered retrieval without re-embedding
