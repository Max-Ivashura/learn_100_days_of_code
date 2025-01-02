print("Welcome to the Love Calculator!")

name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

combine = (name_1 + name_2).lower()

t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")
true = t + r + u + e

l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"You love score is {love_score}, you go together like coke and mentos!")
elif love_score >= 40 and love_score <= 50:
    print(f"You score is {love_score}, you are alright together!")
else:
    print(f"Your score is {love_score}")
