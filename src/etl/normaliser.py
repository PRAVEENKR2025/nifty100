def normalize_year(year_str):
    """
    Convert strings like 'FY2020' or '2020' into integer year.
    """
    year_str = str(year_str).strip()
    if year_str.startswith("FY"):
        return int(year_str[2:])
    return int(year_str)

def normalize_ticker(ticker):
    """
    Convert strings like 'RELIANCE.NS' into 'RELIANCE'.
    """
    ticker = str(ticker).strip()
    if "." in ticker:
        return ticker.split(".")[0]
    return ticker
