import json
# Programming Activity 1

# Ask the user for two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# Create the 2D list
twoDList = []

for i in range(num1):
    twoDList.append([])

# Fill the 2D list with multiplication values
for i in range(1, num1 + 1):
    for j in range(1, num2 + 1):
        twoDList[i - 1].append(i * j)

# Print the multiplication table
print("\nMultiplication Table:")
for i in range(num1):
    for j in range(num2):
        print(twoDList[i][j], end="   ")
    print()


# Programming Activity 2
# Ask the user for age and favorite color
person_info = {}
person_info["age"] = int(input("\nWhat is your age? "))
person_info["favorite_color"] = input("What is your favorite color? ")
person_info["multiplication_table"] = twoDList

# Print all dictionary values by iterating through the keys
print("\nDictionary Contents:")
for key in person_info.keys():
    print(key, person_info[key])


# Programming Activity 3
# Load person.json into a dictionary
with open("person.json", "r") as file:
    person = json.load(file)

# Show the age before and after updating
print("\nAge in person.json before update:", person["age"])
person["age"] += 1
print("Age in person.json after update:", person["age"])

# Save the updated dictionary back to person.json
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Verify the updated contents
#ChatGPT helped me fix an error here
with open("Programming_Activities/person.json", "r") as file:
    updated_person = json.load(file)

print("Verified updated age in file:", updated_person["age"])


# Programming Activity 4
# Ask the user for two numbers
num1 = int(input("\nEnter a number: "))
num2 = int(input("Enter another number: "))

# Try dividing the numbers
try:
    answer = num1 / num2
    print("Result:", answer)
except ZeroDivisionError:
    print("Error, attempted to divide by zero")