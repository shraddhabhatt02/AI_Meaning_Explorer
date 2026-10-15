
from functools import lru_cache

import gensim.downloader as api


@lru_cache(maxsize=1)
def load_model():
    """Load and cache the pretrained GloVe embeddings."""
    return api.load("glove-wiki-gigaword-50")


def get_related_words(word, topn=5):
    """Return the words most similar to the supplied word."""
    word = word.lower().strip()

    if not word:
        return []

    model = load_model()

    if word not in model:
        return []

    similar_words = model.most_similar(word, topn=topn)

    return [similar_word for similar_word, score in similar_words]
