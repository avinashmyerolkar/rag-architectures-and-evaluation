# Module 9 — RAG Evaluation with RAGAS

> **What:** Scientifically measuring how well your RAG pipeline performs.
> **Why:** "It seems to work" is not enough for production. RAGAS provides reference-free metrics that quantify both retrieval and generation quality independently.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_ragas_framework_overview.ipynb` | What RAGAS is and why reference-free evaluation matters |
| 2 | `02_rag_pipeline_components_to_evaluate.ipynb` | Retrieval quality vs generation quality — what to measure and when |
| 3 | `03_rag_metrics_in_detail.ipynb` | Faithfulness, Answer Relevancy, Context Precision, Context Recall explained |
| 4 | `04_individual_metrics_implementation.ipynb` | Computing each metric independently with code |
| 5 | `05_evaluate_api_pipeline.ipynb` | Full end-to-end evaluation using RAGAS `evaluate()` API |

## RAGAS Metrics

| Metric | Measures | Range |
|--------|----------|-------|
| **Faithfulness** | Is the answer grounded in the retrieved context? | 0–1 |
| **Answer Relevancy** | Does the answer address the question? | 0–1 |
| **Context Precision** | Are retrieved docs actually relevant? | 0–1 |
| **Context Recall** | Did retrieval find all necessary information? | 0–1 |
