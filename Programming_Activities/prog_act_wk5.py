#Programming Activity 1
is_palindrome = input("Please enter a 3 digit number")
num = int(is_palindrome)
first_digit = num // 100
third_digit = num % 10
if first_digit == third_digit:
    print("Palindrome!")
else:
    print("Not Palindrome!")

#Programming Activity 2
denominator = 2
total = 0.0

for i in range(1, 1001):
    total += 1 / denominator
    denominator *= 2
    print("total:", total)

#Programming Activity 3
#Boolean
age = int(input("Enter your child's age: "))
weight = float(input("Enter your child's weight: "))

criteria_1 = age >= 12
criteria_2 = (age == 11) and (weight > 90)
criteria_3 = (age < 11) and (weight > 100)

if criteria_1 or criteria_2 or criteria_3:
    print("Your child can sit in the front seat")
else:
    print("Your child cannot sit in the front seat")
