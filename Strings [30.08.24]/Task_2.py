# Arithmetic expression.

import re

arithmetic_expression = input('Enter arithmetic expression: ')
pattern = re.split(r'(\d+\.\d+|\d+)', arithmetic_expression)

first_operand = float(pattern[1])
operator = pattern[2]
second_operand = float(pattern[3])

if operator == '+':
    print(first_operand + second_operand)
elif operator == '-':
    print(first_operand - second_operand)
elif operator == '*':
    print(first_operand * second_operand)
elif operator == '/':
    if second_operand != 0:
        print(first_operand / second_operand)
    else:
        print('Infinity')
else:
    print('Invalid value')