# Enterprise AI Knowledge Assistant using RAG & LLM

An AI-powered Enterprise Knowledge Assistant that enables semantic document search and context-aware question answering using Retrieval-Augmented Generation (RAG). The system retrieves relevant information from enterprise policy documents before generating responses, improving answer accuracy and reducing hallucinations.

---

## Features

- PDF document ingestion
- Automatic document preprocessing and chunking
- Semantic embedding generation
- FAISS vector database for efficient retrieval
- Context-aware question answering using Retrieval-Augmented Generation (RAG)
- Enterprise policy document search
- REST API built with Flask
- Fast semantic similarity search

---

## Tech Stack

- Python
- Flask
- LangChain
- FAISS
- Sentence Transformers
- FLAN-T5
- PostgreSQL

---

## Project Structure

```text
enterprise-ai-knowledge-assistant-rag-llm/
│
├── app.py
├── ingest.py
├── requirements.txt
├── documents.pkl
├── vector_store.index
├── data/
│   ├── email_setup.pdf
│   ├── holidays_policy.pdf
│   ├── hr_policy.pdf
│   ├── it_support.pdf
│   ├── laptop_policy.pdf
│   ├── onboarding.pdf
│   ├── salary_policy.pdf
│   ├── software_installation.pdf
│   └── vpn_policy.pdf
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
└── README.md
```

---

## Installation

```bash
git clone https://github.com/MadhuriPesalavari/enterprise-ai-knowledge-assistant-rag-llm.git

cd enterprise-ai-knowledge-assistant-rag-llm

pip install -r requirements.txt

python ingest.py

python app.py
```

---

## How It Works

1. Load enterprise policy documents.
2. Split documents into smaller text chunks.
3. Generate embeddings using Sentence Transformers.
4. Store embeddings in a FAISS vector database.
5. Retrieve the most relevant document chunks based on user queries.
6. Generate accurate, context-aware responses using an LLM.

---

## Future Enhancements

- Support additional document formats (DOCX, TXT)
- LangGraph integration
- Agentic AI workflows
- ChromaDB support
- Cloud deployment (AWS/Azure)
- User authentication and role-based access

---

## Author

**Pesalavari Madhuri**

GitHub: https://github.com/MadhuriPesalavari

LinkedIn: https://linkedin.com/in/pesalavari-madhuri
## Query Flow

User Query
   ↓
Flask REST API
   ↓
Generate Query Embedding
   ↓
FAISS Similarity Search
   ↓
Retrieve Relevant Policy Chunks
   ↓
FLAN-T5
   ↓
Context-Aware Answer
