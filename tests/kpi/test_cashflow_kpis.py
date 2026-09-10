import pytest
from src.analytics import cashflow_kpis as cf

def test_free_cash_flow():
    assert cf.free_cash_flow(100, -50) == 50

def test_cfo_quality_score_high_quality():
    val, label = cf.cfo_quality_score([120,130,140,150,160], [100,100,100,100,100])
    assert label == "High Quality"

def test_capex_intensity_asset_light():
    val, label = cf.capex_intensity(-20, 1000)
    assert label == "Asset Light"

def test_capex_intensity_capital_intensive():
    val, label = cf.capex_intensity(-200, 1000)
    assert label == "Capital Intensive"

def test_fcf_conversion_rate_normal():
    assert cf.fcf_conversion_rate(50, 100) == 50.0

def test_fcf_conversion_rate_zero_op():
    assert cf.fcf_conversion_rate(50, 0) is None

def test_classify_capital_allocation_reinvestor():
    cfo_sign, cfi_sign, cff_sign, label = cf.classify_capital_allocation(100, -50, -30)
    assert label == "Reinvestor"

def test_classify_capital_allocation_distress():
    cfo_sign, cfi_sign, cff_sign, label = cf.classify_capital_allocation(-100, 50, 60)
    assert label == "Distress Signal"
