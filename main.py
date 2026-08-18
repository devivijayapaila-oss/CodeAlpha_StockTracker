import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "AMZN": 175.00,
    "MSFT": 400.00
}

def calculate_portfolio():
    portfolio = {}
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:", STOCK_PRICES)
    print("Type 'done' when finished adding stocks.\n")

    while True:
        symbol = input("Enter stock symbol (e.g., AAPL): ").upper().strip()
        if symbol == "DONE":
            break
        
        if symbol not in STOCK_PRICES:
            print(f"Stock '{symbol}' not found in database. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Please enter a valid integer for quantity.")

    # Calculate Total Value
    total_value = 0.0
    print("\n--- Portfolio Summary ---")
    summary_rows = []

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = price * qty
        total_value += subtotal
        summary_rows.append([symbol, qty, f"${price:.2f}", f"${subtotal:.2f}"])
        print(f"{symbol}: {qty} shares @ ${price:.2f} each = ${subtotal:.2f}")

    print(f"\n💰 Total Investment Value: ${total_value:.2f}")

    # Save to CSV
    if summary_rows:
        with open("portfolio_summary.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock Symbol", "Quantity", "Price Per Share", "Total Value"])
            writer.writerows(summary_rows)
            writer.writerow(["", "", "Total Portfolio", f"${total_value:.2f}"])
        print("📁 Summary successfully saved to 'portfolio_summary.csv'")

if __name__ == "__main__":
    calculate_portfolio()