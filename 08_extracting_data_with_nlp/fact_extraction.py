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
statements = textacy.extract.semistructured_statements(doc, "London")

# Print the results
print("Here are the things I know about London:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {fact}")