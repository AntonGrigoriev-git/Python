# Calculating the area of a rhombus

first_diagonal = float(input("Enter the first diagonal of rhombus: "))
second_diagonal = float(input("Enter the second diagonal of rhombus: "))

if first_diagonal == second_diagonal:
    print("It's not a rhombus")
else:
    area_of_rhombus = 0.5 * first_diagonal * second_diagonal
    print(f"The area of a rhombus equal to {area_of_rhombus}")