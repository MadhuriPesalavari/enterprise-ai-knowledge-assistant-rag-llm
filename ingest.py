import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DATA_FOLDER = "data"

documents = []

print("Loading documents...")

if not os.path.exists(DATA_FOLDER):
    raise FileNotFoundError(f"'{DATA_FOLDER}' folder not found!")

for file in os.listdir(DATA_FOLDER):
    path = os.path.join(DATA_FOLDER, file)

    print(f"Reading: {file}")

    if file.endswith(".pdf"):
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    elif file.endswith(".txt"):
        loader = TextLoader(path, encoding="utf-8")
        documents.extend(loader.load())

print(f"\nLoaded {len(documents)} documents")

print("Splitting documents...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)

print(f"Split into {len(docs)} chunks")

print("Loading embedding model (first run may take a few minutes)...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating FAISS vector store...")

db = FAISS.from_documents(docs, embedding_model)

print("Saving vector store...")

db.save_local("vectorstore")

print("\n✅ Vectorstore created successfully!")