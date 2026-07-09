from keybert import KeyBERT

kw_model = KeyBERT()

def extract_keywords(text):

    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1,2),
        stop_words="english",
        top_n=10
    )

    return [keyword[0] for keyword in keywords]