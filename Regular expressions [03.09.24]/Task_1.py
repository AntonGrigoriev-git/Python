'''Search for words with the letter 'a'.'''

import re

text = "An apple is not an apricot, because an apricot is not an apple;)"
pattern = r"\b[aA]\w*"
search_words = re.findall(pattern, text)

print(search_words)