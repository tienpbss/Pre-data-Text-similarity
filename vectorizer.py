from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

from module import *

vectorizer = TfidfVectorizer()


directory = 'documents'
 
all_text = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    text = clean_text(f)
    all_text.append(text)

text1 = clean_text('D:\Study\Visual Studio Code\Find Document\Multimedia50-55.pdf')
# text2 = clean_text('D:\Study\Visual Studio Code\Find Document\Multimedia_Database_Management_Systems_(Artech House)-20-50.pdf')
X = vectorizer.fit_transform(all_text)

X2 = vectorizer.transform([text1])
print(cosine_similarity(X, X2))
# print(vectorizer.vocabulary_)

# print(all_text)
print(len(vectorizer.vocabulary_))