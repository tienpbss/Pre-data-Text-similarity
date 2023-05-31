
import pickle

with open('listText.pickle', 'rb') as f:
    fileText = pickle.load(f)   

print(len(fileText[0]))

