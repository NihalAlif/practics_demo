print("Welcome to the tip and bill split calculator.")

bill=float(input("what was the total bill ?\n"))
tip_per=float(input("What Percentage tip would you like to give?\n"))
total_people=int(input("How many people to split the bill ?\n"))
tip=tip_per/100*bill
total_bill=tip+bill
pay="{:.2f}".format(total_bill/total_people)

print(f"Each person shoud pay {pay} tk")