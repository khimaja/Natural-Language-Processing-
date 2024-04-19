import nltk
from nltk.corpus import movie_reviews
from nltk import bigrams, word_tokenize
from collections import Counter
import random

# Download NLTK resources
nltk.download('movie_reviews')
nltk.download('punkt')

# Load movie reviews corpus
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
random.shuffle(documents)

# Tokenization
all_words = [word.lower() for word in movie_reviews.words()]
tokens = [word.lower() for word in all_words if word.isalpha()]

# Create bigrams
ngrams = list(bigrams(tokens))

# Count frequencies of bigrams
bigram_counts = Counter(ngrams)

# Function to predict next word
def predict_next_word(previous_word):
    candidates = [bigram[1] for bigram in bigram_counts if bigram[0] == previous_word]
    if candidates:
        return max(set(candidates), key=candidates.count)
    else:
        return None

# Test prediction
previous_word = 'movie'
next_word = predict_next_word(previous_word)
print(f"Predicted next word after '{previous_word}': {next_word}")
