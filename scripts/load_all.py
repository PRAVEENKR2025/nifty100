import sys, os
import sqlite3

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.etl.loader import (
    insert_companies,
    insert_sectors,
    insert_profitandloss,
    insert_balancesheet,
    insert_cashflow,
    insert_analysis,
    insert_documents,
    insert_prosandcons,
    insert_stock_prices,
    insert_financial_ratios,
    insert_peer_groups
)

def main():
    print("🚀 Starting data load into nifty100.db")

    # Call each loader function with its Excel file
    insert_sectors("data_raw/sectors.xlsx")              # ← make sure this is called
    insert_companies("data_raw/companies.xlsx")
    insert_profitandloss("data_raw/profitandloss.xlsx")
    insert_balancesheet("data_raw/balancesheet.xlsx")
    insert_cashflow("data_raw/cashflow.xlsx")
    insert_analysis("data_raw/analysis.xlsx")
    insert_documents("data_raw/documents.xlsx")
    insert_prosandcons("data_raw/prosandcons.xlsx")
    insert_stock_prices("data_raw/stock_prices.xlsx")
    insert_financial_ratios("data_raw/financial_ratios.xlsx")
    insert_peer_groups("data_raw/peer_groups.xlsx")

    print("✅ All data loaded successfully into nifty100.db")

if __name__ == "__main__":
    main()
