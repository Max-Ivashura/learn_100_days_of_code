student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0

for height in student_heights:
    total_height += height

number_of_students = len(student_heights)
avg = round(total_height / number_of_students)
print(avg)
