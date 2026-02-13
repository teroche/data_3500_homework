#Activity 1
def welcome_fctn(name):
    print("Welcome", name)
welcome_fctn("Tara")

#Activity 2
def welcome_fctn(name):
    welcome_message = "Welcome " + name
    return welcome_message

print(welcome_fctn("Tara"))

#Activity 3
def welcome_fctn(name, age, favorite_color):
    welcome_message = (
        "Welcome " + name +
        ", you are " + str(age) +
        " years old, and " + favorite_color +
        " is your favorite color"
    )
    return welcome_message

print(welcome_fctn("Tara", 47, "Purplegit"))