students_score = [78, 65, 89, 86, 55, 91, 64, 89]
high = 0

for score in students_score:
    if score > high:
        high = score

print("best value:", high)
