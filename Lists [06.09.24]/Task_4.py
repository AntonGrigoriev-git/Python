'''Line alignment.'''

ls_1 = list(input("Enter first word: "))
ls_2 = list(input("Enter second word: "))

if len(ls_1) > len(ls_2):
    length_dif = len(ls_1) - len(ls_2)
    for _ in range(length_dif):
        ls_2.append('_')
    print(ls_2)
else:
    length_dif = len(ls_2) - len(ls_1)
    for _ in range(length_dif):
        ls_1.append('_')
    print(ls_1)