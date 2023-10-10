import json
import string
import random

import nltk
import numpy as np
from nltk import WordNetLemmatizer

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")
nltk.download("wordnet")
data_root = "/Users/tylerbeetle/Desktop/CSCE581/data/"
f = open(data_root+'data.json')
data = json.load(f)
print(data)


words = []
classes = []
data_x = []
data_y = []

for intentions in data["intentions"]:
    for pattern in data["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        data_x.append(pattern)
        data_y.append(intentions(["tag"]) ,
                      
    if intent("tag") not in classes:
        classes.append(intentions("tag"))

lemmatizer = WordNetLemmatizer()

words = 

