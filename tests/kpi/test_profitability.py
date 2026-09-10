import pytest
from src.analytics import ratios

def test_net_profit_margin_normal():
    assert ratios.net_profit_margin(100, 500) == 20.0

def test_net_profit_margin_zero_sales():
    assert ratios.net_profit_margin(100, 0) is None

def test_operating_profit_margin_normal():
    assert ratios.operating_profit_margin(200, 1000) == 20.0

def test_operating_profit_margin_mismatch_logs(caplog):
    ratios.operating_profit_margin(200, 1000, opm_percentage=25)
    assert "OPM mismatch" in caplog.text

def test_return_on_equity_normal():
    assert ratios.return_on_equity(100, 200, 300) == pytest.approx(20.0)

def test_return_on_equity_negative_equity():
    assert ratios.return_on_equity(100, -50, -50) is None

def test_return_on_capital_employed_normal():
    assert ratios.return_on_capital_employed(150, 200, 300, 100) == pytest.approx(25.0)

def test_return_on_assets_zero_assets():
    assert ratios.return_on_assets(100, 0) is None
