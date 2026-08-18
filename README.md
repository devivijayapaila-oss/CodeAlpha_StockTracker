# Stock Portfolio Tracker

A command-line Python script that lets you build a simple stock portfolio using a hardcoded list of stock prices, calculates the total investment value, and saves a summary to a CSV file.

## Features

- Console-based portfolio builder
- Hardcoded dictionary of available stocks and prices:
  - AAPL: $180.00
  - TSLA: $250.00
  - GOOGL: $140.00
  - AMZN: $175.00
  - MSFT: $400.00
- Prompts the user to enter stock symbols and quantities, adding to the portfolio (quantities for the same symbol are summed)
- Validates stock symbols against the hardcoded list
- Validates quantity input (must be a valid non-negative integer)
- Type `done` to finish entering stocks
- Prints a portfolio summary with shares, price per share, and subtotal for each stock
- Calculates and prints the total investment value
- Saves the summary (including total) to `portfolio_summary.csv`

## Requirements

- Python 3
- No external dependencies (uses only the built-in `csv` module)

## Usage

Run the script with:

```
python main.py
```

Follow the prompts:
1. Enter a stock symbol (e.g., `AAPL`) from the available list.
2. Enter the quantity of shares for that symbol.
3. Repeat for as many stocks as you like.
4. Type `done` when finished.

The script will print a summary of your portfolio and total investment value, then save the results to `portfolio_summary.csv` in the same directory.

## How It Works

- `STOCK_PRICES` is a hardcoded dictionary mapping stock symbols to prices.
- `calculate_portfolio()` runs a loop that collects stock symbols and quantities from user input until `done` is entered.
- Invalid symbols (not in `STOCK_PRICES`) or invalid quantities (non-integer or negative) prompt the user to try again.
- After input ends, the script calculates the subtotal for each stock and the total portfolio value.
- If any stocks were entered, the summary is written to `portfolio_summary.csv` using Python's `csv` module, with a final row showing the total portfolio value.

## Output

- Console output showing the portfolio summary and total value.
- A `portfolio_summary.csv` file containing columns: `Stock Symbol`, `Quantity`, `Price Per Share`, `Total Value`, plus a final total row.

## File Structure

- `main.py` — contains all logic for the portfolio tracker in a single file.
