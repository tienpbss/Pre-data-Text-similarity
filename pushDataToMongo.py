from pymongo import MongoClient

import pickle
import os

# MONGO_URL = 'mongodb+srv://tien:123456Aa@cluster0.l9o94oo.mongodb.net/test?retryWrites=true&w=majority'
MONGO_LOCAL = 'mongodb://localhost:27017'

client = MongoClient(MONGO_LOCAL)

# with open('tfidf-file-to-vec.pickle', 'rb') as f:
#     vector = pickle.load(f)

with open('tfidf-file-to-vec.pickle', 'rb') as f:
    vec = pickle.load(f)

with open('listFile.pickle', 'rb') as f:
    fileName = pickle.load(f)    


database = client['documentCSDLDPT']

collection = database['docFeature']

doc_path = 'D:\Document-CSDLDPT'


for i in range(len(fileName)):
    name = fileName[i]
    vector = pickle.dumps(vec[i])
    record = {
        'name': name,
        'path': os.path.join(doc_path, name),
        'vector': vector
    }
    collection.insert_one(record)



