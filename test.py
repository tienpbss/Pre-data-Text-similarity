from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity

import pickle
import os

# MONGO_URL = 'mongodb+srv://tien:123456Aa@cluster0.l9o94oo.mongodb.net/test?retryWrites=true&w=majority'
MONGO_LOCAL = 'mongodb://localhost:27017'

client = MongoClient(MONGO_LOCAL)
    


database = client['book']

collection = database['bookFeature']

docs = collection.find_one()
with open('tfidfvec.pickle', 'rb') as f:
    tfidfvec = pickle.load(f)    

doc_vec = pickle.loads(docs['vector'])

docs['score'] = cosine_similarity('Transformers For Markdown Article Rewriting', doc_vec)


print(docs['score'])

