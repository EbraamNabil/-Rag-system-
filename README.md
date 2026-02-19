# 🧠 Arabic RAG Question Answering System (FAISS + BGE-M3 + Gemini)

An end-to-end **Retrieval Augmented Generation (RAG)** system designed to answer Arabic questions using document-grounded knowledge instead of relying only on LLM memory.

The system performs semantic retrieval using vector embeddings and generates reliable answers using **Google Gemini LLM**.

---

## 🚀 Overview

This project demonstrates how modern AI systems combine:

* Semantic Embeddings
* Vector Databases
* Context Retrieval
* Large Language Models (LLMs)

to build accurate and explainable Question Answering systems.

Instead of hallucinating answers, the model retrieves relevant document chunks before generating responses.

---

## ✨ Features

✅ Arabic document understanding
✅ Semantic similarity search using FAISS
✅ High-quality multilingual embeddings (BAAI BGE-M3)
✅ Chunking with overlap for context preservation
✅ Context-grounded Gemini LLM answers
✅ Interactive command-line chat loop
✅ Secure API key handling using `.env`

---

## 🏗️ Architecture

```
Document (arabic.txt)
        ↓
Text Chunking + Overlap
        ↓
BGE-M3 Embeddings
        ↓
FAISS Vector Index
        ↓
User Question
        ↓
Semantic Similarity Search
        ↓
Top-K Relevant Chunks
        ↓
Prompt Construction
        ↓
Gemini LLM
        ↓
Final Answer
```

---

## 🧠 Technologies Used

* Python
* Sentence Transformers
* BAAI BGE-M3 Embeddings
* FAISS Vector Database
* Google Gemini API
* NumPy
* python-dotenv

---

## 📂 Project Structure

```
.
├── main.py        # Main RAG pipeline
├── arabic.txt     # Arabic knowledge base
├── english.txt    # Optional dataset
├── .env           # API keys (ignored in git)
└── README.md
```

---

## 🔧 Installation

Clone repository:

```
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in project root:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ▶️ Run The Project

```
python main.py
```

Interactive prompt will appear:

```
اكتب سؤالك:
```

Type:

```
exit
```

to close the application.

---

## 🔎 Retrieval Workflow

1. Documents are split into overlapping chunks.
2. Each chunk is converted into embeddings using BGE-M3.
3. FAISS builds a similarity search index.
4. User question embedding retrieves nearest chunks.
5. Retrieved context is injected into Gemini prompt.

This significantly reduces hallucinations and improves accuracy.

---

## 📊 Example Usage

Question:

```
ما هو مفهوم الذكاء الاصطناعي؟
```

System Output:

```
Chunks retrieved:
- ...

الإجابة النهائية:
...
```

---

## 🔒 Safety

The system instructs the LLM to:

* Answer only using retrieved context.
* Respond with "لا أعرف" if the answer is unavailable.

---

## 📈 Future Improvements

* Streamlit Web Interface
* Multi-document ingestion
* Hybrid Search (BM25 + Vector)
* Persistent FAISS index saving
* Source citation display

---

## 👨‍💻 Author

**Ebraam Nabil**

GitHub:
https://github.com/EbraamNabil

---

## ⭐ Purpose

This project demonstrates practical skills in:

* Retrieval Augmented Generation (RAG)
* NLP Engineering
* Vector Databases
* LLM Application Development

Designed for portfolio presentation, internships, and AI engineering roles.
