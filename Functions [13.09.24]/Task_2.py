'''The degree of numbers.'''

def get_degree(numbers, degree):
    return [x**degree for x in numbers]

numbers = input("Enter the numbers separated by a space: ")
degree = int(input("Enter the degree: "))
numbers_list = list(map(int, numbers.split()))
print(get_degree(numbers_list, degree))