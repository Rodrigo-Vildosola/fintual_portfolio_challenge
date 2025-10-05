
# Fintual Portfolio Challenge

Implementation of a minimal portfolio rebalancing system as part of the Fintual technical challenge.


## Problem Description
The goal is to implement two main classes:
- `Stock`: represents a stock with symbol, shares, and price.
- `Portfolio`: holds multiple `Stock` objects, has target allocations, and provides a `rebalance()` method that returns how much to buy or sell of each stock to meet target weights.


## Project Structure
```
fintual_portfolio_challenge/
├── pyproject.toml
├── src/
│   ├── stock.py
│   └── portfolio.py
├── tests/
│   └── test_portfolio.py
└── README.md
````

## Setup
1. Clone this repository:
```bash
git clone https://github.com/Rodrigo-Vildosola/fintual_portfolio_challenge.git
cd fintual_portfolio_challenge
```


2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -e .
```

## Run Tests

To verify the solution:

```bash
pytest
```


## Example Usage

```python
from src.stock import Stock
from src.portfolio import Portfolio

s1 = Stock("AAPL", 10, 150)
s2 = Stock("META", 5, 300)
portfolio = Portfolio([s1, s2], {"AAPL": 0.6, "META": 0.4})
print(portfolio.rebalance())
```

## How the Rebalance Algorithm Works

1. **Compute total portfolio value**
   Sum of all `Stock.current_value()` results.

2. **Determine target values**
   Multiply the total value by each stock’s target allocation weight.
   Example: if total = $10 000 and `AAPL` target = 0.4 → target value = $4000.

3. **Compare with current values**
   For every stock in `target_allocations`, compute

   ```
   difference = target_value - current_value
   ```

   * Positive => need to buy.
   * Negative => need to sell.

4. **Return rebalance plan**
   The method returns a dictionary `{symbol: amount}` in currency units.


## Disclaimer

The tests from this project were created by assistance with AI tools.
