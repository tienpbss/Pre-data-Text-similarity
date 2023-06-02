

import pickle
import pandas as pd

with open('tfidfvec.pickle', 'rb') as file:
    vec = pickle.load(file)
    words = vec.get_feature_names_out()[500:]


with open('tfidf-file-to-vec.pickle', 'rb') as file:
    file_vec = pickle.load(file)

cv_matrix = file_vec.toarray()[:, 500:]

# get all unique words in the corpus
# show document feature 
pd.set_option('display.min_rows', 15)
print(pd.DataFrame(cv_matrix, columns=words))