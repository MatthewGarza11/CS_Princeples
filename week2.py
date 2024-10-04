# This file was created by: Matthew Garza

import random

favMovies = ["Star Wars", "Lord of the rings", "Transformers: The Movie", "Alien"]

favMovies = random.choice (favMovies)

# we are concation a string with a variable 
# Concation is the process of appending one string to another string 
print("One of my favorite movies is " + favMovies + "!")

# len () is a built-in function in python that returns the length of an object in this case a list
numberOfMovies = len(favMovies)