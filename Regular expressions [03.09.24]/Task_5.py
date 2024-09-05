'''The time.'''

import re

pattern = r"^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"

while True:
    time = input("Enter the time in the format 'HH:MM:SS': ")
    if re.match(pattern, time):
        print(f"The time is {time}.")
        break
    else:
        print("Enter the time in the specified format.")