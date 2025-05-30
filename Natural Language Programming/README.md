
# Wordcount NLP Project

This project contains various Natural Language Processing (NLP) experiments and scripts covering tokenization, text vectorization, sentiment analysis, and chatbot-related use cases.

## Folder Structure

- `notebooks/` – Contains all exploratory and instructional Jupyter notebooks.
- `scripts/` – Contains Python scripts implementing core NLP functionalities.

## Included Notebooks
- **wordcount.ipynb** – Word count and preprocessing tasks.
- **IMDBReview_sentiment_analysis.ipynb** – Basic sentiment analysis example using IMDB reviews.
- **mahatmagandhi.ipynb** – Wordcloud and exploratory processing for Gandhi’s speeches.

## Included Scripts
- **NLTK.py** – Tokenization, stopword removal, stemming, and lemmatization.
- **BagOfWords.py** – Basic Bag-of-Words model.
- **OneHot_Vectors.py** – One-hot encoding for token sequences.
- **simpleChat.py** – A simple chatbot to extract email and phone numbers from a file.
- **NLP** - A script of tokenisation of word in dataset.

## Requirements
- Python 3.8+
- pandas, numpy
- nltk
- re

## How to Run
1. Clone the repository or copy this folder.
2. Install required packages using pip:
   ```
   pip install pandas numpy nltk
   ```
3. Open and run the notebooks using Jupyter, VSCode or Colab.

## Note
- Some files require local text files like `Text.txt` or a dataset CSV. Make sure to provide them in the correct path.
