# this file was created by: Matthew Garza
import random

# we define a funstion with a parameter called greeting 
def randomPicker(greeting):
    # creating a lsit that lives only in this function
    global nameList 
    nameList = []
    # getting names from user
    x = input(greeting)
    # add the name to this list
    nameList.append(x)
    y = input(greeting)
    nameList.append(y)
    z = input(greeting)
    nameList.append(z) 
    # choose name from appended list  
    randName = random.choice(nameList)
    # return that name to the function when called 
    return randName
# print(randomPicker("Give me the rizzliest name you can think of"))

randomPicker("type something here...")

print(nameList)

# assign value to variable
x = 1 

# checked to see if this variable hold a value of 1
x !=1 
# This loop uses break to run one time the be done


while x < 5:
    print("infinite loops are dangerous...")
    print("infinite loops are dangerous...")
    print("infinite loops are dangerous...")
    x+=1
    # break 
