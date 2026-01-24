#2.3
if grade >= 90:
    print("Congratulations! Your grade of 91 earned you an A in this course\n")
else:
    print("Congratulations, you still tried your best!\n")

#2.4 Arithmetic
left_operand = 27.5
right_operand = 2
print(f"{left_operand} + {right_operand} = {left_operand + right_operand}")
print(f"{left_operand} - {right_operand} = {left_operand - right_operand}")
print(f"{left_operand} * {right_operand} = {left_operand * right_operand}")
print(f"{left_operand} / {right_operand} = {left_operand / right_operand}")
print(f"{left_operand} // {right_operand} = {left_operand // right_operand}")
print(f"{left_operand} ** {right_operand} = {left_operand ** right_operand}")

print("Math Problems")

#2.5 Circle Area, Diameter and Circumference
pi = 3.14159
radius = 2

diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * (radius ** 2)

print(f"Radius: {radius}")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Area: {area}")

print("Circle")

#2.6 Odd or Even
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

print("Odd or Even")

#2.7 Multiples
num1 = 1024
num2 = 2

if num1 % 4 == 0:
    print(f"{num1} is a multiple of 4.")
else:
    print(f"{num1} is not a multiple of 4.")

if num2 % 10 == 0:
    print(f"{num2} is a multiple of 10.")
else:
    print(f"{num2} is not a multiple of 10.")

print("Multiples")

#2.8 Table of Squares and Cubes
print("number\tsquare\tcube")
for n in range(0, 6):
    print(f"{n}\t{n**2}\t{n**3}")
print("Squares and Cubes")    
