'''Min number of the list.'''

def min_number(num):
    return min(num)

numbers = input("Enter the numbers separated by a space: ")
numbers_list = list(map(int, numbers.split()))
print(min_number(numbers_list))