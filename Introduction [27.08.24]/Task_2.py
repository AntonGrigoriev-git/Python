# Calculating the remaining amount

salary = int(input("Enter the salary: "))
loan = int(input("Enter the amount of the loan payment: "))
utilities = int(input("Enter the utility debt: "))

salary_balances = salary - loan - utilities
print(f"The salary balances is equal to {salary_balances}")