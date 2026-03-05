#Programming Activity
#Activity 1
name = input ("Enter your name: ")
fav_color = input ("Enter your favorite color: ")

with open("favorite_color.txt", "w") as file:
    file.write(name + " 's favorite color is " + fav_color + "\n")
               
print("Favorite color saved.")

#Activity 2
import numpy as np

# initialize numpy array of 100 zeros
np1 = np.zeros(100)

# change array to random numbers
np1 = np.random.rand(100)

print("Random numpy array:")
print(np1)
