# CodeSeer

**CodeSeer** is a semantic code search system that ingests source code, generates vector embeddings, indexes them using FAISS, and exposes an explainable search API with ranked results and confidence scores.

The project focuses on real backend engineering practices: clean architecture, deterministic pipelines, and explainable APIs.

---

## 🚀 Features

- **Code Ingestion Pipeline**
  - Scans source directories
  - Loads and chunks code files
  - Generates embeddings
  - Indexes vectors using FAISS
  - Persists metadata for restart-safe ingestion

- **Semantic Search**
  - Vector-based semantic search over code
  - Ranked results using similarity scores

- **Explainable Results**
  - Normalized relevance scores
  - Rank ordering
  - Human-readable confidence levels (`high`, `medium`, `low`)

- **Production-Oriented Backend**
  - FastAPI-based service
  - Versioned APIs (`/api/v1`)
  - Clean service-layer separation
  - Safe handling of runtime-generated data

---


Architecture
Scanner → Loader → Chunker → Embedder → FAISS → Metadata Store → Search API


**Tech Stack**

Python

FastAPI

FAISS

Sentence Transformers

NumPy

Git & GitHub (PR-based workflow)

