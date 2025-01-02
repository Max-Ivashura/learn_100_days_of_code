height = float(input("Enter your Height in m: "))
weight = float(input("Enter your Weight in kg: "))

bmi = weight / (height**2)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight!")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight!")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese!")
else:
    print(f"Your BMI is {bmi}, you are clinically obese!")
