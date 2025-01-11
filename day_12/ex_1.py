enemies = "Skeleton"

def increase_enemies():
    global enemies
    enemies = "Zombie"
    print(f"Enemies inside func: {enemies}")

def up_enemies():
    return enemies + "_up"

increase_enemies()
print(f"Enemies outsize func: {enemies}")
enemies = up_enemies()
print(f"Enemies outsize + up func: {enemies}")






















