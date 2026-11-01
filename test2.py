def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("=== Function Calculator ===")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. None")
while True:
    operation = int(input("\nEnter your choice (1-5)\n"))
    if operation == 5:
        print("Exiting Calculator...Goodbye")
        break
    try:
        num1 = int(input("Enter the number"))
        num2 = int(input("Enter the number"))
        if operation == 1:
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == 2:
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == 3:
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == 4:
            try:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("Error: Zero Division Error!")
        else:
            print("Please Enter a number from 1-5")
    except ValueError:
        print("Error: Invalid Input! Please enter a correct value.")