
import fitz
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def getText(filePath):
    '''Get text from pdf file'''
    doc = fitz.open(filePath)
    text = ""
    for page in doc:
        text+=page.get_text()
    return text


def remove_stopwords(text):
    '''Remove stop word'''
    stop_words = set(stopwords.words('english')) # Define the set of English stopwords
    words = nltk.word_tokenize(text) # Tokenize the input text
    filtered_words = [word for word in words if word.lower() not in stop_words] # Remove stopwords
    return ' '.join(filtered_words) # Join the filtered words into a string

def stem_words(text):
    '''convert to root word'''
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
    text = remove_stopwords(text) # remove stop word
    text = stem_words(text) #conver words to root words
    text = text.encode('ascii', 'ignore').decode() #remove character not ascii
    return text
