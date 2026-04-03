import json
-
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
    if first_buy:
        percent_return = round((total_profit / first_buy) * 100, 2)

    print("-----------------------")
    print(f"Total profit:    {total_profit:.2f}")
    print(f"First buy:       {first_buy:.2f}" if first_buy else "First buy:       None")
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
    if first_buy:
        percent_return = round((total_profit / first_buy) * 100, 2)

    print("-----------------------")
    print(f"Total profit:    {total_profit:.2f}")
    print(f"First buy:       {first_buy:.2f}" if first_buy else "First buy:       None")
    print(f"Percent return:  {percent_return:.2f}%")

    return round(total_profit, 2), percent_return



# FUNCTION: Save Results

def saveResults(results):
    with open("Programming_Activities/hw5/results.json", "w") as file:
        json.dump(results, file, indent=4)



# MAIN PROGRAM


tickers = [
    "AAPL", "CLH", "ADBE",
    "TSLA", "GFL", "POGHF",
    "RSG", "WCN", "WM", "WMS"
]

results = {}

for ticker in tickers:
    print("\n==============================")
    print(ticker.lower(), "Simple Moving Average Strategy Output:")

    # load file (matches your folder + lowercase filenames)
    with open(f"Programming_Activities/hw5/{ticker.lower()}.txt") as file:
        lines = file.readlines()

    # handle BOTH formats (price-only OR date+price)
    prices = [
        round(float(line.strip().split()[-1]), 2)
        for line in lines
        if line.strip()
    ]

    results[f"{ticker}_prices"] = prices

    # SMA strategy
    sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = sma_returns

    print(f"\n{ticker.lower()} Mean Reversion Strategy Output:")

    # Mean Reversion strategy
    mr_profit, mr_returns = meanReversionStrategy(prices)
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = mr_returns


# save results (OUTSIDE loop)
saveResults(results)