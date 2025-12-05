def addition(first_num, second_num):
    return f'{first_num} + {second_num} = {first_num + second_num}'

def subtraction(first_num, second_num):
    return f'{first_num} - {second_num} = {first_num - second_num}'

def multiplication(first_num, second_num):
    return f'{first_num} * {second_num} = {first_num * second_num}'

def division(first_num, second_num):
    if second_num == 0:
        return "Cannot divide by zero. Enter a value greater than zero"
    return f'{first_num} / {second_num} = {first_num / second_num}'



menu = """Select Operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""
print("Welcome To Ife's Calculator")

while True:
    print(menu)
    choice = input("Enter a number between 1 to 5: ")
    
    if choice not in "12345":
        print("Invalid Choice. Enter any number from 1 to 5")
        break
    if choice == "5":
        print("Exiting the calculator...")
        break

    first_num = float(input("Enter any number of your choice: "))
    second_num = float(input("Enter another number of your choice: "))
    if choice == "1":
        print(addition(first_num, second_num))
    elif choice == "2":
        print(subtraction(first_num, second_num))
    elif choice == "3":
        print(multiplication(first_num, second_num))
    elif choice == "4":
        print(division(first_num, second_num))
    else:
        print("Invalid Choice.")