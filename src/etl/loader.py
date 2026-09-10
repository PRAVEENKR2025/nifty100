import sqlite3
import pandas as pd

DB_PATH = r"C:\BLUESTOCK PROJECTS\nifty100\db\nifty100.db"

def insert_companies(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO companies (company_id, name, sector_id)
            VALUES (?, ?, ?)
        """, (int(row['company_id']), row['name'], int(row['sector_id'])))
    conn.commit()
    conn.close()

def insert_sectors(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO sectors (sector_id, sector_name)
            VALUES (?, ?)
        """, (int(row['sector_id']), row['sector_name']))
    conn.commit()
    conn.close()

def insert_profitandloss(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO profitandloss (company_id, year, sales, operating_profit, net_profit)
            VALUES (?, ?, ?, ?, ?)
        """, (int(row['company_id']), int(row['year']), float(row['sales']),
              float(row['operating_profit']), float(row['net_profit'])))
    conn.commit()
    conn.close()

def insert_balancesheet(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO balancesheet (company_id, year, assets, liabilities)
            VALUES (?, ?, ?, ?)
        """, (int(row['company_id']), int(row['year']), float(row['assets']), float(row['liabilities'])))
    conn.commit()
    conn.close()

def insert_cashflow(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO cashflow (company_id, year, operating_cash, investing_cash, financing_cash)
            VALUES (?, ?, ?, ?, ?)
        """, (int(row['company_id']), int(row['year']), float(row['operating_cash']),
              float(row['investing_cash']), float(row['financing_cash'])))
    conn.commit()
    conn.close()

def insert_analysis(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO analysis (company_id, year, eps, pe_ratio)
            VALUES (?, ?, ?, ?)
        """, (int(row['company_id']), int(row['year']), float(row['eps']), float(row['pe_ratio'])))
    conn.commit()
    conn.close()

def insert_documents(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO documents (doc_id, company_id, url, description)
            VALUES (?, ?, ?, ?)
        """, (int(row['doc_id']), int(row['company_id']), row['url'], row['description']))
    conn.commit()
    conn.close()

def insert_prosandcons(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO prosandcons (company_id, year, pros, cons)
            VALUES (?, ?, ?, ?)
        """, (int(row['company_id']), int(row['year']), row['pros'], row['cons']))
    conn.commit()
    conn.close()

def insert_stock_prices(excel_path):
    df = pd.read_excel(excel_path)
    df['date'] = pd.to_datetime(df['date']).dt.strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO stock_prices (sp_id, company_id, date, close_price)
            VALUES (?, ?, ?, ?)
        """, (int(row['sp_id']), int(row['company_id']), row['date'], float(row['close_price'])))
    conn.commit()
    conn.close()

def insert_financial_ratios(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO financial_ratios (company_id, year, roe, debt_equity)
            VALUES (?, ?, ?, ?)
        """, (int(row['company_id']), int(row['year']), float(row['roe']), float(row['debt_equity'])))
    conn.commit()
    conn.close()

def insert_peer_groups(excel_path):
    df = pd.read_excel(excel_path)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO peer_groups (company_id, peer_company_id)
            VALUES (?, ?)
        """, (int(row['company_id']), int(row['peer_company_id'])))
    conn.commit()
    conn.close()
