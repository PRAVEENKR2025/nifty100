import os
import sys
import sqlite3

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.apply_schema import *   # optional if you want schema step
from scripts.load_all import main as load_all

DB_PATH = r"C:\BLUESTOCK PROJECTS\nifty100\db\nifty100.db"

def run_validations(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\n🔍 Running validations...\n")

    checks = [
    ("Companies table not empty", "SELECT COUNT(*) FROM companies;", lambda x: int(x) > 0),
    ("Sectors table not empty", "SELECT COUNT(*) FROM sectors;", lambda x: int(x) > 0),
    ("Profit & Loss has valid years", "SELECT MIN(year), MAX(year) FROM profitandloss;", lambda x: int(x[0]) >= 2000 and int(x[1]) <= 2026),
    ("Balance Sheet has no NULL assets", "SELECT COUNT(*) FROM balancesheet WHERE assets IS NULL;", lambda x: int(x) == 0),
    ("Cashflow has no NULL operating_cash", "SELECT COUNT(*) FROM cashflow WHERE operating_cash IS NULL;", lambda x: int(x) == 0),
    ("Analysis EPS positive", "SELECT COUNT(*) FROM analysis WHERE eps <= 0;", lambda x: int(x) == 0),
    ("Documents URLs present", "SELECT COUNT(*) FROM documents WHERE url IS NULL;", lambda x: int(x) == 0),
    ("Prosandcons has entries", "SELECT COUNT(*) FROM prosandcons;", lambda x: int(x) > 0),
    ("Stock Prices valid dates", "SELECT COUNT(*) FROM stock_prices WHERE date IS NULL;", lambda x: int(x) == 0),
    ("Financial Ratios ROE not NULL", "SELECT COUNT(*) FROM financial_ratios WHERE roe IS NULL;", lambda x: int(x) == 0),
    ("Peer Groups linked", "SELECT COUNT(*) FROM peer_groups;", lambda x: int(x) > 0),
    ("Companies linked to sectors", "SELECT COUNT(*) FROM companies WHERE sector_id NOT IN (SELECT sector_id FROM sectors);", lambda x: int(x) == 0),
    ("Profitandloss linked to companies", "SELECT COUNT(*) FROM profitandloss WHERE company_id NOT IN (SELECT company_id FROM companies);", lambda x: int(x) == 0),
    ("Balancesheet linked to companies", "SELECT COUNT(*) FROM balancesheet WHERE company_id NOT IN (SELECT company_id FROM companies);", lambda x: int(x) == 0),
    ("Cashflow linked to companies", "SELECT COUNT(*) FROM cashflow WHERE company_id NOT IN (SELECT company_id FROM companies);", lambda x: int(x) == 0),
    ("Analysis linked to companies", "SELECT COUNT(*) FROM analysis WHERE company_id NOT IN (SELECT company_id FROM companies);", lambda x: int(x) == 0),
]

    for name, query, rule in checks:
        cursor.execute(query)
        result = cursor.fetchone()
        value = result[0] if len(result) == 1 else result
        if rule(value):
            print(f"✅ {name}")
        else:
            print(f"❌ {name} FAILED (value={value})")

    conn.close()

def main():
    print("🚀 Starting ETL orchestration")

    # Step 1: Apply schema (optional if already applied)
    # apply_schema()

    # Step 2: Load all Excel data
    load_all()

    # Step 3: Run validations
    run_validations(DB_PATH)

    print("\n🎉 ETL process complete")

if __name__ == "__main__":
    main()
