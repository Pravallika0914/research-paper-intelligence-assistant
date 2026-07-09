from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-mpnet-base-v2")


import faiss
import numpy as np

def create_vector_store(text):

    chunk_size = 800
    overlap = 200

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += (chunk_size - overlap)

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    return index, chunks
def search_chunks(query, index, chunks, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        query_embedding.astype("float32"),
        top_k
    )

    results = [chunks[i] for i in indices[0]]

    return results