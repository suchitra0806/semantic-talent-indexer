# 🚀 Semantic Talent Indexer

A local RAG (retrieval-augmented generation) pipeline designed to index and query professional resumes using natural language.

## 🛠️ Stack
- **Orchestration:** [llamaIndex](https://www.llamaindex.ai/)
- **Embeddings:** `BAAI/bge-small-en-v1.5` (via huggingface)
- **LLM:** llama 3.2 (running locally via [ollama](https://ollama.com/))
- **Language:** python 3.13+

## 🌟 Key Features
- **Data privacy:** Indexing and inference happen 100% locally. Sensitive candidate data never leaves the machine.
- **Semantic search:** Goes beyond keyword matching to understand professional context.
- **Zero-cost scaling:** Utilizes local hardware, bypassing expensive openai/anthropic api token costs.
