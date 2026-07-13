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

## ▶️ Running it
1. Install [Ollama](https://ollama.com/) and pull the model: `ollama pull llama3.2`
2. Install dependencies: `pip install -r requirements.txt`
3. Drop resume PDFs into `data/` (a sample is already included)
4. Run: `python src/main.py`
