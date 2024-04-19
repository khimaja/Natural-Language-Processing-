import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')

# Sample text
text = "The rusty key turned with a groan, revealing a dusty attic. Sunlight streamed across Amelia, illuminating forgotten treasures. A chipped music box, a faded teddy bear, and a worn leather journal whispered tales of a life long past. A smile tugged at Amelia's lips - a treasure trove of memories awaited."

# Tokenization
tokens = word_tokenize(text)

# Morphological analysis (Lemmatization)
lemmatizer = WordNetLemmatizer()
morphological_analysis = []

for word in tokens:
    if word.lower() in words.words():
        lemma = lemmatizer.lemmatize(word)
        morphological_analysis.append((word, lemma))

# Displaying output
print("Morphological Analysis (Lemmatization):")
for word, lemma in morphological_analysis:
    print(f"{word}: {lemma}")
