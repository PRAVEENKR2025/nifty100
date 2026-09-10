import pytest
from src.analytics import ratios

def test_debt_to_equity_normal():
    de, flag = ratios.debt_to_equity(500, 100, 100)
    assert de == 2.5
    assert flag is False

def test_debt_to_equity_debt_free():
    de, flag = ratios.debt_to_equity(0, 200, 300)
    assert de == 0
    assert flag is False

def test_debt_to_equity_high_leverage_flag():
    de, flag = ratios.debt_to_equity(2000, 100, 100)
    assert flag is True

def test_interest_coverage_normal():
    icr, flag = ratios.interest_coverage(300, 50, 100)
    assert icr == 3.5
    assert flag is False

def test_interest_coverage_debt_free():
    icr, label = ratios.interest_coverage(300, 50, 0)
    assert icr is None
    assert label == "Debt Free"

def test_interest_coverage_warning_flag():
    icr, flag = ratios.interest_coverage(100, 0, 100)
    assert icr == 1.0
    assert flag is True

def test_net_debt():
    assert ratios.net_debt(500, 200) == 300

def test_asset_turnover_normal():
    assert ratios.asset_turnover(1000, 500) == 2.0

def test_asset_turnover_zero_assets():
    assert ratios.asset_turnover(1000, 0) is None
