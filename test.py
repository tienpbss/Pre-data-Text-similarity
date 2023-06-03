

import pickle
import pandas as pd

with open('tfidfvec.pickle', 'rb') as file:
    vec = pickle.load(file)
    words = vec.get_feature_names_out()[500:]


with open('tfidf-file-to-vec.pickle', 'rb') as file:
    file_vec = pickle.load(file)

print(len(file_vec.toarray()))