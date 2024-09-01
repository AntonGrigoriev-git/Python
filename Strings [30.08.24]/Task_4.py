# The number of different characters.

user_string = input('Enter a string: ')

sum_letters = sum(char.isalpha() for char in user_string)
sum_digits = sum(char.isdigit() for char in user_string)
sum_symbols = sum(not char.isalnum() and not char.isspace() for char in user_string)

print(f'Count of letters = {sum_letters}')
print(f'Count of digits = {sum_digits}')
print(f'Count of special symbols = {sum_symbols}')