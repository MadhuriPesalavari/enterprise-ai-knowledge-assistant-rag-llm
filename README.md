# Enterprise AI Knowledge Assistant using RAG & LLM

An AI-powered enterprise knowledge assistant that enables semantic document search and context-aware question answering using Retrieval-Augmented Generation (RAG). The system retrieves relevant information from enterprise documents before generating responses, improving answer accuracy and reducing hallucinations.

---

## Features

- Upload and process PDF and TXT documents
- Automatic text chunking and preprocessing
- Generate semantic embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Perform semantic similarity search
- Context-aware question answering with FLAN-T5
- REST API for document ingestion and querying
- Improved response quality through Retrieval-Augmented Generation (RAG)

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

## System Architecture

```
Documents
     │
     ▼
Text Chunking
     │
     ▼
Sentence Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Semantic Retrieval
     │
     ▼
FLAN-T5 LLM
     │
     ▼
Generated Answer
```

---

## Project Structure

```
enterprise-ai-knowledge-assistant-rag-llm/
│
├── app.py
├── requirements.txt
├── data/
├── embeddings/
├── vector_store/
├── utils/
└── README.md
```

---

## Installation

```bash
git clone https://github.com/MadhuriPesalavari/enterprise-ai-knowledge-assistant-rag-llm.git

cd enterprise-ai-knowledge-assistant-rag-llm

pip install -r requirements.txt

python app.py
```

---

## Future Enhancements

- LangGraph integration
- Agentic AI workflows
- ChromaDB support
- Streaming LLM responses
- Cloud deployment (AWS/Azure)

---

## Author

**Pesalavari Madhuri**

GitHub: https://github.com/MadhuriPesalavari

LinkedIn: https://linkedin.com/in/pesalavari-madhuri
