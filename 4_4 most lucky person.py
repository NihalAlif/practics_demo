import random 
name=input("Give me everybody's name, seperated by a comma.\n")
names=name.split(",")

x=len(names)

y=random.randint(0,x-1)

luccky=names[y]
print(f"{luccky} ")
    	