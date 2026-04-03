import json
# FUNCTION: Mean Reversion Strategy
def meanReversionStrategy(prices):
    position = None
    buy_price = 0
    total_profit = 0
    first_buy = None

    window = 5  # 5-day average

    for i in range(window, len(prices)):
        avg = sum(prices[i-window:i]) / window
        price = prices[i]

        if price < avg * 0.98:
            if position is None:
                print("buying at:", price)
                position = "long"
                buy_price = price
                if first_buy is None:
                    first_buy = price

        elif price > avg * 1.02:
            if position == "long":
                print("selling at:", price)
                profit = round(price - buy_price, 2)
                print("trade profit:", profit)
                total_profit += profit
                position = None

    percent_return = round((total_profit / first_buy) * 100, 2) if first_buy else 0

    print("-----------------------")
    print("Total profit:", round(total_profit, 2))
    print("First buy:", first_buy)
    print("Percent return:", percent_return, "%")

    return round(total_profit, 2), percent_return


# FUNCTION: Simple Moving Average Strategy
def simpleMovingAverageStrategy(prices):
    position = None
    buy_price = 0
    total_profit = 0
    first_buy = None

    window = 5

    for i in range(window, len(prices)):
        avg = sum(prices[i-window:i]) / window
        price = prices[i]

        if price > avg:
            if position is None:
                print("buying at:", price)
                position = "long"
                buy_price = price
                if first_buy is None:
                    first_buy = price

        elif price < avg:
            if position == "long":
                print("selling at:", price)
                profit = round(price - buy_price, 2)
                print("trade profit:", profit)
                total_profit += profit
                position = None

    percent_return = round((total_profit / first_buy) * 100, 2) if first_buy else 0

    print("-----------------------")
    print("Total profit:", round(total_profit, 2))
    print("First buy:", first_buy)
    print("Percent return:", percent_return, "%")

    return round(total_profit, 2), percent_return


# FUNCTION: Save Results
def saveResults(results):
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)


# MAIN PROGRAM

# 10 tickers
tickers = [
    "AAPL", "GOOG", "ADBE",
    "TSLA", "GFL", "POGHF",
    "RSG", "WCN", "WM", "WMS"
]

results = {}

for ticker in tickers:
    print("\n==============================")
    print(ticker, "Simple Moving Average Strategy Output:")

    # load prices
    file = open(f"hw5/{ticker}.txt")
    lines = file.readlines()
    prices = [round(float(line.strip()), 2) for line in lines]

    # store prices
    results[f"{ticker}_prices"] = prices

    # SMA strategy
    sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = sma_returns

    print("\n" + ticker, "Mean Reversion Strategy Output:")

    # Mean Reversion strategy
    mr_profit, mr_returns = meanReversionStrategy(prices)
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = mr_returns


# save results
saveResults(results)