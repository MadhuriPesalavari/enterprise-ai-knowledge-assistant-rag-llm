import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# =========================
# Load Embeddings
# =========================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

# =========================
# Load FLAN-T5 Model
# =========================

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# =========================
# Answer Generator
# =========================

def generate_answer(context, question):
    prompt = f"""
Answer ONLY using the context below.
If answer not found, say "Answer not found in documents."

Context:
{context}

Question:
{question}
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,      # ✅ Only this (no max_length)
        temperature=0.3,
        do_sample=True
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()


# =========================
# Chat Loop
# =========================

if __name__ == "__main__":
    print("✅ Enterprise Assistant Ready\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        docs = db.similarity_search(query, k=5)

        if not docs:
            print("Answer not found in documents.\n")
            continue

        context = "\n".join([doc.page_content for doc in docs])

        answer = generate_answer(context, query)

        print("\nAnswer:", answer, "\n")