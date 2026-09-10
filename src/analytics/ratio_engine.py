import sqlite3
from src.analytics import ratios
import os

DB_PATH = r"C:\BLUESTOCK PROJECTS\nifty100\db\nifty100.db"
LOG_PATH = r"C:\BLUESTOCK PROJECTS\nifty100\output\ratio_edge_cases.log"

def log_edge_case(company_id, year, message):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"[Company {company_id} | Year {year}] {message}\n")

def run_ratio_engine():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.company_id, p.year, p.sales, p.operating_profit, p.net_profit,
           b.assets, b.liabilities
    FROM profitandloss p
    JOIN balancesheet b ON p.company_id = b.company_id AND p.year = b.year
    """)

    rows = cursor.fetchall()

    for row in rows:
        (company_id, year, sales, op, np,
         assets, liabilities) = row

        equity = assets - liabilities if assets and liabilities else 0
        reserves = 0
        borrowings = 0

        try:
            roe = ratios.return_on_equity(np, equity, reserves)
            de, _ = ratios.debt_to_equity(borrowings, equity, reserves)

            # Edge case checks
            if equity == 0:
                log_edge_case(company_id, year, "Equity is zero → ROE undefined")
            if de is None or de < 0:
                log_edge_case(company_id, year, f"Debt/Equity anomaly: {de}")

            cursor.execute("""
                INSERT OR REPLACE INTO financial_ratios (
                    company_id, year, roe, debt_equity
                ) VALUES (?, ?, ?, ?)
            """, (company_id, year, roe, de))

        except Exception as e:
            log_edge_case(company_id, year, f"Error calculating ratios: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_ratio_engine()
    print("✅ financial_ratios table populated with ROE and Debt/Equity")
    print(f"📂 Edge cases logged to: {LOG_PATH}")
