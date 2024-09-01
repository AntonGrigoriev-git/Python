# Substrings.

user_string = input('Enter a string: ')
substrings = []

for i in range(len(user_string)):
    for j in range(i + 1, len(user_string) + 1):
        substrings.append(user_string[i:j])

for substring in substrings:
    print(substring)