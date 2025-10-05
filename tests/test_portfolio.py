import pytest
from src.stock import Stock
from src.portfolio import Portfolio


@pytest.fixture
def sample_portfolio():
    stocks = [
        Stock("AAPL", 10, 150.0),  # value = 1500
        Stock("GOOG", 5, 200.0),   # value = 1000
    ]
    targets = {"AAPL": 0.6, "GOOG": 0.4}
    return Portfolio(stocks, targets)


def test_stock_current_value():
    s = Stock("aapl", 10, 150)
    assert s.symbol == "AAPL"
    assert s.current_value() == 1500.0


def test_portfolio_total_value(sample_portfolio):
    assert sample_portfolio.total_value() == 2500.0


def test_current_values(sample_portfolio):
    values = sample_portfolio.current_values()
    assert values == {"AAPL": 1500.0, "GOOG": 1000.0}


def test_invalid_allocations_sum():
    stocks = [Stock("MSFT", 10, 300)]
    bad_targets = {"MSFT": 0.8}
    with pytest.raises(ValueError):
        Portfolio(stocks, bad_targets)


def test_rebalance_no_change(sample_portfolio):
    plan = sample_portfolio.rebalance()
    assert plan["AAPL"] == pytest.approx(0.0, abs=1e-2)
    assert plan["GOOG"] == pytest.approx(0.0, abs=1e-2)


def test_rebalance_with_imbalance():
    stocks = [
        Stock("AAPL", 10, 100.0),  # 1000
        Stock("GOOG", 10, 200.0),  # 2000
    ]
    targets = {"AAPL": 0.5, "GOOG": 0.5}
    p = Portfolio(stocks, targets)
    plan = p.rebalance()
    # total = 3000; each target = 1500
    assert plan == {"AAPL": 500.0, "GOOG": -500.0}


def test_rebalance_add_new_stock():
    stocks = [Stock("AAPL", 10, 100.0)]  # total 1000
    targets = {"AAPL": 0.5, "GOOG": 0.5}
    p = Portfolio(stocks, targets)
    plan = p.rebalance()
    # total = 1000; each target = 500
    assert plan == {"AAPL": -500.0, "GOOG": 500.0}
