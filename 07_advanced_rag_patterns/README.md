# Module 7 — Advanced RAG Patterns

> **What:** Architectural patterns that push retrieval quality beyond standard pipelines.
> **Why:** Production RAG systems face failure modes — stale retrieval, hallucinated answers, missing context — that require these patterns to handle robustly.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_rag_fusion_rrf.ipynb` | Multi-query retrieval + Reciprocal Rank Fusion for re-ranking |
| 2 | `02_hyde.ipynb` | Hypothetical Document Embeddings — generate then retrieve |
| 3 | `03_corrective_rag.ipynb` | CRAG: detect retrieval failure and fall back to web search |
| 4 | `04_self_rag.ipynb` | Self-reflective generation with retrieve, critique, and regenerate loops |
| 5 | `05_graph_rag.ipynb` | Knowledge graph construction and graph-guided retrieval |

## Key Concepts

- **HyDE:** Ask LLM to write a hypothetical answer, embed that — often retrieves better than embedding the raw question
- **CRAG:** Adds a retrieval grader; if score is low, triggers web search as fallback
- **Self-RAG:** Model decides when to retrieve, critiques its own output, and can regenerate
- **Graph RAG:** Captures entity relationships that chunk-based retrieval cannot express
