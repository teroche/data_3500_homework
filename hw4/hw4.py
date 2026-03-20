file = open("hw4/TSLA.txt")

lines = file.readlines()

for line in lines:
    price = float(line.strip())
    print(price)

file.close()