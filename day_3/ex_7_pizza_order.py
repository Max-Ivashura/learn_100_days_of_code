print("Welcome to Python pizza!")
size = input("What size pizza do you want?\n S, M, or L: ").upper()
add_pipperoni = input("Do you want pepperoni?\n Y or N: ").upper()
extra_cheese = input("do you want extra cheese?\n Y or N: ").upper()

bill = 0

if size == "S":
    bill += 15
    if add_pipperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pipperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pipperoni == "Y":
        bill += 3
else:
    print("Error size!")

if extra_cheese == "Y":
    bill += 1

print("Your final bill:", bill)
