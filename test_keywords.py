from keybert import KeyBERT

kw_model = KeyBERT()

text = """
Transformers have become the dominant architecture
for natural language processing tasks.
"""

keywords = kw_model.extract_keywords(
    text,
    keyphrase_ngram_range=(1,2),
    stop_words="english",
    top_n=5
)

print(keywords)