import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample text
# text = "NLTK is a powerful Python library for natural language processing tasks."
text = "Imagine all the people living life in peace."

# Tokenization
tokens = word_tokenize(text)

# POS tagging
pos_tags = pos_tag(tokens)

# Displaying output
print("POS tagging:")
print(pos_tags)
