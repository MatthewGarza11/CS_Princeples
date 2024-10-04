# This file was made by Matthew Garza

M = 1

while M < 11:
    print("Bueller")
    M += 1  
    break 

anyoneList = ["anyone"]

for x in anyoneList: 
    print(x)
    print(x)
    print(x)
    print(x)
    print(x)
    break


def myfunc(message):
    name = input("give me name")
    print(message + name)

askingforname = True

names = 0


while askingforname:
    myfunc("hello there...")
    names += 1
    if names > 5:
            askingforname = False