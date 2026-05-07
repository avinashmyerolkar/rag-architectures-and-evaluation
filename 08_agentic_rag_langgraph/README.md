# Module 8 — Agentic RAG with LangGraph

> **What:** Building RAG systems where an LLM agent decides how and when to retrieve.
> **Why:** Static RAG pipelines break on multi-hop questions. Agents can plan, retrieve iteratively, verify, and adapt — enabling far more complex reasoning.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `01_introduction_to_agentic_rag.ipynb` | Why agents, tool-calling, and multi-step reasoning change RAG |
| 2 | `02_rag_as_a_tool.ipynb` | Wrapping a retriever as an LLM-callable tool |
| 3 | `03_langgraph_fundamentals.ipynb` | State, nodes, edges, conditional routing, and checkpointing |
| 4 | `04_agentic_rag_patterns.ipynb` | ReAct, Plan-and-Execute, and Reflection patterns in LangGraph |

## Key Concepts

- **ReAct:** Reason → Act → Observe loop; agent interleaves thinking and tool calls
- **LangGraph State:** Typed dictionary passed through nodes — each node reads and writes to state
- **Checkpointing:** Persist graph state between runs for human-in-the-loop and resumable workflows
- **Plan-and-Execute:** Separate planning and execution agents — better for long-horizon tasks
