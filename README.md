# 🧠 Agentic RAG using LangGraph, LangChain & ChromaDB

An end-to-end implementation of an **Agentic Retrieval-Augmented Generation (RAG)** system inspired by the [Medium article by Alpha Iterations](https://medium.com/ai-in-plain-english/build-agentic-rag-using-langgraph-b568aa26d710).

This project demonstrates how to build an adaptive, reasoning-based RAG workflow that can:

- Dynamically **choose the best data source** (medical Q&A, device manuals, or web search)
- Validate retrieval relevance before generation
- Produce grounded, auditable answers using a lightweight LLM agent

---

## 🧱 Project Structure

agentic-rag/
├── data/
│ ├── medical_q_n_a.csv
│ ├── medical_device_manuals_dataset.csv
│ ├── medical_q_n_a_prepared.csv
│ ├── medical_device_manuals_prepared.csv
├── src/
│ ├── prepare_data.py
│ ├── create_vector_db.py
│ ├── test_llm_connection.py
│ ├── app.py
├── chroma_db/ # vector store (auto-generated)
├── .env # holds API keys (NOT pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-github-username>/agentic-rag.git
cd agentic-rag
```

# Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate # macOS / Linux

# OR

# Install dependencies

pip install -r requirements.txt

# Configure API keys . Create a .env file in the project root:

OPENAI_API_KEY=sk-your-openai-key
SERPER_API_KEY=your-serper-key
