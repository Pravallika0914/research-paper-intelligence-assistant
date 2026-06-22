# 📄 Research Paper Intelligence Assistant

An AI-powered document analysis and question-answering system built with Flask, FAISS, Sentence Transformers, and Gemini API.

---

## 🚀 Features

- 📂 PDF Upload
- 📝 Text Extraction
- 📌 Keyword Extraction
- 📄 Automatic Summary Generation
- 🔍 Semantic Search with FAISS
- 🤖 RAG-based Question Answering
- 💬 Conversational Chat History
- 📊 Analytics Dashboard
- 🌙 Dark Mode
- 📑 Source Attribution

---

## 🛠 Tech Stack

- Python
- Flask
- Sentence Transformers
- FAISS
- Gemini API
- HTML
- CSS
- Matplotlib

---

## 📁 Project Structure



```text
research-paper-simplifier/
│
├── static/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
├── utils/
│   ├── keywords.py
│   ├── llm.py
│   ├── pdf_extractor.py
│   ├── rag.py
│   └── summarizer.py
│
├── venv/
│
├── .env
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
├── test_keywords.py
├── test_models.py
├── test_rag.py
└── test.py
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/research-paper-simplifier.git
cd research-paper-simplifier
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```powershell
venv\Scripts\Activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

---

## 🔄 Workflow

1. Upload PDF
2. Extract text
3. Generate summary
4. Extract keywords
5. Create embeddings
6. Store vectors in FAISS
7. Retrieve relevant chunks
8. Generate context-aware answers

---

## 📷 Screenshots

(Add screenshots here after uploading to GitHub)

---

## 🔮 Future Improvements

- Multi-PDF support
- OCR support
- LangChain integration
- Persistent chat memory
- Cloud deployment

---

## 👨‍💻 Author

Pravallika