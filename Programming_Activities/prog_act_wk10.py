
# Programming Activity Week 10
# Activity 1
# create list of even numbers 2–100 using list comprehension

evens = [i for i in range(2, 101, 2)]

# Activity 2
# remove whitespace from strings using list comprehension

strings = ["   hello  ", "whitespace      ", "   :)  "]

new_list = [string.strip() for string in strings]
print(new_list)

# Activity 3
# get user name, convert to uppercase, print

name = input("Enter your name: ")
name = name.upper()
print("welcome,", name, "!")

# Programming Activity 4
# modify sentence

sentence = "dude, I just biked down that mountain and at first I was like Whoa and then I was like Whoa"

print(sentence)

sentence = sentence.capitalize()

words = sentence.split(" ")

first_whoa = True
i = 0

for word in words:
    if words[i] == "whoa" and first_whoa:
        words[i] = words[i].lower()
        first_whoa = False
    elif words[i] == "whoa" and not first_whoa:
        words[i] = words[i].upper()
    i += 1

new_sentence = ""

for word in words:
    new_sentence += " " + word

new_sentence += "!"

print(new_sentence)

# Challenge: names starting with vowels

names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie"]

vowel_names = [name.upper() for name in names if name[0].lower() in "aeiou"]

count = len(vowel_names)

print(vowel_names)
print(count)
