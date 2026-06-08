import os
import re
import shutil
from pathlib import Path

import chromadb
import gradio as gr
from dotenv import load_dotenv
from groq import Groq
from chromadb.utils import embedding_functions


DOCUMENTS_DIR = Path("documents")
CHROMA_PATH = "chroma_db"
CHROMA_COLLECTION = "unofficial_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.3-70b-versatile"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
TOP_K = 5


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")


groq_client = Groq(api_key=GROQ_API_KEY)

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=embedding_function,
    metadata={"hnsw:space": "cosine"},
)


def clean_text(text: str) -> str:
    """Basic cleanup for copied text documents."""
    text = re.sub(r"\r\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def load_documents():
    """Load local .txt documents from the documents folder."""
    docs = []

    for path in sorted(DOCUMENTS_DIR.glob("*.txt")):
        raw_text = path.read_text(encoding="utf-8")
        text = clean_text(raw_text)

        title = path.stem
        url = "Local file"

        for line in text.splitlines():
            if line.lower().startswith("title:"):
                title = line.split(":", 1)[1].strip()
            elif line.lower().startswith("source url:"):
                url = line.split(":", 1)[1].strip()

        docs.append({
            "title": title,
            "url": url,
            "path": str(path),
            "text": text,
        })

    return docs


def chunk_text(text: str, source_title: str, source_url: str, source_path: str):
    """Split text into overlapping character chunks."""
    chunks = []
    start = 0
    chunk_index = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end].strip()

        if len(chunk) >= 80:
            chunks.append({
                "text": chunk,
                "source_title": source_title,
                "source_url": source_url,
                "source_path": source_path,
                "chunk_index": chunk_index,
                "chunk_id": f"{Path(source_path).stem}_{chunk_index}",
            })
            chunk_index += 1

        if end >= len(text):
            break

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def ingest_documents(force_reset: bool = False):
    """Load, chunk, embed, and store documents in ChromaDB."""
    global collection

    if force_reset and Path(CHROMA_PATH).exists():
        shutil.rmtree(CHROMA_PATH)
        new_client = chromadb.PersistentClient(path=CHROMA_PATH)
        collection = new_client.get_or_create_collection(
            name=CHROMA_COLLECTION,
            embedding_function=embedding_function,
            metadata={"hnsw:space": "cosine"},
        )

    if collection.count() > 0:
        return f"Vector store already populated with {collection.count()} chunks."

    docs = load_documents()
    all_chunks = []

    for doc in docs:
        all_chunks.extend(
            chunk_text(
                text=doc["text"],
                source_title=doc["title"],
                source_url=doc["url"],
                source_path=doc["path"],
            )
        )

    if not all_chunks:
        return "No chunks produced. Check the documents folder."

    collection.add(
        documents=[chunk["text"] for chunk in all_chunks],
        metadatas=[
            {
                "source_title": chunk["source_title"],
                "source_url": chunk["source_url"],
                "source_path": chunk["source_path"],
                "chunk_index": chunk["chunk_index"],
            }
            for chunk in all_chunks
        ],
        ids=[chunk["chunk_id"] for chunk in all_chunks],
    )

    return f"Ingested {len(docs)} documents and stored {len(all_chunks)} chunks."


def retrieve(query: str, top_k: int = TOP_K):
    """Retrieve top-k semantically relevant chunks."""
    if collection.count() == 0:
        ingest_documents()

    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    chunks = []
    for text, metadata, distance in zip(documents, metadatas, distances):
        chunks.append({
            "text": text,
            "source_title": metadata["source_title"],
            "source_url": metadata["source_url"],
            "source_path": metadata["source_path"],
            "chunk_index": metadata["chunk_index"],
            "distance": distance,
        })

    return chunks


def format_sources(chunks):
    """Format retrieved chunks for display."""
    lines = []
    for i, chunk in enumerate(chunks, start=1):
        lines.append(
            f"Source {i}: {chunk['source_title']}\n"
            f"Distance: {chunk['distance']:.3f}\n"
            f"URL: {chunk['source_url']}\n"
            f"Chunk: {chunk['text'][:600]}..."
        )
    return "\n\n---\n\n".join(lines)


def generate_response(query: str, retrieved_chunks):
    """Generate a grounded answer using only retrieved chunks."""
    if not retrieved_chunks:
        return "I do not have enough information in the loaded documents to answer that."

    context_blocks = []
    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_blocks.append(
            f"[Source {i}: {chunk['source_title']}]\n"
            f"URL: {chunk['source_url']}\n"
            f"{chunk['text']}"
        )

    context = "\n\n---\n\n".join(context_blocks)

    system_prompt = (
        "You are The Unofficial Guide, a RAG assistant for student-shared WGU cybersecurity program knowledge. "
        "Answer using only the retrieved context provided by the user message. "
        "Do not use outside knowledge, assumptions, or general knowledge. "
        "If the context does not contain enough information to answer, say that the loaded documents do not provide enough information. "
        "Cite the source title or source number for every claim."
    )

    user_prompt = f"""
Retrieved context:
{context}

User question:
{query}

Write a concise answer using only the retrieved context. Include source attribution in the answer.
"""

    response = groq_client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
    )

    return response.choices[0].message.content


def ask(question):
    """End-to-end query function for the UI."""
    if not question.strip():
        return "Please enter a question.", ""

    chunks = retrieve(question)
    answer = generate_response(question, chunks)
    sources = format_sources(chunks)

    return answer, sources


def build_ui():
    ingest_status = ingest_documents()

    with gr.Blocks(title="The Unofficial Guide") as demo:
        gr.Markdown("# The Unofficial Guide: WGU Cybersecurity Student Survival Guide")
        gr.Markdown(
            "Ask questions about student-shared advice on WGU BSCSIA acceleration, certifications, course difficulty, and common bottlenecks."
        )
        gr.Markdown(f"**Startup status:** {ingest_status}")

        question = gr.Textbox(
            label="Your question",
            placeholder="Example: What do students say are common ways to accelerate the WGU BSCSIA program?",
            lines=2,
        )

        ask_button = gr.Button("Ask")

        answer = gr.Textbox(label="Grounded answer", lines=8)
        sources = gr.Textbox(label="Retrieved sources", lines=16)

        ask_button.click(fn=ask, inputs=question, outputs=[answer, sources])
        question.submit(fn=ask, inputs=question, outputs=[answer, sources])

        gr.Examples(
            examples=[
                "What do students say are common ways to accelerate the WGU BSCSIA program?",
                "What do students say are some of the hardest parts of the WGU cybersecurity program?",
                "What certifications or prior credits can help reduce the number of courses?",
                "What advice do students give for preparing for cybersecurity certification courses?",
                "Can the documents tell me which WGU instructor is best?",
            ],
            inputs=question,
        )

    return demo


if __name__ == "__main__":
    demo = build_ui()
    demo.launch()