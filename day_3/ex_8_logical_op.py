print("Wellcome to the rollercoaster!")
height = int(input("What is your height in cm: "))

if height > 120:
    print("You can ride!")
    age = int(input("How old are you: "))
    if age <= 12:
        print("Price: 5$")
    elif age <= 18:
        print("Price: 7$")
    elif age >= 45 and age <= 55:
        print("Price: 0$")
    else:
        print("Price: 12$")
else:
    print("Sorry, you have to grow taller before you can ride!")
