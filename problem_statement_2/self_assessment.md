# Self-Assessment — LLM, Deep Learning, AI, ML

**Author:** Bishal Kumar Shah
**Date:** 2026-09-09
**Scale:** A = can code independently; B = can code under supervision; C = have little or no understanding

## Rating Summary

| Area | Rating | Justification |
|------|--------|---------------|
| **Machine Learning (ML)** | **A** | Can code independently. Built supervised models (classification/regression), feature engineering, cross-validation, hyperparameter tuning (GridSearchCV, Optuna), ensemble methods, preprocessing pipelines with scikit-learn, and hypothesis testing for research verification. Comfortable from data ingestion to deployment and evaluation (precision/recall/F1, ROC-AUC, RMSE). |
| **Deep Learning (DL)** | **B** | Can code under supervision / independently for standard architectures. Implemented and fine-tuned CNNs, RNN/LSTM, and Transformer-based models using PyTorch and Hugging Face. Experience with transfer learning, training loops, mixed precision, and debugging convergence issues. Requires peer review for novel architecture design, large-scale distributed training, and advanced optimization research. |
| **AI (General)** | **B** | Can code under supervision for broad AI systems. Covers search, knowledge representation, RAG pipelines, vector search, and agentic orchestration (LangGraph, function calling). Strong on applied AI system composition; defers to deep experts for theoretical AI planning or symbolic reasoning at research depth. |
| **LLM** | **A–B** | **A** for applied LLM engineering (RAG, prompt engineering, tool use, vector DB integration, evaluation, deployment); **B** for LLM research (pre-training, RLHF, mechanistic interpretability). Shipped production RAG systems (see complex code links below) with hybrid retrieval, re-ranking, and guardrails; can independently build and evaluate LLM applications but would seek supervision for training/fine-tuning foundation models from scratch. |

## Detailed Notes

### Machine Learning — A

- **Workflow:** Exploratory data analysis, feature engineering, handling imbalance/missing data, pipeline construction (`Pipeline`, `ColumnTransformer`), model selection, and validation (k-fold, stratified split, time-series split where needed).
- **Algorithms:** Linear/logistic regression, decision trees, random forest, gradient boosting (XGBoost, LightGBM, CatBoost), SVM, k-means, and dimensionality reduction (PCA, t-SNE).
- **Evaluation:** Confusion matrix, classification report, calibration, learning curves, and error analysis. Aware of leakage and overfitting pitfalls.
- **Tools:** Python, scikit-learn, pandas, NumPy, MLflow for tracking.

### Deep Learning — B

- **Frameworks:** PyTorch (primary), exposure to TensorFlow/Keras; Hugging Face Transformers for NLP/vision.
- **Architectures:** Feed-forward, CNN (ResNet, EfficientNet), sequence models (LSTM/GRU), attention/Transformer; fine-tuned pretrained models for downstream tasks.
- **Training:** Custom Dataset/DataLoader, loss functions, optimizers (AdamW), schedulers, early stopping, gradient clipping, mixed precision. Debugging via loss curves, gradient flow checks.
- **Gap to A:** Needs supervision for distributed training (DDP/FSDP), large-scale hyperparameter search, neural architecture search, and novel model invention beyond adapting existing architectures.

### AI — B

- Systems-level AI: Composes retrieval, reasoning, and generation into end-to-end products (e.g., Advanced RAG with LangGraph + Groq model tiering — see links below).
- Familiar with RAG, ReAct agents, vector databases (FAISS, pgvector, Weaviate — see `vector_database_analysis.md`), and evaluation frameworks (RAGAs).
- General AI theory (search, planning, probabilistic reasoning) at working knowledge level; not a researcher in symbolic AI.

### LLM — A (Applied) / B (Research)

- **Applied (A):** Prompt design, few-shot, chain-of-thought, function/tool calling, RAG ingestion (chunking, embedding, hybrid search, re-ranking), conversation memory/windowing, streaming, guardrails (prompt injection, PII, hallucination checks), and observability (LangSmith/Langfuse). Built:
  - Advanced RAG with LangGraph (graph-based orchestration, stateful retrieval)
  - Enterprise knowledge assistant design (this assessment, `llm_chatbot_architecture.md`)
- **Research (B):** Understands transformer fundamentals (attention, positional encoding, scaling laws), pre-training objectives, fine-tuning (LoRA/QLoRA), and RLHF at conceptual + hands-on level for adaptation, but not independently pre-training foundation models or conducting RLHF research without guidance.

## How I Would Close Gaps to A Across All Areas

1. **DL → A:** Lead a project requiring distributed training of a custom architecture end-to-end, with peer review from a senior DL researcher.
2. **LLM (Research) → A:** Participate in a fine-tuning/RLHF cycle on an open model (e.g., Llama 3) with full evaluation harness.

## Evidence

See complex code and database links in the root `README.md` and commit history. Happy to walk through any project in a technical interview.

---
*Note: Ratings are self-assessed and intended to be calibrated in interviews.*
