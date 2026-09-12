string = input("Please enter your own string")
string2 = ('')
for i in string:
    string2 = i + string2
print("The original string", string)
print("The reverse string", string2)
