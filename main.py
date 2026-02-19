from dotenv import load_dotenv
import os


# ---------------- CONFIG ----------------
# load environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


# ---------------------------
# Load text file
# ---------------------------
file_path = "arabic.txt"

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

text = load_text(file_path)


# ---------------------------
# Chunking function
# ---------------------------
def chunk_text(text, chunk_size=150, overlap=30):
    words = text.split()

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))

        start += chunk_size - overlap

    return chunks


documents = chunk_text(text)

print("no of chunks:", len(documents))


# ---------------------------
# Load embedding model
# ---------------------------
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")


# ---------------------------
# Generate embeddings
# ---------------------------
doc_embeddings = model.encode(
    documents,
    normalize_embeddings=True
)


# ---------------------------
# Create FAISS index
# ---------------------------
import numpy as np
import faiss

dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(np.array(doc_embeddings))

print("Index ready")


# ---------------------------
# Setup Gemini LLM
# ---------------------------
import google.generativeai as genai

genai.configure(api_key=api_key)


llm = genai.GenerativeModel("gemini-2.5-flash")


# ---------------------------
# Query loop
# ---------------------------
while True:
    query = input("\nاكتب سؤالك (اكتب exit للخروج): ")

    if query.lower() == "exit":
        print("تم إنهاء البرنامج.")
        break

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    k = 3
    scores, indices = index.search(query_embedding, k)

    results = [documents[i] for i in indices[0]]

    print("\nChunks retrieved:")
    for r in results:
        print("-", r[:120], "...")

    context = "\n".join(results)

    prompt = f"""
اعتمد فقط على المعلومات التالية للإجابة.
إذا لم تجد الإجابة قل لا أعرف.

المعلومات:
{context}

السؤال:
{query}

الإجابة:
"""

    response = llm.generate_content(prompt)

    print("\nالإجابة النهائية:")
    print(response.text)
