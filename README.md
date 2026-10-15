# AI Meaning Explorer

A beginner-friendly Python project that explores relationships between words using pretrained GloVe word embeddings and Streamlit.

## Overview

AI Meaning Explorer accepts an English word and returns the five words with the most similar vector representations according to the pretrained GloVe model.

This project demonstrates how word embeddings represent language numerically and how those representations can be used to explore relationships between words.

## Features

- Search for related words using a pretrained GloVe model.
- Display ranked results in a Streamlit web interface.
- Handle empty input and words that are not in the model vocabulary.
- Configure the number of related words returned.
- Run automated unit tests.

## Technologies Used

- Python
- Streamlit
- Gensim
- GloVe 50-dimensional pretrained word embeddings
- Unittest

## Project Structure

```text
AI-Meaning-Explorer/
├── AI_Meaning_Explorer.py
├── meaning_explorer.py
├── test_meaning_explorer.py
├── download_embeddings.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Meaning-Explorer
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m streamlit run AI_Meaning_Explorer.py
```

The first run may download the pretrained GloVe model, which Gensim caches locally for future use.

## Run Tests

```bash
python -m unittest test_meaning_explorer.py -v
```

## How It Works

1. The application loads the pretrained GloVe word embeddings.
2. The user enters a word in the Streamlit interface.
3. Gensim retrieves the most similar words using vector similarity.
4. The application displays the results.

## Learning Objectives

- Understand pretrained word embeddings.
- Explore semantic and contextual relationships between words.
- Separate application logic from user interface code.
- Write unit tests for Python functions.
- Build and document a small AI-related application.

## Limitations

The results are based on relationships learned from the model's training corpus. Similar words are not necessarily synonyms, and the model may reflect biases present in its training data.

The application requires the entered word to exist in the model vocabulary.

## Future Improvements

- Display similarity scores.
- Add input validation and improved error handling.
- Add more interactive visualizations.
- Improve automated test coverage.

## License

No license has been selected yet. Add an appropriate open-source license before inviting others to reuse or distribute the project.
