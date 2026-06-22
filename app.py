import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import os

from utils.pdf_extractor import extract_text
from utils.summarizer import generate_summary
from utils.keywords import extract_keywords
from utils.rag import create_vector_store, search_chunks
from utils.llm import generate_answer

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Global storage
index_store = None
chunks_store = None
uploaded_meta = {}
chat_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global index_store, chunks_store, uploaded_meta, chat_history

    chat_history = []

    try:

        print("1. Upload started")

        file = request.files["pdf"]

        if file.filename == "":
            return "No file selected"

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)
        print("2. File saved")

        text, page_count = extract_text(filepath)
        text = text[2000:]
        print("3. Text extracted")

        if not text or len(text.strip()) == 0:
            return "Could not extract text from PDF"

        word_count = len(text.split())
        reading_time = max(1, word_count // 250)

        print("4. Generating summary...")
        summary = generate_summary(text)
        print("5. Summary generated")

        print("6. Extracting keywords...")
        keywords = extract_keywords(text)
        print("7. Keywords extracted")

        print("8. Creating vector store...")
        index_store, chunks_store = create_vector_store(text)

        chunk_count = len(chunks_store)

        # ---------- Analytics Chart ----------
        labels = [
            "Pages",
            "Words",
            "Reading Time",
            "Keywords",
            "Chunks"
        ]

        values = [
            page_count,
            word_count,
            reading_time,
            len(keywords),
            chunk_count
        ]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values)
        plt.title("PDF Analytics")

        chart_path = os.path.join("static", "chart.png")

        plt.savefig(chart_path)
        plt.close()
        # ------------------------------------

        print("9. Vector store created")

        uploaded_meta = {
            "filename": file.filename,
            "page_count": page_count,
            "word_count": word_count,
            "reading_time": reading_time,
            "summary": summary,
            "keywords": keywords,
            "full_text": text,
            "chunk_count": chunk_count
        }

        print("10. Rendering result page")

        return render_template(
            "result.html",
            filename=file.filename,
            page_count=page_count,
            word_count=word_count,
            reading_time=reading_time,
            summary=summary,
            keywords=keywords,
            answer=None,
            chat_history=chat_history,
            results=None,
            chunk_count=chunk_count
        )

    except Exception as e:

        print("UPLOAD ERROR:", e)

        return f"Upload Error: {str(e)}"


@app.route("/ask", methods=["POST"])
def ask():

    global index_store, chunks_store, uploaded_meta, chat_history

    if index_store is None:
        return "Please upload a PDF first."

    question = request.form["question"]

    try:

        if "summary" in question.lower():

            answer = generate_answer(
                "Summarize this document in 5 bullet points",
                [uploaded_meta["full_text"][:8000]]
            )

            results = []

        else:

            results = search_chunks(
                question,
                index_store,
                chunks_store
            )

            answer = generate_answer(
                question,
                results
            )

        chat_history.append({
            "question": question,
            "answer": answer
        })

    except Exception as e:

        print("ERROR:", e)

        answer = f"Error generating answer: {str(e)}"
        results = []

    return render_template(
        "result.html",
        chat_history=chat_history,

        filename=uploaded_meta.get("filename", ""),
        page_count=uploaded_meta.get("page_count", 0),
        word_count=uploaded_meta.get("word_count", 0),
        reading_time=uploaded_meta.get("reading_time", 0),
        summary=uploaded_meta.get("summary", ""),
        keywords=uploaded_meta.get("keywords", []),

        answer=answer,
        results=results,
        chunk_count=uploaded_meta.get("chunk_count", 0)
    )


@app.route("/clear_chat", methods=["POST"])
def clear_chat():

    global chat_history

    chat_history = []

    return render_template(
        "result.html",
        chat_history=chat_history,

        filename=uploaded_meta.get("filename", ""),
        page_count=uploaded_meta.get("page_count", 0),
        word_count=uploaded_meta.get("word_count", 0),
        reading_time=uploaded_meta.get("reading_time", 0),
        summary=uploaded_meta.get("summary", ""),
        keywords=uploaded_meta.get("keywords", []),

        answer=None,
        results=None,
        chunk_count=uploaded_meta.get("chunk_count", 0)
    )


if __name__ == "__main__":

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)