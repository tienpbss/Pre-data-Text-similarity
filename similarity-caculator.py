
import pickle
from pre_text import clean_text
from sklearn.metrics.pairwise import cosine_similarity

with open('listFile.pickle', 'rb') as file :
    listFile = pickle.load(file)
with open('tfidfvec.pickle', 'rb') as file :
    tfidfvec = pickle.load(file)
with open('tfidf-file-to-vec.pickle', 'rb') as file :
    tfidf_file_to_vec = pickle.load(file)


'''
Multimedia50-55 
Multimedia_Database_Management_Systems_(Artech House)-20-50
1  CLASS ACTION SETTLEMENT AGREEMENT AND RELEASE 5
1 Approved April 9 2010 Revised April 12 2019 AST Guidelines for
100 Philosophy parapsychology and occultism psychology
900 History geography and auxiliary disciplines
'''
query = ''

while True:
    query = input('Type name file to search: ')
    if query == 'q': break
    try:
        text = clean_text(query+'.pdf')
    except:
        print('some thing wrong, please try again')
        continue
    text_to_vec = tfidfvec.transform([text])
    similarity = cosine_similarity(text_to_vec, tfidf_file_to_vec)
    # print(similarity)
    similar_indices = similarity.argsort()[0][::-1][:10]
    res = [{listFile[i], similarity[0][i]} for i in similar_indices]
    for i in res:
        print(i)


