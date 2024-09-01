# A number that is divisible by six

number = input("You wanna check if the number is divisible by six, then enter a number: ")
digits = []
digits_sum = 0

for i in number:
    digits.append(int(i))

for num in digits:
    digits_sum += num

if digits_sum % 3 == 0 and int(number[-1]) % 2 == 0:
    print(f"The number {number} is divisible by six")
else:
    print(f"The number {number} is indivisible by six")