# src/analytics/ratios.py
import logging

# Configure logging for cross-checks and anomalies
logging.basicConfig(filename="output/ratio_engine.log", level=logging.INFO)

def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return (net_profit / sales) * 100

def operating_profit_margin(operating_profit, sales, opm_percentage=None):
    if sales == 0:
        return None
    opm_calc = (operating_profit / sales) * 100
    if opm_percentage is not None and abs(opm_calc - opm_percentage) > 1:
        logging.warning(f"OPM mismatch: calc={opm_calc:.2f}, source={opm_percentage:.2f}")
    return opm_calc

def return_on_equity(net_profit, equity_capital, reserves):
    equity_total = equity_capital + reserves
    if equity_total <= 0:
        return None
    return (net_profit / equity_total) * 100

def return_on_capital_employed(ebit, equity_capital, reserves, borrowings, sector=None):
    capital_employed = equity_capital + reserves + borrowings
    if capital_employed <= 0:
        return None
    roce = (ebit / capital_employed) * 100
    # Sector-relative benchmark for Financials
    if sector == "Financials":
        logging.info(f"ROCE benchmark applied for Financials sector: {roce:.2f}")
    return roce

def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return (net_profit / total_assets) * 100

def debt_to_equity(borrowings, equity_capital, reserves, sector=None):
    equity_total = equity_capital + reserves
    if equity_total <= 0:
        return None
    if borrowings == 0:
        return 0
    de_ratio = borrowings / equity_total
    # High leverage flag
    high_leverage_flag = False
    if de_ratio > 5 and sector != "Financials":
        high_leverage_flag = True
    return de_ratio, high_leverage_flag

def interest_coverage(operating_profit, other_income, interest):
    if interest == 0:
        return None, "Debt Free"
    icr = (operating_profit + other_income) / interest
    icr_flag = False
    if icr < 1.5:
        icr_flag = True
    return icr, icr_flag

def net_debt(borrowings, investments):
    return borrowings - investments

def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return sales / total_assets

def debt_to_equity(borrowings, equity_capital, reserves, sector=None):
    equity_total = equity_capital + reserves
    if equity_total <= 0:
        return None, False   # return tuple for consistency
    if borrowings == 0:
        return 0, False      # return (0, False) instead of just 0
    de_ratio = borrowings / equity_total
    high_leverage_flag = False
    if de_ratio > 5 and sector != "Financials":
        high_leverage_flag = True
    return de_ratio, high_leverage_flag
