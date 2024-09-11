'''English-French dictionary.'''

dictionary = {
    "home": "accueil",
    "ocean": "océan",
    "sky": "ciel",
    "air": "aérien"
}

while True:
    print("1. Add")
    print("2. Delete")
    print("3. Search")
    print("4. Replacement")
    print("0. Exit")
    choice = input("Select an action (0-4): ")

    if choice == '1':
        english = input("Enter a word in English: ")
        french = input(f"Enter the translation of the word {english} into French: ")
        dictionary[english] = french
        print(dictionary)

    elif choice == "2":
        english = input("Enter the word in English to delete: ")
        if english in dictionary:
            del dictionary[english]
            print(dictionary)
        else:
            print("The entered word is missing")

    elif choice == "3":
        english = input("Enter a word in English: ")
        if english in dictionary:
            print(f"The word {english} in French: {dictionary[english]}")
        else:
            print("The entered word is missing")

    elif choice == "4":
        english = input("Enter a word in English: ")
        french = input(f"Enter the new meaning of the word {english} in French: ")
        if english in dictionary:
            dictionary[english] = french
            print(dictionary)
        else:
            print("The entered word is missing")

    elif choice == "0":
        break

    else:
        print("Invalid value, try again")