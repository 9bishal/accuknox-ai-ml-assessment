# AccuKnox AI/ML Assessment — Bishal Kumar Shah

This repository contains the complete submission for the AccuKnox AI/ML technical assessment, covering Problem Statement 1 (Python, API, Database, Visualization) and Problem Statement 2 (LLM, Deep Learning, AI, ML theory).

**Author:** Bishal Kumar Shah (1CR23AI020) — `shahvishal.9090@gmail.com` — [@9bishal](https://github.com/9bishal)
**Date:** September 2026

---

## Repository Structure

```
accuknox-ai-ml-assessment/
├── problem_statement_1/          # Implementation tasks
│   ├── 01_api_to_sqlite.py       # API → SQLite (books)
│   ├── 02_student_scores.py      # API → Average → Matplotlib
│   ├── 03_csv_to_sqlite.py       # CSV → SQLite (users)
│   ├── books.db                  # Generated SQLite DB (gitignored)
│   ├── users.db                  # Generated SQLite DB (gitignored)
│   ├── student_scores.png        # Generated chart
│   ├── requirements.txt
│   └── README.md
├── problem_statement_2/          # Theory / research
│   ├── llm_chatbot_architecture.md   # Chatbot architecture + diagram
│   ├── vector_database_analysis.md   # Vector DB analysis + selection
│   ├── self_assessment.md            # A/B/C rating (LLM, DL, AI, ML)
│   └── diagrams/                     # Architecture diagrams
├── sample_data/
│   └── users.csv                 # 25 sample user records
├── screenshots/
│   └── student_scores.png
├── .gitignore
└── README.md
```

---

## Problem Statement 1 — Quick Start

All scripts resolve paths relative to their own file location (`Path(__file__).resolve().parent`), so they work from any working directory.

```bash
# From repository root or from problem_statement_1/
pip install -r problem_statement_1/requirements.txt

# Run each task
python3 problem_statement_1/01_api_to_sqlite.py   # → creates problem_statement_1/books.db
python3 problem_statement_1/02_student_scores.py  # → creates problem_statement_1/student_scores.png
python3 problem_statement_1/03_csv_to_sqlite.py   # → creates problem_statement_1/users.db

# Or from inside the folder
cd problem_statement_1
python3 01_api_to_sqlite.py
python3 02_student_scores.py
python3 03_csv_to_sqlite.py
```

| Task | Script | Input | Output | Technique |
|------|--------|-------|--------|-----------|
| API → SQLite (books) | `01_api_to_sqlite.py` | Open Library API `search.json?q=python` | `books.db` (10 books) | `requests`, `sqlite3`, `INSERT OR IGNORE` |
| Scores → Avg → Chart | `02_student_scores.py` | jsonplaceholder `/users` (+ synthetic scores) | `student_scores.png` + avg | `requests`, `matplotlib`, `axhline` |
| CSV → SQLite | `03_csv_to_sqlite.py` | `sample_data/users.csv` | `users.db` (25 users) | `csv.DictReader`, `sqlite3` |

See `problem_statement_1/README.md` for detailed data flows, assumptions, and error handling.

---

## Problem Statement 2 — Theory

| Document | Content |
|----------|---------|
| `problem_statement_2/llm_chatbot_architecture.md` | High-level LLM chatbot architecture: 10 components (Client, API Gateway, Auth, Conversation Manager, RAG/Retrieval, Vector DB, Prompt Builder, LLM, Guardrails, Observability) + end-to-end build steps. Includes ASCII architecture diagram. |
| `problem_statement_2/vector_database_analysis.md` | Vector database deep dive: embedding, similarity metrics (cosine/euclidean/dot), indexing (HNSW/IVF/PQ/ANN), metadata filtering, hybrid search, 5-way comparison (FAISS, pgvector, Pinecone, Weaviate, Milvus), and selection (Weaviate for enterprise RAG, pgvector as alternative). |
| `problem_statement_2/self_assessment.md` | Self-rating A/B/C for LLM, Deep Learning, AI, ML with justifications and evidence (see scale: A = independent, B = under supervision, C = little/no understanding). |
| `problem_statement_2/diagrams/` | Exported architecture diagrams (PNG) referenced by the docs. |

---

## Most Complex Code — Links

As requested in Problem Statement 1:

### Most Complex Python Code

1. **Autonomous Research Verification Agent (5-Agent LangGraph)** — Orchestrator, Research, Analyst, Writer, Fact-Checker agents with LangGraph `StateGraph`, Groq model tiering, and automated report generation.
   - **Link:** <https://github.com/9bishal/Autonomous-Research-Verification-Agent->

2. **Grounded RAG Bot (Hybrid Retrieval, Production)** — Hybrid retrieval (Chroma + BM25 + RRF), re-ranking, hallucination guard, streaming SSE, FastAPI + React + Groq (`gpt-oss-20b/120b`), PDF/DOCX page-level citations.
   - **Link:** <https://github.com/9bishal/grounded-rag-bot>

3. **NovaCart AI — Multi-hop RAG Agent** — LangGraph + Groq + ChromaDB + FastAPI, multi-hop reasoning over complex queries.
   - **Link:** <https://github.com/9bishal/novacart-ai>

4. **Secure-RAG / Learning_RAG** — From-scratch RAG implementation, LangChain + OpenAI + FAISS, end-to-end ingestion and evaluation.
   - Links: local projects `Learning_RAG/` and `secure-rag/` (available on request / drive).

### Most Complex Database Code

1. **Event-Driven Order Notification System** — Kafka event bus, PostgreSQL durability, Redis/BullMQ delayed jobs, idempotent consumers, saga-style lifecycle, k6 load testing, Dockerized microservices.
   - **Link:** <https://github.com/9bishal/event-driven-order-notification-system>

2. **InkAPI — Blog Platform (System Design)** — Redis cache-aside, Nginx load balancing, JWT auth, outbox pattern, CQRS read model, consistent hashing, circuit breaker, PostgreSQL.
   - **Link:** <https://github.com/9bishal/inkapi>

3. **ReachInbox Email Scheduler** — BullMQ + Redis + PostgreSQL, Google OAuth, per-sender hourly limits, restart-safe idempotent delivery.
   - **Link:** <https://github.com/9bishal/reachinbox-email-scheduler>

4. **PERC Production** — Supabase/PostgreSQL with program images, contact form, and faculty management.
   - **Link:** <https://github.com/9bishal/PERC-Prod>

All repositories are public unless noted. Private repos available on request.

---

## Technologies

Python, REST API, JSON, SQLite, SQL, CSV, Matplotlib, Requests, Vector Databases, RAG, LLM, Pathlib

## Author

**Bishal Kumar Shah** — AI/ML, Dept. of AI, CMRIT (VTU) — `shahvishal.9090@gmail.com`

- GitHub: <https://github.com/9bishal>


For submission: this repository (`9bishal/accuknox-ai-ml-assessment`) or drive link available on request.

---

## Notes

- Assumptions are documented inline and in `problem_statement_1/README.md` and `problem_statement_2/vector_database_analysis.md`.
- Databases (`*.db`) and generated images are gitignored; they are recreated by running the scripts.
- Scripts handle missing fields, empty responses, duplicate records (`INSERT OR IGNORE`), and use timeouts on API calls.
