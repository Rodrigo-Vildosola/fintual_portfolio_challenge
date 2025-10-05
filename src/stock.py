from typing import Union

class Stock:
    """Represents a stock position."""
    def __init__(self, symbol: str, shares: Union[int, float], price: Union[int, float]) -> None:
        
        self.symbol: str = symbol.upper()
        self.shares: float = float(shares)
        self.price: float = float(price)

    def current_value(self) -> float:
        return self.shares * self.price
