# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:04:46 2024

@author: NFSU
"""

#%% Divide Doc into tokens

import nltk
# nltk.download("punkt")

filename = r"NLTK\Text.txt"
text = open(filename,"r",encoding="utf-8").read()

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
sentence = tokenizer.tokenize(text)
print(sentence)

#%% removing stopwords

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

mySW = set(stopwords.words("english"))
text = text.replace("\n"," ")
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
tokens = word_tokenize(text)
for token in tokens:
  if token not in mySW:
    print(token)

#%% removing stopwords and punctuation

from string import punctuation
import nltk
from nltk.corpus import stopwords

for token in tokens:
    if token not in mySW and token not in punctuation:
        print(token)

#%% Stemmer

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem('cars'))
print(stemmer.stem('brushing'))
print(stemmer.stem('formality'))
print(stemmer.stem('motivation'))
print(stemmer.stem('revolution'))

#%% Lemmatizer

# nltk.download('wordnet')
# nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('better',pos='a'))
