import pytest
from src.analytics import cagr

def test_normal_cagr():
    val, flag = cagr.compute_cagr(100, 200, 5)
    assert round(val, 2) == 14.87
    assert flag is None

def test_decline_to_loss():
    val, flag = cagr.compute_cagr(100, -50, 3)
    assert val is None
    assert flag == "DECLINE_TO_LOSS"

def test_turnaround():
    val, flag = cagr.compute_cagr(-100, 200, 5)
    assert val is None
    assert flag == "TURNAROUND"

def test_both_negative():
    val, flag = cagr.compute_cagr(-100, -200, 5)
    assert val is None
    assert flag == "BOTH_NEGATIVE"

def test_zero_base():
    val, flag = cagr.compute_cagr(0, 200, 5)
    assert val is None
    assert flag == "ZERO_BASE"

def test_insufficient_data():
    val, flag = cagr.revenue_cagr([100, 200], 5)
    assert val is None
    assert flag == "INSUFFICIENT"

def test_eps_cagr_normal():
    val, flag = cagr.eps_cagr([10, 12, 15, 20, 25, 30], 5)
    assert flag is None
    assert round(val, 2) > 0
