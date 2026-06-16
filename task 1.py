# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 170
}

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

total_investment = 0
portfolio_details = []

n = int(input("\nEnter the number of stocks you want to buy: "))

for i in range(n):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name} - Quantity: {quantity}, Investment: ${investment}"
        )

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not available!")

print("\n===== PORTFOLIO SUMMARY =====")

for detail in portfolio_details:
    print(detail)

print(f"\nTotal Investment Value: ${total_investment}")

# Optional file saving
choice = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n\n")

        for detail in portfolio_details:
            file.write(detail + "\n")

        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("Portfolio saved successfully in 'portfolio.txt'")

print("\nThank you for using Stock Portfolio Tracker!")