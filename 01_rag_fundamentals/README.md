# Module 1 — RAG Fundamentals and Architecture

> **What:** Core concepts behind Retrieval-Augmented Generation.
> **Why:** Before building pipelines, you need a clear mental model of every component and why RAG outperforms alternatives in many scenarios.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_introduction_to_rag.ipynb` | What RAG is, problems it solves (hallucinations, knowledge cutoffs), and when to use it |
| 2 | `02_core_components_and_data_flow.ipynb` | End-to-end flow: Knowledge Base → Chunking → Embeddings → Retriever → Generator |
| 3 | `03_rag_vs_finetuning_vs_prompt_engineering.ipynb` | Decision framework — when to fine-tune vs RAG vs prompt engineer |

## Key Concepts

- **Hallucination:** LLMs confidently generating false information not grounded in facts
- **Knowledge Cutoff:** LLM training data frozen at a point in time; RAG provides dynamic, up-to-date context
- **Retriever:** Finds the most relevant documents for a given query
- **Generator:** LLM that synthesizes an answer conditioned on retrieved context
