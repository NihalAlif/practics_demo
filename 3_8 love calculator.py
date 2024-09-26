print("Wellcome to love calculator")
nam1=input("Whal is your name ?\n")
nam2=input("Whal is their name ?\n")
combined_nam=nam1+nam2
lower_case=combined_nam.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
true=t+r+u+e

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

love=l+o+v+e

love_score=int(str(true)+str(love))
if (love_score<10) or (love_score>90):
    
    print(f"your score is {love_score}. you go together like coke and mentors.")
elif (love_score>=40) and (love_score<=50):
    print(f"your score is {love_score}. you are allright together.")    
else:
    print(f"your score is {love_score}.")    