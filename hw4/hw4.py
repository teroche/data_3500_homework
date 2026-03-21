file = open("hw4/TSLA.txt")

lines = file.readlines()

for line in lines:
    price = float(line.strip())
    print(price)

file.close()
file = open("hw4/TSLA.txt")
# DATA 3500
# HW4 - Stock Market Trading
# Tara Roche

# open file
file = open("hw4/TSLA.txt")

# read all lines
lines = file.readlines()

# close file
file.close()

# create empty list
prices = []

# loop through lines and convert to floats
for line in lines:
    price = float(line.strip())
    price = round(price, 2)
    prices.append(price)

print(prices)
for i in range(5, len(prices)):
    current_price = prices[i]

    avg_price = (
        prices[i-1] +
        prices[i-2] +
        prices[i-3] +
        prices[i-4] +
        prices[i-5]
    ) / 5

    avg_price = round(avg_price, 2)

    print("current price:", current_price)
    print("5 day average:", avg_price)

    for i in range(5, len(prices)):
      current_price = prices[i]

    avg_price = (
        prices[i-1] +
        prices[i-2] +
        prices[i-3] +
        prices[i-4] +
        prices[i-5]
    ) / 5

    avg_price = round(avg_price, 2)

    print("current price:", current_price)
    print("5 day average:", avg_price)

    buy = 0
first_buy = 0
total_profit = 0

for i in range(5, len(prices)):
    current_price = prices[i]

    avg_price = (
        prices[i-1] +
        prices[i-2] +
        prices[i-3] +
        prices[i-4] +
        prices[i-5]
    ) / 5

    avg_price = round(avg_price, 2)

    # BUY condition
    if current_price < avg_price * 0.98:
        buy = current_price

        if first_buy == 0:
            first_buy = buy

        print("buying at:", round(buy, 2))

    # SELL condition
    elif current_price > avg_price * 1.02:
        sell = current_price
        trade_profit = sell - buy
        total_profit += trade_profit

        print("selling at:", round(sell, 2))
        print("trade profit:", round(trade_profit, 2))

    # DO NOTHING
    else:
        pass
    # DATA 3500
# HW4 - Stock Market Trading
# Tara Roche

# open file
file = open("hw4/TSLA.txt")

# read all lines
lines = file.readlines()

# close file
file.close()

# create empty list
prices = []

# loop through lines and convert to floats
for line in lines:
    price = float(line.strip())
    price = round(price, 2)
    prices.append(price)

# initialize variables
buy = 0
first_buy = 0
total_profit = 0

# print heading
print("TSLA Mean Reversion Strategy Output: 2025 - 2026 Data")

# loop through prices and calculate 5 day moving average
for i in range(5, len(prices)):
    current_price = prices[i]

    avg_price = (
        prices[i-1] +
        prices[i-2] +
        prices[i-3] +
        prices[i-4] +
        prices[i-5]
    ) / 5

    avg_price = round(avg_price, 2)

    # buy condition
    if current_price < avg_price * 0.98:
        buy = current_price

        if first_buy == 0:
            first_buy = buy

        print("buying at:      ", round(buy, 2))

    # sell condition
    elif current_price > avg_price * 1.02:
        sell = current_price
        trade_profit = sell - buy
        trade_profit = round(trade_profit, 2)
        total_profit += trade_profit
        total_profit = round(total_profit, 2)

        print("selling at:     ", round(sell, 2))
        print("trade profit:   ", round(trade_profit, 2))

    # do nothing
    else:
        pass

# print final output
print("-----------------------")

final_profit_percentage = (total_profit / first_buy) * 100
final_profit_percentage = round(final_profit_percentage, 2)

print("Total profit:   ", round(total_profit, 2))
print("First buy:      ", round(first_buy, 2))
print("% return:       ", str(final_profit_percentage) + "%")