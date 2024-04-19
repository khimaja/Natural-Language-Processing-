import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import words

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

# Sample text
# text = "NLTK is a powerful Python library for natural language processing tasks."
text = "Submiting the 4 lab expermens before the dedline."

# Tokenization
tokens = word_tokenize(text)
print("Tokenization:")
print(tokens)

# Filtration (remove punctuation)
filtered_tokens = [word for word in tokens if word.isalnum()]
print("\nFiltration:")
print(filtered_tokens)

# Script Validation
english_words = set(words.words())
valid_words = [word for word in filtered_tokens if word.lower() in english_words]
print("\nScript Validation:")
print(valid_words)

# Stop Word Removal
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in valid_words if word.lower() not in stop_words]
print("\nStop Word Removal:")
print(filtered_words)

# Stemming
porter = PorterStemmer()
stemmed_words = [porter.stem(word) for word in filtered_words]
print("\nStemming:")
print(stemmed_words)
