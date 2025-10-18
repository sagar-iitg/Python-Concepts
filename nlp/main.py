import nltk
from nltk.tokenize import word_tokenize

# Explicitly add path to NLTK data
nltk.data.path.append("/Users/sk/nltk_data")

text = "Tokenization isn't always easy."
tokens = word_tokenize(text)
print(tokens)
