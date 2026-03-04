#Programming Activity
#Activity 1
name = input ("Enter your name: ")
fav_color = input ("Enter your favorite color: ")

with open("favorite_color.txt", "w") as file:
    file.write(name + " 's favorite color is " + fav_color + "\n")
               
print("Favorite color saved.")