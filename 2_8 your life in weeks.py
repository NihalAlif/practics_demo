name=input("enter your name: \n")
age=input("enter your age: \n")
left_year=65-int(age)
day=left_year*365
weeks=left_year*52
month=left_year*12
print(f"{name} you have {day} days or {weeks} weeks or {month} months")