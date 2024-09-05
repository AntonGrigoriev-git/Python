'''Replacing words.'''

import re

text = "Old house, OLD books, old photos, oLD someTHinG ELEs..."
matches = re.findall("old", text, re.IGNORECASE)

for word in matches:
    if word.isupper():
        text = re.sub(word, "NEW", text)
    elif word.islower():
        text = re.sub(word, "new", text)
    elif word.istitle():
        text = re.sub(word, "New", text)
    else:
        text = re.sub(word, "new", text)

print(text)