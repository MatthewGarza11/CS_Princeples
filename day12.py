# This file was created by Matthew Garza


# Algorithms: A set of instructions to solve a problem step by step.
# N = N+1 same thing as N +=1
#
#
#
#



N = 0

room = ["Bill", "Ted", "Socrates", "Sam", "Frodo"]


# A for loop goes for a set number of times based on some parameter
# i holds the values in the list "room"
# pair = 0


# for i in room:
#     pair (i)
#     if pair == 2 
#         N +=2
#         #print (We have a pair!
#         print(pair)
#         pair = 0 
#         if N % 2 == 1
#             N += 1

#     print (N)

level1 = [".....",
          ".WW..",
          ".....",
          "..P..",
          "WWWWW",]

print(level1)
print(level1[0])
print(level1[0][0])




# print(list(enumerate(level1)))
# nested for loop

for row in level1:
    print(row)
    for col in row:
        print(col)