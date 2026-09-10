from src.etl.normaliser import normalize_year, normalize_ticker

# -------------------------------
# 20 tests for normalize_year
# -------------------------------

def test_year_2020(): assert normalize_year("FY2020") == 2020
def test_year_2019(): assert normalize_year("FY2019") == 2019
def test_year_2021(): assert normalize_year("FY2021") == 2021
def test_year_plain(): assert normalize_year("2022") == 2022
def test_year_1999(): assert normalize_year("FY1999") == 1999
def test_year_2000(): assert normalize_year("FY2000") == 2000
def test_year_2010(): assert normalize_year("2010") == 2010
def test_year_1990(): assert normalize_year("FY1990") == 1990
def test_year_1985(): assert normalize_year("FY1985") == 1985
def test_year_1975(): assert normalize_year("1975") == 1975
def test_year_1960(): assert normalize_year("FY1960") == 1960
def test_year_2050(): assert normalize_year("2050") == 2050
def test_year_2030(): assert normalize_year("FY2030") == 2030
def test_year_2025(): assert normalize_year("2025") == 2025
def test_year_2015(): assert normalize_year("FY2015") == 2015
def test_year_2018(): assert normalize_year("2018") == 2018
def test_year_2005(): assert normalize_year("FY2005") == 2005
def test_year_2008(): assert normalize_year("2008") == 2008
def test_year_1995(): assert normalize_year("FY1995") == 1995
def test_year_1992(): assert normalize_year("1992") == 1992

# -------------------------------
# 15 tests for normalize_ticker
# -------------------------------

def test_ticker_reliance(): assert normalize_ticker("RELIANCE.NS") == "RELIANCE"
def test_ticker_tcs(): assert normalize_ticker("TCS.BSE") == "TCS"
def test_ticker_infy(): assert normalize_ticker("INFY.NS") == "INFY"
def test_ticker_plain(): assert normalize_ticker("HDFC") == "HDFC"
def test_ticker_sbin(): assert normalize_ticker("SBIN.NSE") == "SBIN"
def test_ticker_axis(): assert normalize_ticker("AXISBANK.BSE") == "AXISBANK"
def test_ticker_itc(): assert normalize_ticker("ITC") == "ITC"
def test_ticker_icici(): assert normalize_ticker("ICICI.NS") == "ICICI"
def test_ticker_wipro(): assert normalize_ticker("WIPRO.BSE") == "WIPRO"
def test_ticker_hcl(): assert normalize_ticker("HCLTECH.NS") == "HCLTECH"
def test_ticker_ntpc(): assert normalize_ticker("NTPC.BSE") == "NTPC"
def test_ticker_powergrid(): assert normalize_ticker("POWERGRID.NS") == "POWERGRID"
def test_ticker_ultratech(): assert normalize_ticker("ULTRACEMCO.BSE") == "ULTRACEMCO"
def test_ticker_bajaj(): assert normalize_ticker("BAJAJFIN.NS") == "BAJAJFIN"
def test_ticker_plain2(): assert normalize_ticker("ONGC") == "ONGC"
