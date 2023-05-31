from preprocess import *
import nltk
import re
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def stem_words(text):
    word_tokens = nltk.word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return ' '.join(stems)

def clean_text(filePath):
    text = getText(filePath)
    text = text.lower()
    text = re.sub(r'http\S+', '', text) # remove url
    # text = ''.join([i for i in text if not i.isdigit()]) #remove number
    text = re.sub(r'\d+', '', text) #remove number
    text = re.sub(r'[^\w\s]', '', text) # remove special character, white space

    # text = stem_words(text)

    text = text.encode('ascii', 'ignore').decode() #remove character not ascii
    text = remove_stopwords(text) # remove stop word
    return text