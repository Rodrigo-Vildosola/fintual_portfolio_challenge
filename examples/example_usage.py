from src.stock import Stock
from src.portfolio import Portfolio

stocks = [
    Stock("AAPL", 10, 150),
    Stock("META", 5, 300),
    Stock("GOOG", 8, 180)
]

targets = {"AAPL": 0.5, "META": 0.3, "GOOG": 0.2}

portfolio = Portfolio(stocks, targets)

print("Total value:", portfolio.total_value())
print("Rebalance plan:")
for symbol, diff in portfolio.rebalance().items():
    action = "BUY" if diff > 0 else "SELL"
    print(f"{symbol}: {action} ${abs(diff):.2f}")
