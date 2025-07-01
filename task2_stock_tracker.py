
# Task 2: Stock Portfolio Tracker 📈

# Set stock values
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "INFY": 1500,
    "GOOG": 2800
}

total = 0

print("💰 Simple Stock Calculator")
print("Available stocks:", ", ".join(prices.keys()))

while True:
    code = input("Enter stock symbol (or type 'end'): ").upper()
    if code == 'END':
        break
    if code in prices:
        qty = int(input(f"How many shares of {code}? "))
        total += prices[code] * qty
    else:
        print("Stock not found. Try again.")

print(f"Total investment: ₹{total}")
