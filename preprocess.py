
import os
import fitz
import re
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english')) 
# print(len(stop_words))
# print(stop_words)


def getText(filePath):
    '''Get text from pdf file'''
    doc = fitz.open(filePath)
    text = ""
    for page in doc:
        text+=page.get_text()
    return text
 

def remove_stopwords(text):
    stop_words = set(stopwords.words('english')) # Define the set of English stopwords
    words = nltk.word_tokenize(text) # Tokenize the input text
    filtered_words = [word for word in words if word.lower() not in stop_words] # Remove stopwords
    return ' '.join(filtered_words) # Join the filtered words into a string


