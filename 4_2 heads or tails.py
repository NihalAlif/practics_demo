
choise=input("Enter Head for 'H' or Tail For 'T'\n").lower()
import random

ran_int=random.randint(1,2)

if ran_int==1:
    print("its HEADS.")
    if choise=="h":
        print("you winn")
    else:
        print("you lose.best of luck for next time")    

elif ran_int==2:
    print("its TAILS")    
    if choise=="t":
        print("you winn")
    else:
        print("you lose . best of luck for next time ")
else:
    print("Enter only H OR T ")         