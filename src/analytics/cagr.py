# src/analytics/cagr.py
import math

def compute_cagr(start_value, end_value, years):
    """
    CAGR formula: ((end/start)^(1/n) - 1) * 100
    Handles 6 edge cases with flags.
    Returns (cagr_value, flag)
    """
    if years <= 0:
        return None, "INVALID_YEARS"
    if start_value is None or end_value is None:
        return None, "MISSING_DATA"
    if start_value == 0:
        return None, "ZERO_BASE"
    if years < 1:
        return None, "INSUFFICIENT"

    # Edge cases: sign combinations
    if start_value > 0 and end_value > 0:
        cagr = ((end_value / start_value) ** (1 / years) - 1) * 100
        return cagr, None
    elif start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"
    elif start_value < 0 and end_value > 0:
        return None, "TURNAROUND"
    elif start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    return None, "UNKNOWN"

def revenue_cagr(values, window):
    if len(values) < window + 1:
        return None, "INSUFFICIENT"
    start = values[-(window+1)]
    end = values[-1]
    return compute_cagr(start, end, window)

def pat_cagr(values, window):
    if len(values) < window + 1:
        return None, "INSUFFICIENT"
    start = values[-(window+1)]
    end = values[-1]
    return compute_cagr(start, end, window)

def eps_cagr(values, window):
    if len(values) < window + 1:
        return None, "INSUFFICIENT"
    start = values[-(window+1)]
    end = values[-1]
    return compute_cagr(start, end, window)
