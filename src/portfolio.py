from typing import Dict, List

from src.stock import Stock

class Portfolio:
    def __init__(self, stocks: List[Stock], target_allocations: Dict[str, float]) -> None:
        self.stocks: List[Stock] = stocks

        # We want to normalize the names for symbols, to have all tickers names on upper case
        self.target_allocations: Dict[str, float] = {
            k.upper(): v for k, v in target_allocations.items()
        }
        # It is critical to check wether our target allocations sum exactly 1
        self._validate_allocations()

    def _validate_allocations(self) -> None:
        """Sums the value of each weight to check wether a Portfolio has the required total_weight for allocatiosn"""
        total_weight = sum(self.target_allocations.values())
        if not 0.99 <= total_weight <= 1.01:
            raise ValueError(f"Target allocations must sum to 1. Got {total_weight:.2f}")

    def total_value(self) -> float:
        """Get the total value of the portfolio"""
        return sum(stock.current_value() for stock in self.stocks)
    
    def current_values(self) -> Dict[str, float]:
        return {stock.symbol: stock.current_value() for stock in self.stocks}


    def rebalance(self) -> Dict[str, float]:
        # 1. Compute the total market value of the portfolio
        total = self.total_value()

        # 2. Get current market value per stock
        current = self.current_values()

        # 3. Compute target dollar value for each stock
        #    Example: total = 10_000, weight = 0.4 -> target = 4000
        target_values = {
            symbol: total * weight for symbol, weight in self.target_allocations.items()
        }

        # 4. Add missing symbols with zero current value
        #    (e.g., target stock not yet held in the portfolio)
        for symbol in target_values:
            current.setdefault(symbol, 0.0)

        # 5. Calculate difference between target and current
        #    Positive -> buy; Negative -> sell
        rebalance_plan = {
            symbol: round(target_values[symbol] - current[symbol], 2)
            for symbol in target_values
        }

        # 6. Return dictionary of adjustments in currency units
        return rebalance_plan
