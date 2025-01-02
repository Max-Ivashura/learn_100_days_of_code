price = 0
print("Wellcome to the rollercoaster!")
height = int(input("What is your height in cm: "))

if height > 120:
    print("You can ride!")
    age = int(input("How old are you: "))
    if age <= 12:
        price += 5
        print("Price: 5$")
    elif age <= 18:
        price += 7
        print("Price: 7$")
    else:
        price += 12
        print("Price: 12$")
    wants_photo = input("Do you want a photo taken? Cost: 3$ Y or N.\n")
    if wants_photo == "Y":
        price += 3
    print("Total price:", price, "$")
else:
    print("Sorry, you have to grow taller before you can ride!")
