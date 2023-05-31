import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Folder path containing the list of documents
folder_path = 'documents'

# List all files in the folder
files = os.listdir(folder_path)

# Read contents of all documents in the folder
documents = []
for file in files:
    with open(os.path.join(folder_path, file), 'r') as f:
        content = f.read()
        documents.append(content)

# User-provided document
user_document = 'path.pdf'

# Preprocess user-provided document
user_document = user_document.lower()

# Calculate TF-IDF vectors for all documents
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents + [user_document])

# Calculate similarity between user-provided document and all documents
similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# Get the index of the most similar document
most_similar_index = similarity_scores.argmax()

# Get the file name of the most similar document
most_similar_file = files[most_similar_index]

# Print the most similar file name
print(most_similar_file)
