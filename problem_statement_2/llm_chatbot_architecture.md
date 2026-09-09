# LLM-Based Chatbot — High-Level Architecture

## 1. Overview

A chatbot based on a Large Language Model (LLM) is not just the model itself.
The LLM is one component in a larger system that handles user interaction,
context management, knowledge retrieval, prompt construction, safety, and
deployment. This document describes the key architectural components and a
high-level approach for building such a system.

## 2. Architecture Diagram

```
                         ┌───────────────┐
                         │     USER      │
                         └───────┬───────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │ Client / Web App │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │    API Layer     │
                       └────────┬─────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ Authentication &        │
                    │ Authorization           │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ Conversation Manager   │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ Context / Retrieval    │
                    │ Manager (RAG)          │
                    └───────────┬────────────┘
                                │
                     ┌──────────┴──────────┐
                     │                     │
                     ▼                     ▼
             Conversation DB        Vector Database
                                         ▲
                                         │
                                  ┌──────┴──────┐
                                  │  Embeddings │
                                  └──────┬──────┘
                                         ▲
                                         │
                                  ┌──────┴──────┐
                                  │  Documents  │
                                  └─────────────┘
                     │
                     ▼
             ┌─────────────────┐
             │ Prompt Builder  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │      LLM        │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Guardrails /    │
             │ Validation      │
             └────────┬────────┘
                      │
                      ▼
                    USER
```

## 3. Key Components

### 3.1 Client / User Interface

The entry point for the user. Typically a web application, mobile app, or
messaging platform (Slack, Teams, WhatsApp). Responsibilities:

- Captures user input (text, voice, attachments)
- Displays streaming responses, citations, and conversation history
- Handles session management and UI state

### 3.2 API Layer (Backend Gateway)

A stateless HTTP/WebSocket service (e.g., FastAPI, Express, Django) that
exposes endpoints for chat.

- Routes requests to downstream components
- Implements rate limiting, request validation, and logging
- Supports streaming (Server-Sent Events / WebSockets) for token-by-token
  LLM output
- Orchestrates the overall request lifecycle

### 3.3 Authentication & Authorization

Ensures only authorized users access data.

- Authentication: JWT, OAuth 2.0, SSO (SAML/OIDC)
- Authorization: role-based or attribute-based access control (RBAC/ABAC)
- Critical for enterprise RAG: document-level filtering by user permissions

### 3.4 Conversation Manager

Maintains multi-turn dialogue state.

- Stores conversation history in a persistent database (PostgreSQL, DynamoDB,
  Redis)
- Implements conversation windowing, summarization, or truncation to fit the
  LLM context limit (e.g., 128K tokens)
- Handles session, thread, and memory management

### 3.5 Context / Retrieval Manager (RAG Layer)

The core of a knowledge-grounded chatbot. Without retrieval, the LLM relies
only on its parametric knowledge (cutoff date, hallucinations).

**Ingestion pipeline (offline):**

```
Documents → Text Extraction → Chunking (e.g., 512 tokens, 50 overlap)
→ Embedding Generation (e.g., text-embedding-3-large, E5, BGE)
→ Vector Database
```

**Query pipeline (online):**

```
User Query → Embedding Model → Query Vector
→ Vector Similarity Search (top-k, e.g., k=5)
→ Metadata Filtering (department, access level)
→ Hybrid Search (vector + keyword / BM25)
→ Re-rank (optional, cross-encoder)
→ Relevant Chunks → Prompt Context
```

Key decisions: chunk size, embedding model, distance metric (cosine),
index type (HNSW), and retrieval threshold.

### 3.6 Vector Database

Stores and indexes embeddings for semantic search. Detailed comparison is in
`vector_database_analysis.md`. For the enterprise assistant hypothetical, Weaviate
is selected for hybrid search + metadata filtering; pgvector is preferred when
PostgreSQL is already the primary store.

### 3.7 Prompt Builder (Orchestration)

Constructs the final prompt sent to the LLM.

Components:

- System prompt: defines role, tone, constraints
- Retrieved context: top-k document chunks with citations
- Conversation history: recent turns (with optional summarization)
- User query: current question
- Few-shot examples (optional)
- Tool definitions (if function calling is used)

Example template:

```
System: You are an enterprise knowledge assistant. Answer only from context.
        Cite document IDs. If answer not in context, say "I don't know".

Context:
[Doc 123] Leave policy: Employees can request WFH via manager...
[Doc 456] Production access requires ticket SEC-...

History:
User: How to get prod access?
Assistant: ...

User: What about WFH?
```

Prompt engineering and versioning are critical for quality.

### 3.8 LLM (Inference Layer)

The generative engine. Options:

- **Managed APIs:** OpenAI GPT-4o, Anthropic Claude, Google Gemini
- **Self-hosted:** Llama 3, Mistral, Qwen via vLLM, TGI, Ollama

Considerations:

- Context window, latency, cost per 1K tokens
- Function / tool calling for agentic workflows
- Fine-tuning vs. RAG vs. prompt tuning — for most knowledge tasks, RAG is
  preferred over fine-tuning to keep knowledge fresh
- Model routing / tiering: small fast model for simple queries, large model
  for complex reasoning

Generation parameters: `temperature`, `top_p`, `max_tokens`, `stop sequences`.

### 3.9 Guardrails & Validation (Post-Processing)

Output passes through safety and quality checks before reaching the user.

- **Input guardrails:** prompt injection detection, PII redaction, toxicity
  filter
- **Output guardrails:** hallucination detection, citation verification,
  policy compliance, content moderation (e.g., Llama Guard, NeMo Guardrails,
  Azure Content Safety)
- **Validation:** schema enforcement for structured outputs, retry on failure
- **Observability:** logging, tracing, evaluation metrics (faithfulness,
  relevance, latency)

### 3.10 Supporting Infrastructure (Cross-Cutting)

| Concern | Technology Examples |
|---------|---------------------|
| Storage (conversations, docs, metadata) | PostgreSQL, S3, Redis |
| Caching | Redis for LLM response / embedding cache |
| Monitoring | LangSmith, Langfuse, Prometheus, Grafana |
| Evaluation | RAGAs, TruLens, human-in-the-loop |
| Deployment | Docker, Kubernetes, CI/CD |
| Cost control | Token usage tracking, quota management |

## 4. High-Level Approach (Build Steps)

1. **Define use case and constraints:** Who are users? What knowledge sources?
   Latency / accuracy / cost targets? Compliance requirements?
2. **Ingest knowledge base:** Connect to document sources (Confluence, SharePoint,
   S3), chunk, embed, and index in vector database.
3. **Build retrieval layer:** Implement embedding, vector search, metadata
   filtering, hybrid search, and re-ranking; tune via retrieval evaluation.
4. **Implement conversation and prompt layer:** Design prompt templates,
   context window management, and citation handling.
5. **Integrate LLM:** Connect to inference endpoint, implement streaming,
   function calling if needed, and fallback handling.
6. **Add guardrails:** Input/output validation, PII handling, and safety
   filters.
7. **Instrument observability:** Log prompts, retrieved chunks, and outputs;
   track cost, latency, and quality metrics.
8. **Evaluate and iterate:** Measure retrieval precision/recall, answer
   faithfulness, and user satisfaction; A/B test prompt and model changes.
9. **Deploy and scale:** Containerize, deploy behind API gateway, add
   auto-scaling, and monitor.

## 5. Design Trade-offs

| Decision | Option A | Option B |
|----------|----------|----------|
| Knowledge grounding | RAG (fresh, cited) | Fine-tuning (parametric, needs retraining) |
| Vector store | Dedicated (Weaviate/Milvus) for scale | pgvector for simplicity if Postgres already used |
| LLM hosting | Managed API (faster to ship) | Self-hosted (data privacy, cost at scale) |
| Search | Pure vector (semantic) | Hybrid (semantic + keyword) for technical terms |

There is no single best architecture; the choice depends on data size,
latency, cost, existing infrastructure, and privacy requirements.

## 6. Summary

An LLM chatbot is a system where the LLM is orchestrated with a client, API
gateway, authentication, conversation memory, retrieval (vector search),
prompt construction, and guardrails. For an enterprise knowledge assistant,
the retrieval layer (RAG + vector database + hybrid search) is the most
critical component for delivering accurate, cited, and permission-aware
answers.

**References:**

- Weaviate Documentation — Retrieval and Hybrid Search
- pgvector Documentation — Vector Similarity Search
- Lewis et al., Retrieval-Augmented Generation (2020)
- LangChain / LlamaIndex — RAG Orchestration Patterns
