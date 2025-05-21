# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:00:12 2024

@author: NFSU
"""

import pandas as pd
import numpy as np

sentence = "Today is 04th March 2024. Month of March is hot."
token_sequence = sentence.split()
vocab = sorted(set(token_sequence))

onehot_sot = np.zeros((len(token_sequence), len(vocab)), int)

for i, word in enumerate(token_sequence):
    onehot_sot[i, vocab.index(word)] = 1
    
print(pd.DataFrame(onehot_sot, columns = vocab))