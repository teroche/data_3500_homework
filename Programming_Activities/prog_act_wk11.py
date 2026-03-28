# Programming Activity 1
# create list and use join

message = "My favorite colors are: "
fav_colors = ["blue", "white", "red"]

message += ", ".join(fav_colors)

print(message)

# Programming Activity 2
# validate address using isalnum()

address = input("Enter your address: ")

address = address.strip()

# remove common non-alphanumeric characters
address = address.replace(" ", "")
address = address.replace(".", "")
address = address.replace(",", "")

print("address:", address, address.isalnum())

# Challenge 1
# palindrome check (ignore spaces)

sentence = input("Enter a sentence: ")

clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Challenge 2
# remove leading/trailing spaces but keep word order

sentence2 = input("Enter another sentence: ")

clean_sentence = sentence2.strip()

print(clean_sentence)

# Challenge 3
# compare strings function

def compare_strings(string1, string2):

    if string1.lower() == string2.lower():
        return "Equal"

    elif len(string1) != len(string2):
        return "Different Lengths"

    else:
        return "Different Content"


# test function
print(compare_strings("Hello", "hello"))
print(compare_strings("Hello", "Hi"))
print(compare_strings("Hello", "World"))