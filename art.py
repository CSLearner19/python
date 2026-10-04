price_per_item = int(input("Enter price per item in dollars: "))
items_bought = int(input("Enter the amount of items bought: "))
def calculate_total(price, items):
    total = price*items
    return total
total_price = calculate_total(price_per_item, items_bought)
print("")
print("Bill\n")
print("Price Per Item = ", price_per_item)
print("Number of items bought = ", items_bought)
print("Amount total = ", total_price)
