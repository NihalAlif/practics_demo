print("Welcome to the rollercoster")
height=int(input("What is your height in cm ?\n"))
bill=0
if height>=120:
     print("you can ride the rolarcoster! ")
     age=int(input("what is your age??\n"))
     if age<12:
          bill=5
          print("child ticket are 5 ")
     elif age<18:
          bill=7
          print("youth ticket are 7")
     elif age>=45 and age <=55:
          print("free")
     else:
          bill=12
          print("adult ticket are 12")
     photos=input("do you want photos ? N or Y\n")
     if photos=="Y":
          bill+=3
     print(f"your total bill {bill}")
                                 
else:
    print("sorry")    