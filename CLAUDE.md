# CLAUDE.md — Project Context

## What this repo is

A structured, module-by-module deep dive into **Retrieval-Augmented Generation (RAG)** covering fundamentals through production-grade agentic systems and evaluation. Built for two audiences: recruiters reviewing the research depth, and the open-source community learning RAG.

## Repo layout

Nine topic folders live at the **root level** (so GitHub's file browser shows them immediately on the landing page):

```
01_rag_fundamentals/
02_document_processing/
03_embeddings/
04_vector_stores/
05_basic_retrieval/
06_advanced_retrieval/
07_advanced_rag_patterns/
08_agentic_rag_langgraph/
09_rag_evaluation_ragas/
src/          ← shared Python utilities (loaders, retrievers, evaluators, utils)
data/         ← sample documents for notebook demos
assets/       ← diagrams and images
```

Each module folder has its own `README.md` as the module's reference document, plus Jupyter notebooks for hands-on code.

## Content conventions

- Each module `README.md` is the **authoritative theory reference** for that topic — written from the author's own research notes, not copied from docs
- Notebooks are numbered (`01_`, `02_`, ...) and must run top-to-bottom without manual steps
- API keys loaded via `python-dotenv` from `.env` — never hardcoded
- Clear all notebook output before committing

## Research notes already incorporated

| Module | Notes status |
|--------|-------------|
| `04_vector_stores/` | Full notes incorporated: What/Why/How of vector stores, IVF clustering mechanics, HNSW layered graph mechanics, ChromaDB |
| `08_agentic_rag_langgraph/` | Full notes incorporated: Naive RAG limitations, CRAG, Self-RAG, Agentic RAG properties, ReAct loop, query phase, retrieval phase (where/how/when), relevancy check, response verification, memory, dynamic augmentation, graceful fallback |

## Tech stack

LangChain · LangGraph · OpenAI · ChromaDB · FAISS · RAGAS · sentence-transformers · rank-bm25

## Adding new research notes

When the user provides research notes for a module:
1. Update that module's `README.md` — keep the What/Why/Key Concepts/Notebooks/Takeaways structure
2. Update this file's "Research notes already incorporated" table
3. No need to update the root `README.md` unless a new module or notebook is added
