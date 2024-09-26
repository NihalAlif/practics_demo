height=input("enter your height in foot: ")
weight=input("enter your weight in kg: ")
height_meter=float(height)/3.28084   # 1 meter= 3.28084foot
bmi=int(weight)/height_meter ** 2

print("Your BMI is" ,bmi)