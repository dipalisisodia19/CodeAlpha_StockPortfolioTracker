# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "MSFT": 300,
    "AMZN": 220
}

print("===== Available Stocks =====")
for stock, price in stocks.items():
    print(stock, "=", price)

portfolio = {}
total_investment = 0

n = int(input("\nHow many stocks do you want to enter? "))

for i in range(n):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock_name in stocks:
        value = stocks[stock_name] * quantity
        portfolio[stock_name] = value
        total_investment += value
    else:
        print("Stock Not Found!")

print("\n===== Portfolio Report =====")

for stock, value in portfolio.items():
    print(stock, ":", value)

print("\nTotal Investment =", total_investment)

if portfolio:
    highest_stock = max(portfolio, key=portfolio.get)
    print("Highest Investment Stock =", highest_stock)

with open("portfolio.txt", "w") as file:
    file.write("===== Portfolio Report =====\n")

    for stock, value in portfolio.items():
        file.write(f"{stock}: {value}\n")

    file.write(f"\nTotal Investment = {total_investment}\n")

    if portfolio:
        file.write(f"Highest Investment Stock = {highest_stock}\n")

print("\nPortfolio saved successfully in portfolio.txt")