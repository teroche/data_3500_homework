#Programming Activity
#Activity 1
name = input ("Enter your name: ")
fav_color = input ("Enter your favorite color: ")

with open("favorite_color.txt", "w") as file:
    file.write(name + " 's favorite color is " + fav_color + "\n")
               
print("Favorite color saved.")

#Activity 2
import numpy

np1 = numpy.zeros(100)
np1 = numpy.random.rand(100)

print("np1:", np1)