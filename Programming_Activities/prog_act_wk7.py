import random
# Activity 1
colors = ["Purple", "Teal", "Black"]

for color in colors:
    print("color:", color)

# Activity 2
for color in colors:
    print("color:", color)
    for letter in color:
        print("letter:", letter)
        
# Activity 3
print()

lst = []

for i in range(10):
    lst.append(random.randint(1, 100))
    
print("lst:", lst)

# Activity 4
print()

i = 0

for num in lst:
    if i > 0:
        print(lst[i])
        print(lst[i-1])
    
        if lst[i] % 2 == 0 and lst[i-1] % 2 == 0: # check both indexes
            print("both", lst[i], "and", lst[i-1], "are even")
    
        print("--------")
    i += 1

# Activity 5
# create file variable to pull data into cloud9
file = open("Programming_Activities/AAPL.2023.txt")

# convert file object into list of lines
lines = file.readlines()

# convert lines into rounded floats and put them in a new list
prices = []
for line in lines:
    line = line.strip()
    if line:
        prices.append(float(line))

# caclulate average
total_avg = sum(prices) / len(prices)
print("total_avg:", total_avg)

five_day_avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
print("five_day_avg:", five_day_avg)

# Activity 5.2
# average if the last four days 
last_four_avg = sum(prices[-4:])/4
print("last_four_avg:", last_four_avg)

print()

# set up iterator values and trading variables
i = 0
buy = 0
total_profit = 0

# loop through prices
for price in prices:
    if i >= 4: # only begin 4 day average once there are 4 days to backtrack to
        avg = (prices[i] + prices[i - 1] + prices[i - 2] + prices[i - 3]) / 4
        if price < avg and buy == 0: # buy conditions
            buy = price
            print("Buying at:", "\t", price)
        elif price > avg and buy != 0: # sell conditions
            trade_profit = price - buy
            print("Selling at:", "\t", price)
            print("Trade profit:", "\t", trade_profit)
            total_profit += trade_profit
            buy = 0
            
    i += 1
   
print("total_profit:", "\t", total_profit)