import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = r"C:\BLUESTOCK PROJECTS\nifty100\db\nifty100.db"

def plot_sector_distribution():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT s.sector_name, COUNT(c.company_id) AS company_count
        FROM companies c
        JOIN sectors s ON c.sector_id = s.sector_id
        GROUP BY s.sector_name
    """, conn)
    conn.close()

    plt.figure(figsize=(8,6))
    plt.pie(df['company_count'], labels=df['sector_name'], autopct='%1.1f%%')
    plt.title("Fig‑1: Sector Distribution")
    plt.show()

def plot_top_companies_by_profit(top_n=10):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT c.name, SUM(p.net_profit) AS total_profit
        FROM profitandloss p
        JOIN companies c ON p.company_id = c.company_id
        GROUP BY c.name
        ORDER BY total_profit DESC
        LIMIT ?
    """, conn, params=(top_n,))
    conn.close()

    plt.figure(figsize=(10,6))
    plt.bar(df['name'], df['total_profit'], color="skyblue")
    plt.xticks(rotation=45, ha='right')
    plt.title(f"Fig‑2: Top {top_n} Companies by Net Profit")
    plt.ylabel("Total Profit")
    plt.show()

def plot_stock_price_trend(company_id):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT date, close_price
        FROM stock_prices
        WHERE company_id = ?
        ORDER BY date
    """, conn, params=(company_id,))
    conn.close()

    plt.figure(figsize=(10,6))
    plt.plot(df['date'], df['close_price'], marker='o', color="green")
    plt.xticks(rotation=45, ha='right')
    plt.title(f"Fig‑3: Stock Price Trend (Company ID {company_id})")
    plt.ylabel("Close Price")
    plt.xlabel("Date")
    plt.show()

if __name__ == "__main__":
    plot_sector_distribution()
    plot_top_companies_by_profit(10)
    plot_stock_price_trend(1)  # Example: company_id = 1

plot_top_companies_by_profit(10)
plot_stock_price_trend(1)   # Example: company_id = 1
