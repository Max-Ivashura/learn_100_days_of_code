import random

names_str = "Angela, Max, Steave, Jack"
names_list = names_str.split(", ")
print(names_list)
print(random.choice(names_list))
