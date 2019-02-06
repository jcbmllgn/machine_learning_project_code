import spacy
import textacy.extract
from pathlib import Path

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
text = Path("london.txt").read_text()

# Parse the document with spaCy
doc = nlp(text)

# Extract semi-structured statements
noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)

# Convert noun chunks to lowercase strings
noun_chunks = map(str, noun_chunks)
noun_chunks = map(str.lower, noun_chunks)

# Print out any nouns that are at least 2 words long
for noun_chunk in set(noun_chunks):
    if len(noun_chunk.split(" ")) > 1:
        print(noun_chunk)
