
from meaning_explorer import load_model, get_related_words


def main():
    """Verify that the embeddings model and search function work."""
    print("Loading pretrained word embeddings...")

    model = load_model()

    print("Model loaded successfully!")
    print("Vocabulary size:", len(model.key_to_index))
    print("Vector dimensions:", model.vector_size)

    for word in ["king", "doctor", "xyzabc123"]:
        print(f"Related words for {word}: {get_related_words(word)}")


if __name__ == "__main__":
    main()
