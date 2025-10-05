import pytest
from src.stock import Stock
from src.portfolio import Portfolio


def make_portfolio():
    """Helper for tests."""
    s1 = Stock("AAPL", 10, 150)   # 1500
    s2 = Stock("META", 5, 300)    # 1500
    return Portfolio([s1, s2], {"AAPL": 0.6, "META": 0.4})


def test_total_value():
    p = make_portfolio()
    assert p.total_value() == pytest.approx(3000.0)


def test_current_values():
    p = make_portfolio()
    values = p.current_values()
    assert values == {"AAPL": 1500.0, "META": 1500.0}


def test_validate_allocations_sum_error():
    s1 = Stock("AAPL", 1, 100)
    with pytest.raises(ValueError):
        Portfolio([s1], {"AAPL": 0.5})  # Invalid sum


def test_rebalance_basic():
    p = make_portfolio()
    plan = p.rebalance()
    assert isinstance(plan, dict)
    # Expect META to be sold and AAPL to be bought
    assert plan["AAPL"] > 0
    assert plan["META"] < 0
    # Sum of changes should be close to 0
    assert sum(plan.values()) == pytest.approx(0.0, abs=1e-2)


def test_rebalance_handles_missing_stock():
    s1 = Stock("AAPL", 10, 1000)
    p = Portfolio([s1], {"AAPL": 0.5, "META": 0.5})
    plan = p.rebalance()
    # META should appear even if not in portfolio
    assert "META" in plan
    assert isinstance(plan["META"], float)


def test_symbols_case_insensitive():
    s1 = Stock("aapl", 10, 100)
    s2 = Stock("Meta", 10, 100)
    p = Portfolio([s1, s2], {"AAPL": 0.5, "META": 0.5})
    result = p.rebalance()
    assert set(result.keys()) == {"AAPL", "META"}
