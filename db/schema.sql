-- Companies table
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    name TEXT,
    sector_id INTEGER
);

-- Sectors table
CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT
);

-- Profit and Loss table
CREATE TABLE IF NOT EXISTS profitandloss (
    company_id INTEGER,
    year INTEGER,
    sales REAL,
    operating_profit REAL,
    net_profit REAL
);

-- Balance Sheet table
CREATE TABLE IF NOT EXISTS balancesheet (
    company_id INTEGER,
    year INTEGER,
    assets REAL,
    liabilities REAL
);

-- Cash Flow table
CREATE TABLE IF NOT EXISTS cashflow (
    company_id INTEGER,
    year INTEGER,
    operating_cash REAL,
    investing_cash REAL,
    financing_cash REAL
);

-- Analysis table
CREATE TABLE IF NOT EXISTS analysis (
    company_id INTEGER,
    year INTEGER,
    eps REAL,
    pe_ratio REAL
);

-- Documents table
CREATE TABLE IF NOT EXISTS documents (
    doc_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    url TEXT,
    description TEXT
);

-- Pros and Cons table
CREATE TABLE IF NOT EXISTS prosandcons (
    company_id INTEGER,
    year INTEGER,
    pros TEXT,
    cons TEXT
);

-- Stock Prices table
CREATE TABLE IF NOT EXISTS stock_prices (
    sp_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    date TEXT,
    close_price REAL
);

-- Financial Ratios table
CREATE TABLE IF NOT EXISTS financial_ratios (
    company_id INTEGER,
    year INTEGER,
    roe REAL,
    debt_equity REAL
);

-- Peer Groups table
CREATE TABLE IF NOT EXISTS peer_groups (
    company_id INTEGER,
    peer_company_id INTEGER
);
