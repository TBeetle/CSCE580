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
