def parking_payment_helper(total_due):
    amount_due = total_due
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert coin (1,5,10,25): "))
        if coin == 5 or coin == 10 or coin == 1 or coin ==25:
            amount_due -= coin
        else:
            continue
        if amount_due<=0:
            break
    change_owed = amount_due
    if change_owed == 0:
        print("No more change owed!")
    else: 
        print(f"Change owed: {change_owed}")
print(parking_payment_helper(40))


