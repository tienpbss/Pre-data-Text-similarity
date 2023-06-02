

import pickle

with open('tfidfvec.pickle', 'rb') as file:
    vec = pickle.load(file)
    words = vec.get_feature_names_out()

with open('vocabulary.txt', 'w') as file:
    for i in words:
        file.write(i+' ')

print(len(words))