import json

# FUNCTION: Mean Reversion Strategy
def meanReversionStrategy(prices):
    position = None
    buy_price = 0
    total_profit = 0
    first_buy = None

    window = 5

    for i in range(window, len(prices)):
        avg = sum(prices[i - window:i]) / window
        price = prices[i]

        if price < avg * 0.98:
            if position is None:
                print(f"buying at:       {price:.2f}")
                position = "long"
                buy_price = price
                if first_buy is None:
                    first_buy = price

        elif price > avg * 1.02:
            if position == "long":
                print(f"selling at:      {price:.2f}")
                profit = round(price - buy_price, 2)
                print(f"trade profit:    {profit:.2f}")
                total_profit += profit
                position = None

    percent_return = 0
    if first_buy is not None:
        percent_return = round((total_profit / first_buy) * 100, 2)

    print("-----------------------")
    print(f"Total profit:    {total_profit:.2f}")
    if first_buy is not None:
        print(f"First buy:       {first_buy:.2f}")
    else:
        print("First buy:       None")
    print(f"Percent return:  {percent_return:.2f}%")

    return round(total_profit, 2), percent_return


# FUNCTION: Simple Moving Average Strategy
def simpleMovingAverageStrategy(prices):
    position = None
    buy_price = 0
    total_profit = 0
    first_buy = None

    window = 5

    for i in range(window, len(prices)):
        avg = sum(prices[i - window:i]) / window
        price = prices[i]

        if price > avg:
            if position is None:
                print(f"buying at:       {price:.2f}")
                position = "long"
                buy_price = price
                if first_buy is None:
                    first_buy = price

        elif price < avg:
            if position == "long":
                print(f"selling at:      {price:.2f}")
                profit = round(price - buy_price, 2)
                print(f"trade profit:    {profit:.2f}")
                total_profit += profit
                position = None

    percent_return = 0
    if first_buy is not None:
        percent_return = round((total_profit / first_buy) * 100, 2)

    print("-----------------------")
    print(f"Total profit:    {total_profit:.2f}")
    if first_buy is not None:
        print(f"First buy:       {first_buy:.2f}")
    else:
        print("First buy:       None")
    print(f"Percent return:  {percent_return:.2f}%")

    return round(total_profit, 2), percent_return


# FUNCTION: Save Results
def saveResults(results):
    with open("/workspaces/data_3500_homework/Programming_Activities/hw5/results.json", "w") as file:
        json.dump(results, file, indent=4)


# MAIN PROGRAM
tickers = [
    "AAPL", "GOOG", "ADBE",
    "TSLA", "GFL", "POGHF",
    "RSG", "WCN", "WM", "WMS"
]

results = {}

for ticker in tickers:
    print("\n==============================")
    print(f"{ticker.lower()} Simple Moving Average Strategy Output:")

    with open(f"/workspaces/data_3500_homework/Programming_Activities/hw5/{ticker.lower()}.txt", "r") as file:
        lines = file.readlines()

    prices = [round(float(line.strip().split()[-1]), 2) for line in lines if line.strip()]

    print("Loaded prices:", len(prices))
    print("First 5 prices:", prices[:5])

    results[f"{ticker}_prices"] = prices

    sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = sma_returns

    print(f"\n{ticker.lower()} Mean Reversion Strategy Output:")

    mr_profit, mr_returns = meanReversionStrategy(prices)
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = mr_returns

saveResults(results)
print("\nresults.json saved.")