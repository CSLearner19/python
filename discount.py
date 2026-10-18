print("Shopping Discount Calculator")
valid = True
while valid:
    try:
        total_amount = int(input("Enter the total shopping amount: $"))
    except ValueError:
        print("Invalid input: Please enter a valid number")
while valid:
    try:
        discount_percent = int(input("Enter discount: "))
    except ValueError:
        print("Invalid input: Please enter a valid number")
while valid:
    try:
        num_people = int(input("Enter number of people paying"))
    except ValueError:
        print("Invalid input: Please enter a valid number")
discount_amount = total_amount*(discount_percent/100)
final_bill = total_amount - discount_amount
per_person = final_bill/num_people
print("Discount amount is ", discount_amount)
print("Final Bill is ", final_bill)
print("Number of money per person", per_person)