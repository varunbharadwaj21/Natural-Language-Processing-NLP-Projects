# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:58:02 2024

@author: NFSU
"""

sentence_bow = {}
sentence = "Today is 04th March, 2024 and Monday. we are currently at NFSU."

for token in sentence.split():
    sentence_bow[token] = 1
print(sentence_bow)


#%% bow example 2

# import pandas as pd

# sentence = "Today is 04th March, 2024 and Monday. \n we are currently at NFSU."

# corpus = {}
# for i, s in enumerate(sentence.split("\n")):
#     corpus['s{}'.format(i)] = dict((tok, 1) for tok in s.split())

# df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
# print(df)
