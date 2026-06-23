# 📄 RAG Document Assistant

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask natural language questions. The system retrieves relevant document chunks using semantic search and generates context-aware answers.

## 🚀 Features

* Upload and process PDF documents
* Automatic document chunking
* Semantic search using vector embeddings
* Context-aware question answering
* ChromaDB vector storage
* HuggingFace sentence embeddings
* Interactive Streamlit web interface

## 🏗️ Architecture

PDF Upload → Document Loading → Text Chunking → Embedding Generation → ChromaDB Vector Store → Similarity Search → Answer Generation

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Transformers
* PyPDF
* Sentence Transformers

## 📂 Project Structure

```text
rag-document-assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── document_loader.py
│   ├── rag_pipeline.py
│   └── vector_store.py
│
└── data/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/SanthoshGopi-B/rag-document-assistant.git
cd rag-document-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📋 Example Questions

* What are the candidate's technical skills?
* What projects are mentioned in the document?
* What programming languages does the candidate know?
* Summarize the experience section.
* What tools and technologies are used?

## 💡 How It Works

1. User uploads a PDF document.
2. PDF content is extracted using PyPDFLoader.
3. Text is split into smaller chunks.
4. Chunks are converted into vector embeddings.
5. ChromaDB stores the embeddings.
6. User submits a question.
7. Relevant chunks are retrieved using similarity search.
8. The model generates an answer based on retrieved context.

## 🎯 Use Cases

* Resume Analysis
* Research Document Q&A
* Policy Document Search
* Knowledge Base Assistant
* Educational Content Exploration

## 📈 Future Improvements

* Multi-PDF support
* Source citations
* Conversational memory
* Advanced LLM integration
* Cloud deployment
* User authentication

## 👨‍💻 Author

**Santhosh Gopi**

GitHub: https://github.com/SanthoshGopi-B
