'''Search for the capital.'''

geography = [
    ("Russia", "Moscow"),
    ("Greece", "Athens"),
    ("Switzerland", "Bern"),
    ("Belgium", "Brussels")
]

dict_geography = dict(geography)
country = input("Enter the country: ")

if country in dict_geography.keys():
    print(f"The capital of {country} is {dict_geography[country]}")
else:
    print("This country is not on the list")