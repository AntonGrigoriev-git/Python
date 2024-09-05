'''Searching for digits.'''

import re

text = input("Enter some text: ")
pattern = r"\d+"
search_digits = re.findall(pattern, text)
print(search_digits)