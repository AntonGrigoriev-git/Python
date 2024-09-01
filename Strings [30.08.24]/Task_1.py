# Search for reserved words.

import re

# text = 'In the Python programming language, there are reserved words such as \
# conditional operators, these are if and else, there are also loop operators, \
# these are while and for. And it is worth noting a reserved word such as def, \
# which means the beginning of the function definition.'

# reserved_words = 'if, else, while, for, def'

text = input('Enter some text: ')
reserved_words = input('Enter the reserved words separated by commas: ')

list_words = reserved_words.split(', ')

for word in list_words:
    pattern = r'\b{}\b'.format(word)
    text = re.sub(pattern, word.upper(), text)

print(text)