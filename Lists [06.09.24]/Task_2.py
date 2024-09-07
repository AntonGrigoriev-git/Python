'''Deleting a value.'''

digits = [1, 2, 3, 4, 5, 3, 4, 4, 3]
delete_digit = int(input("Enter the digit of list: "))

# Решил итерировать через копию digits, чтоб не создвать новый список
for num in list(digits):
    if delete_digit == num:
        digits.remove(num)

print(digits)