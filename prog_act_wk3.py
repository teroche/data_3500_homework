# Activity 1
# variables
apple_price = 1.25
number_purchased = 3
tax = 1.07
total_bill = apple_price * number_purchased * tax
print("You bought", number_purchased, "apples for", apple_price, "per apple. Your total bill was", total_bill, "\n")

# Activity 2
# user input
age = int(input("Enter your age: "))
live_to = int(input("What age would you like to live to: "))

# calculate years left to live
print("You have", live_to - age, "years left to live.\n")

# Activity 3
# user input
grade = float(input("Enter your grade as a percentage: "))

# check if they got an A
if grade >= 93:
    print("Congratulations you got an A\n")
else:
    print("Congratulations, you still learned a ton!!!!\n")
