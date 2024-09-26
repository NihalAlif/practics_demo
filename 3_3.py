print("Welcome to the rollercoster")
height=int(input("What is your height in cm ?\n"))

if height>=100:
    age=int(input("what is your age ?\n"))
    
    if age>12:
        print("please pay 7 taka extra.")
    elif age>=18:
        print("wellcome")
    else :
        print("sorry. came when you are 18:)")    
else:
    print("sorry")    