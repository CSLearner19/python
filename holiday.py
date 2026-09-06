print("===========================================")
print("        Welcome to Holiday Builder         ")
print("===========================================")
print()
choice = int(input("Enter 1 for Christmas or 2 for Halloween"))
print()
if choice == 1:
    print("You chose Christmas")
    print("What gifts do you want?")
    choice1 = int(input("Enter 1 for bike or 2 for cake"))
    print()
    if choice1 == 1:
        print("You want a bike as a gift!")
        print("A bike is very useful for transportation")
        print("A bike can also be used for exercise")
    elif choice1 == 2:
        print("You want cake as a gift!")
        print("A cake is very delicious!")
        print("A cake can come in many different varieties")
    else:
        print("Invalid input, Try again")
    print()
    print("Thanks for using the Holiday Builder")
    print()
elif choice == 2:
    print("You chose Halloween!")
    print("What costume do you want?")
    choice2 = int(input("Enter 1 for spiderman or 2 for princess"))
    if choice2 == 1:
        print("You chose Spiderman!")
        print("He is a very famous and strong superhero")
    elif choice2 == 2:
        print("You chose princess")
        print("She is a very nice person")
    else:
        print("Invalid input, try again")
    print()
    print("Thanks for using the Holiday Builder")
    print()
else:
    print("Invalid input, try again")