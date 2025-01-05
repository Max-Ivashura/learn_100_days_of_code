import random


letters = list(map(chr, range(ord("a"), ord("z") + 1))) + list(
    map(chr, range(ord("A"), ord("Z") + 1))
)
numbers = list(map(chr, range(ord("0"), ord("9") + 1)))
symbols = list(map(chr, range(ord("!"), ord("+") + 1)))

print("Welcome to PyPassword")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for nr_symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print("".join(password_list))
