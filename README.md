# Advanced RAG Architectures and Evaluation

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-green)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2%2B-orange)](https://langchain-ai.github.io/langgraph/)
[![RAGAS](https://img.shields.io/badge/RAGAS-0.2%2B-purple)](https://docs.ragas.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive, hands-on exploration of **Retrieval-Augmented Generation (RAG)** — from core fundamentals to production-grade agentic systems and rigorous evaluation. Each module pairs conceptual depth with working Jupyter notebooks so you can learn, adapt, and ship.

---

## Modules

| Folder | Module | Topics Covered |
|--------|--------|----------------|
| [`01_rag_fundamentals/`](./01_rag_fundamentals/) | RAG Fundamentals & Architecture | What RAG is · Core components · RAG vs Fine-tuning vs Prompt Engineering |
| [`02_document_processing/`](./02_document_processing/) | Document Processing & Chunking | PDF/Web/CSV loaders · Text splitters · Chunk size strategies · Metadata |
| [`03_embeddings/`](./03_embeddings/) | Embeddings & Vector Representations | Semantic similarity · Distance metrics · OpenAI vs open-source models |
| [`04_vector_stores/`](./04_vector_stores/) | Vector Stores | IVF & HNSW indexing · Chroma · FAISS · Pinecone · CRUD operations |
| [`05_basic_retrieval/`](./05_basic_retrieval/) | Basic Retrieval Techniques | Similarity search · Score thresholds · MMR · Hybrid Search · Ensemble |
| [`06_advanced_retrieval/`](./06_advanced_retrieval/) | Advanced Retrieval Techniques | Contextual compression · Parent-doc retriever · Self-query · Multi-query |
| [`07_advanced_rag_patterns/`](./07_advanced_rag_patterns/) | Advanced RAG Patterns | RAG Fusion · HyDE · Corrective RAG · Self-RAG · Graph RAG |
| [`08_agentic_rag_langgraph/`](./08_agentic_rag_langgraph/) | Agentic RAG with LangGraph | ReAct · Plan-and-Execute · Reflection · State graphs · Checkpointing |
| [`09_rag_evaluation_ragas/`](./09_rag_evaluation_ragas/) | RAG Evaluation with RAGAS | Faithfulness · Answer Relevancy · Context Precision · Recall · `evaluate()` API |

---

## RAG Data Flow

```
Documents → Chunking → Embeddings → Vector Store
                                         ↓
               Query → Retriever → LLM Generator → Answer
```

LLMs hallucinate and have knowledge cutoffs. RAG solves both by grounding generation in an external, updatable knowledge base at inference time — no retraining required.

---

## Prerequisites

- Python 3.10+
- Basic familiarity with LLMs and Python
- API keys: OpenAI (required) · Cohere / Anthropic (optional, specific notebooks)

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/rag-architectures-and-evaluation.git
cd rag-architectures-and-evaluation

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env             # fill in your API keys

jupyter lab
```

---

## Module Details

### [`01_rag_fundamentals/`](./01_rag_fundamentals/)

| Notebook | Description |
|----------|-------------|
| `01_introduction_to_rag.ipynb` | What RAG is, the problems it solves (hallucinations, knowledge cutoffs), and when to use it |
| `02_core_components_and_data_flow.ipynb` | End-to-end data flow: Knowledge Base → Retriever → Generator |
| `03_rag_vs_finetuning_vs_prompt_engineering.ipynb` | Decision framework — when to fine-tune vs RAG vs prompt engineer |

---

### [`02_document_processing/`](./02_document_processing/)

| Notebook | Description |
|----------|-------------|
| `01_document_loaders.ipynb` | LangChain loaders for PDFs, web pages, CSV, JSON, and databases |
| `02_text_splitting_strategies.ipynb` | Recursive, character, semantic, Markdown, and code splitters compared |
| `03_chunking_best_practices.ipynb` | Optimal chunk sizes, overlap strategies, and performance benchmarks |
| `04_metadata_management.ipynb` | Attaching, storing, and filtering metadata for precise retrieval |

---

### [`03_embeddings/`](./03_embeddings/)

| Notebook | Description |
|----------|-------------|
| `01_how_embeddings_work.ipynb` | Vector spaces, cosine similarity, dot product, and Euclidean distance |
| `02_embedding_models_overview.ipynb` | OpenAI `text-embedding-3`, HuggingFace MTEB leaders, Cohere |
| `03_choosing_right_embedding_model.ipynb` | Cost vs quality trade-offs, benchmarking on your own data |
| `04_langchain_embeddings_implementation.ipynb` | Drop-in LangChain `Embeddings` interface with multiple providers |

---

### [`04_vector_stores/`](./04_vector_stores/)

| Notebook | Description |
|----------|-------------|
| `01_vector_store_working_and_indexing.ipynb` | IVF, HNSW, and flat index mechanics; Chroma, FAISS, Pinecone, Qdrant |
| `02_vector_store_crud_operations.ipynb` | Create, read, update, and delete documents with metadata filtering |

---

### [`05_basic_retrieval/`](./05_basic_retrieval/)

| Notebook | Description |
|----------|-------------|
| `01_similarity_search_fundamentals.ipynb` | k-NN search, top-k selection, and score interpretation |
| `02_similarity_score_thresholds.ipynb` | Filtering low-confidence results dynamically |
| `03_mmr_retrieval.ipynb` | Maximal Marginal Relevance — balancing relevance and diversity |
| `04_hybrid_search.ipynb` | Dense + sparse (BM25) fusion with reciprocal rank fusion |
| `05_ensemble_retriever.ipynb` | Combining multiple retrievers with weighted aggregation |

---

### [`06_advanced_retrieval/`](./06_advanced_retrieval/)

| Notebook | Description |
|----------|-------------|
| `01_contextual_compression.ipynb` | LLM-based and embeddings-based document compressors |
| `02_parent_document_retriever.ipynb` | Index small chunks, retrieve large parent context |
| `03_self_query_retriever.ipynb` | Natural-language metadata filtering via structured query generation |
| `04_multi_query_retriever.ipynb` | Generate query variants to overcome single-query blind spots |

---

### [`07_advanced_rag_patterns/`](./07_advanced_rag_patterns/)

| Notebook | Description |
|----------|-------------|
| `01_rag_fusion_rrf.ipynb` | Multi-query retrieval + Reciprocal Rank Fusion for re-ranking |
| `02_hyde.ipynb` | Hypothetical Document Embeddings — generate then retrieve |
| `03_corrective_rag.ipynb` | CRAG: detect retrieval failure and fall back to web search |
| `04_self_rag.ipynb` | Self-reflective generation with retrieve, critique, and regenerate loops |
| `05_graph_rag.ipynb` | Knowledge graph construction and graph-guided retrieval |

---

### [`08_agentic_rag_langgraph/`](./08_agentic_rag_langgraph/)

| Notebook | Description |
|----------|-------------|
| `01_introduction_to_agentic_rag.ipynb` | Why agents, tool-calling, and multi-step reasoning change RAG |
| `02_rag_as_a_tool.ipynb` | Wrapping a retriever as an LLM-callable tool |
| `03_langgraph_fundamentals.ipynb` | State, nodes, edges, conditional routing, and checkpointing |
| `04_agentic_rag_patterns.ipynb` | ReAct, Plan-and-Execute, and Reflection patterns in LangGraph |

---

### [`09_rag_evaluation_ragas/`](./09_rag_evaluation_ragas/)

| Notebook | Description |
|----------|-------------|
| `01_ragas_framework_overview.ipynb` | What RAGAS is and why reference-free evaluation matters |
| `02_rag_pipeline_components_to_evaluate.ipynb` | Retrieval quality vs generation quality — what to measure and when |
| `03_rag_metrics_in_detail.ipynb` | Faithfulness, Answer Relevancy, Context Precision, Context Recall |
| `04_individual_metrics_implementation.ipynb` | Computing each metric independently with code |
| `05_evaluate_api_pipeline.ipynb` | Full end-to-end evaluation using RAGAS `evaluate()` API |

---

## Tech Stack

| Library | Purpose |
|---------|---------|
| `langchain` | Core RAG pipeline components |
| `langgraph` | Agentic RAG orchestration |
| `openai` | LLM and embedding provider |
| `ragas` | RAG evaluation framework |
| `chromadb` | Local vector store |
| `faiss-cpu` | High-performance similarity search |
| `sentence-transformers` | Open-source embedding models |
| `rank-bm25` | Sparse BM25 retrieval |
| `pypdf` | PDF document loading |
| `jupyter` | Interactive notebooks |

---

## Repository Structure

```
rag-architectures-and-evaluation/
├── 01_rag_fundamentals/
├── 02_document_processing/
├── 03_embeddings/
├── 04_vector_stores/
├── 05_basic_retrieval/
├── 06_advanced_retrieval/
├── 07_advanced_rag_patterns/
├── 08_agentic_rag_langgraph/
├── 09_rag_evaluation_ragas/
├── src/
│   ├── loaders/        # Custom document loaders
│   ├── retrievers/     # Retriever wrappers and utilities
│   ├── evaluators/     # Evaluation helpers
│   └── utils/          # Shared config and logging
├── data/
│   └── sample_documents/
├── assets/
│   └── images/
├── requirements.txt
├── .env.example
├── CONTRIBUTING.md
└── LICENSE
```

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [LangChain](https://www.langchain.com/) for the RAG tooling ecosystem
- [LangGraph](https://langchain-ai.github.io/langgraph/) for agentic orchestration primitives
- [RAGAS](https://docs.ragas.io/) for reference-free RAG evaluation
