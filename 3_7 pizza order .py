print("Wellcome to python pizza deliveries")
size=input("What size pizza do you want? S, M, OR L\n")
add_pepperoni=input("do you want pepperoni?? N, OR Y\n")
cheese=input("do you want cheese ?? N, OR Y\n")
bill=0
if size=="S":
    bill=150
    if add_pepperoni=="Y":
        bill+=20
elif size=="M":
    bill=200
    if add_pepperoni=="Y":
        bill+=30
else :
    bill=250
    if add_pepperoni=="Y":
        bill+=30
if cheese=="Y":
    bill+=10
print(f"your total bill {bill}")
