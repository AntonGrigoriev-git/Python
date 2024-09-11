'''Unique numbers.'''

numbers = ([1, 2, 3], [2, 3, 4], [3, 4, 5])
unique = set()

for ls in numbers:
    for num in ls:
        unique.add(num)

print(unique)