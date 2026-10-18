try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("The result is ", result)
except ZeroDivisionError:
    print("Zero Division Error");
except ValueError:
    print("Value Error")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will always print")
