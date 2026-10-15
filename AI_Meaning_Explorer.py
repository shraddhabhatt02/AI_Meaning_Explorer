import streamlit as st
from meaning_explorer import get_related_words

st.set_page_config(
    page_title="AI Meaning Explorer",
    layout="centered",
)

st.title("AI Meaning Explorer")
st.write(
    "Explore how pretrained word embeddings find "
    "words with similar meanings or associations."
)

word = st.text_input(
    "Enter an English word",
    placeholder="Try king, doctor, ocean...",
)

if word.strip():
    related_words = get_related_words(word)

    if related_words:
        st.subheader(f"Words related to '{word.strip()}'")

        for rank, related_word in enumerate(related_words, start=1):
            st.write(f"{rank}. {related_word}")

    else:
        st.warning(
            "No results found. Try another word from the model's vocabulary."
        )
else:
    st.info("Enter a word above to explore its related words.")

st.caption(
    "Powered by GloVe 50-dimensional pretrained word embeddings."
)
