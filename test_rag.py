from utils.rag import create_vector_store, search_chunks

text = """
Transformers are neural networks used in deep learning.
They rely heavily on self-attention mechanisms.
Self-attention allows each word to focus on other important words in a sentence.
This helps models understand context better than traditional RNNs.
Transformers have revolutionized NLP tasks like translation and summarization.
"""

# Step 1: Create vector store
index, chunks = create_vector_store(text)

# Step 2: Ask different questions
questions = [
    "What are transformers?",
    "What is self-attention?",
    "Why are transformers important?"
]

# Step 3: Test retrieval
for q in questions:
    print("\nQuestion:", q)
    results = search_chunks(q, index, chunks)
    
    for i, r in enumerate(results):
        print(f"Result {i+1}:", r)