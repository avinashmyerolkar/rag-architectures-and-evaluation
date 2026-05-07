# Module 4 — Vector Stores

> **What:** Databases purpose-built for storing high-dimensional vectors (embeddings) and running fast similarity search over them.
> **Why:** Brute-force k-NN is O(n) — it breaks at scale. Vector stores use Approximate Nearest Neighbor (ANN) algorithms to reduce search to a tiny subset of the corpus while keeping accuracy above 99%.

---

## Core Idea

```
Vector Store  =  Storage  +  Similarity Search
```

Every chunk of text gets embedded once, persisted, and reused on every query — you only pay the embedding cost once.

---

## Table of Contents

1. [Why Use Vector Stores?](#1-why-use-vector-stores)
2. [What Gets Stored?](#2-what-gets-stored)
3. [Multi-Dimensional Space](#3-multi-dimensional-space)
4. [Indexing Process](#4-indexing-process)
5. [Brute Force vs ANN](#5-brute-force-vs-ann)
6. [ANN: IVF (Clustering-Based)](#6-ann-ivf--clustering-based-search)
7. [ANN: HNSW (Graph-Based)](#7-ann-hnsw--graph-based-search)
8. [ChromaDB](#8-chromadb)
9. [Notebooks](#9-notebooks)

---

## 1. Why Use Vector Stores?

### Queries vs Documents — different persistence needs

| | Query | Document |
|---|---|---|
| Nature | Dynamic (new every time) | Static (rarely changes) |
| Persist? | No | Yes |

Documents are embedded **once** and stored. Queries are embedded at runtime and never persisted.

### Two reasons to persist embeddings

- **Cost** — embedding models (especially paid APIs) charge per token. Re-embedding the same corpus on every query is wasteful.
- **Time** — embedding inference runs through deep learning models. Doing it at query time adds unacceptable latency.

---

## 2. What Gets Stored?

Each document chunk in a vector store holds **four fields**:

```json
{
  "id":        "chunk_001",
  "embedding": [0.23, -0.17, 0.85, ..., 0.61],
  "document":  "LangChain is a framework for...",
  "metadata":  {"source": "doc1.pdf", "page": 3}
}
```

| Field | Why it's stored |
|-------|----------------|
| `id` | Unique identifier for CRUD operations |
| `embedding` | The vector used for similarity search |
| `document` | Original text returned to the LLM — we retrieve text, not the raw vector |
| `metadata` | Source, page, date, author — enables filtered retrieval |

> **Key insight:** We never return raw embeddings to the LLM. The vector is only used for *finding* the right chunk — the original text is what gets passed to the generator.

---

## 3. Multi-Dimensional Space

Embeddings are stored in a **multi-dimensional vector space** where:

- **Dimensionality** = number of dimensions in the embedding (e.g. 1536 for `text-embedding-3-small`)
- Query and document embeddings **must share the same dimension** — similarity calculations happen element-wise
- **Semantic meaning** is encoded as position in this space — similar concepts cluster together geometrically

### Purpose of the Embedding Model

The embedding model captures **semantic meaning**, not keywords. This is why a query for *"reducing CO₂ from atmosphere"* can match a document about *"photosynthesis"* — they are geometrically close in vector space even though they share no words.

---

## 4. Indexing Process

When you add documents to a vector store:

1. Text → embedding model → dense vector
2. Vector stored alongside original text and metadata
3. An **index** is built over the stored vectors to enable fast future search

The indexing strategy chosen at step 3 determines how fast and accurate retrieval will be.

---

## 5. Brute Force vs ANN

### Brute Force (Exact Search)

- Calculates similarity between the query vector and **every** document vector in the store
- Sorts by score descending, returns top-k
- Time complexity: **O(n)** — latency grows linearly with corpus size
- 100% accurate but unusably slow at scale

### Approximate Nearest Neighbor (ANN)

- Searches only a **structured subset** of the corpus — not all documents
- Proven to return **~99% accurate results** in practice
- Dramatically reduces latency — near O(log n)
- The trick is *how documents are organized at index time* — smart structure means smart skipping at query time

> **When to use brute force:** Small corpora (< ~10k documents) where exact accuracy matters more than speed.

---

## 6. ANN: IVF — Clustering-Based Search

**IVF = Inverted File Index**

### Core idea

Apply **K-Means clustering** (unsupervised) at index time. The query then only searches the most relevant cluster — skipping everything else.

### Index time

```
Documents → K-Means (k = number of clusters) → clusters formed by topic/semantics
Each cluster → centroid = average embedding of all docs in that cluster

IVF index structure:
  cluster_1 = [e1, e10, e20, ...]   # Python docs
  cluster_2 = [e3, e7,  e15, ...]   # Heart disease docs
  cluster_3 = [e5, e9,  e18, ...]   # AQI docs
```

### Query time

```
Query vector → cosine similarity vs each centroid
→ Closest centroid wins → search only that cluster
→ Exact similarity on just those docs → return top-k
```

### Visual intuition

Three clusters: `Python`, `Heart Diseases`, `AQI`. A query *"heart attack"* computes cosine angle against each centroid. The smallest angle lands at `Heart Diseases` → only those documents are searched. `Python` and `AQI` are entirely skipped.

### What the centroid represents

The centroid is the **geometric average of all document vectors in that cluster** — it represents the average semantic meaning of that topic group. A closer angle between the query and a centroid means the query is topically closer to that cluster.

### IVF trade-offs

| Pro | Con |
|-----|-----|
| Massive search space reduction | If the query lands at the wrong cluster boundary, relevant docs in neighboring clusters are missed |
| Works well when topics are well-separated | Requires choosing `k` (number of clusters) as a hyperparameter |

---

## 7. ANN: HNSW — Graph-Based Search

**HNSW = Hierarchical Navigable Small World**

### Inspiration: Six Degrees of Separation

The social science principle: any person on Earth can reach any other person through at most ~6 mutual connections. HNSW applies this to vector search — every embedding is reachable from any starting point through a small number of graph hops.

### Structure: A Multi-Layer Graph

HNSW builds a **layered graph**. The value below each node represents its embedding coordinate in 1D (simplified for illustration):

```
Layer 2 (Express):   P(5.0) ———————————————————— T(9.0)
                       ↓
Layer 1 (Local):   Js(1.5) ———— P(5.0) —————————— T(9.0)
                                  ↓
Layer 0 (Base):  Py(1.0)—Js(1.5)——P(5.0)—O(5.3)——T(9.0)
```

| Layer | Role | Connections |
|-------|------|-------------|
| Layer 0 (base) | All embeddings | Dense — connected to close neighbors |
| Layer 1 | Subset promoted randomly | Sparser — longer-range hops |
| Layer 2+ | Further promoted subset | Very sparse — "express" connections |

Graph building starts from layer 0 upward. Searching starts from the top and drills down.

### Query time: top → bottom navigation

```
Query Q = 5.2

Layer 2: Enter at P(5.0). Compare T(9.0). Q is closer to P → descend ↓
Layer 1: At P(5.0). Compare Js(1.5) and T(9.0). Both farther → descend ↓
Layer 0: At P(5.0). Compare O(5.3). Q(5.2) closer to O(5.3).
         Local neighborhood = [P(5.0), O(5.3)]
         → Full similarity scored on just 2 docs → retrieve
```

Large jumps at the top layers, fine-grained local search at the base — this is the "small world" efficiency.

### Disadvantages

- Results are **suboptimal** (approximate) — the graph traversal may miss a marginally closer neighbor that was never connected
- Promotion of embeddings to upper layers is **random** — index quality has some non-determinism

---

## 8. ChromaDB

ChromaDB is an open-source, HNSW-backed vector store built for RAG applications.

**ChromaDB uses HNSW by default.** When you store chunks in ChromaDB, it automatically builds the multi-layer graph for fast retrieval — no configuration required.

**Key features:**
- Zero-config: runs in-memory or persisted to disk
- Automatic HNSW indexing on every `add`
- Metadata filtering via `where` clauses
- Native LangChain integration via `langchain-chroma`

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma(
    collection_name="rag_docs",
    embedding_function=OpenAIEmbeddings(),
    persist_directory="./chroma_db",
)

# Index time — HNSW graph built automatically
vectorstore.add_documents(docs)

# Query time — top-down graph traversal
results = vectorstore.similarity_search("heart attack", k=3)
```

---

## 9. Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_vector_store_working_and_indexing.ipynb` | IVF and HNSW mechanics with working code; Chroma, FAISS, Pinecone, Qdrant setup |
| 2 | `02_vector_store_crud_operations.ipynb` | Create, read, update, and delete documents; metadata filtering with `where` |

---

## Key Takeaways

| Concept | One-liner |
|---------|-----------|
| Vector store | Storage + Similarity Search |
| Persist documents | Cost + Time of re-embedding |
| Don't persist queries | They are dynamic |
| What's stored per chunk | id · embedding · original text · metadata |
| Brute force problem | O(n) — too slow at scale |
| ANN solution | Search a structured subset, not everything |
| IVF approach | K-Means cluster at index time → search one cluster at query time |
| HNSW approach | Layered graph, navigate top-down, fine-grained hop at base layer |
| ChromaDB uses | HNSW by default |
