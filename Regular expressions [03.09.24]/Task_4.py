'''The phone number.'''

import re

pattern = r"^\+\d \(\d{3}\) \d{3}-\d{4}$"

while True:
    phone_number = input("Enter the phone number in the format '+X (XXX) XXX-XXXX': ")
    if re.match(pattern, phone_number):
        print(f"The phone number is {phone_number}.")
        break
    else:
        print("Enter the phone number in the specified format.")