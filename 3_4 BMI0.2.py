height=float(input("enter your height in m: "))
weight=int(input("enter your weight in kg: "))

bmi=round(weight/height**2)

if bmi<18.5:
    print(f"BMI {bmi}. underweight")
elif bmi <25:
    print(f"BMI {bmi}. normal weight")
elif bmi <30:
    print(f"BMI {bmi}. over weight")
elif bmi <35:
    print(f"BMI {bmi}. obese")
else:
    print(f"BMI {bmi}. clinically obese")            

