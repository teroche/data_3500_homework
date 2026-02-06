#Homework 3
#Problem 3.4
#Print 2 rows of 7 zeroes
for row in range(2):
    for col in range(7):
        print("0", end="")
    print()

#Problem 3.9
#Separate digits
num = int(input("Enter a number 7 to 10 digits: "))

divisor = 10 ** (len(str(num)) - 1)

while divisor > 0:
    digit = num // divisor
    print(digit)
    num = num % divisor
    divisor //= 10

# Problem 3.11
# Miles per gallon
total_miles = 0
total_gallons = 0

gallons = float(input("Enter the gallons used (-1 to end): "))

while gallons != -1:
    miles = float(input("Enter the miles driven: "))
    mpg = miles / gallons
    print("The miles/gallon for this tank was", mpg)

    total_miles += miles
    total_gallons += gallons

    gallons = float(input("Enter the gallons used (-1 to end): "))

if total_gallons > 0:
    print("The overall average miles/gallon was", total_miles / total_gallons)

#3.12
#Palindrome
is_palindrome = input("Please enter a 3 digit number")
num = int(is_palindrome)
first_digit = num // 100
third_digit = num % 10
if first_digit == third_digit:
    print("Palindrome!")
else:
    print("Not Palindrome!")

#3.14
#Approximating pi
pi = 0
sign = 1
count_314 = 0
for i in range(1, 3000, 2):
    pi += sign * (4 / i)
    sign *= -1

    approx = round(pi, 3)

    if round(pi, 2) == 3.14:
        count_314 += 1
        if count_314 == 2:
            print("3.14 appears twice at iteration", i)
    else:
        count_314 = 0

    if approx == 3.141:
        count_3141 += 1
        if count_3141 == 2:
            print("3.141 appears twice at iteration", i)
    else:
        count_3141 = 0