import pickle
import pandas as pd
import numpy as np

with open('tfidfvec.pickle', 'rb') as f:
    tv = pickle.load(f)   

with open('tfidf-file-to-vec.pickle', 'rb') as f:
    tv_matrix = pickle.load(f)   

tv_matrix = tv_matrix.toarray()[:, 5000:]

vocab = tv.get_feature_names_out()
pd.set_option("min_rows", 20)
pd.set_option("min_column", 20)

print(pd.DataFrame(np.round(tv_matrix, 2), columns=vocab[5000:]))
