# Nifty100 Ratio Engine

## 📌 Overview
This project calculates key financial ratios (ROE, Debt-to-Equity) for Nifty100 companies using data from profit and loss statements and balance sheets.  
It also logs anomalies (e.g., zero equity, negative ratios) for review.

## ⚙️ Features
- Calculates **ROE** and **Debt-to-Equity**
- Logs anomalies to `ratio_edge_cases.log`
- Stores results in `financial_ratios` table
- Ready to expand with more ratios (NPM, OPM, ROA, ROCE, FCF, Capex, FCF Conversion)

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/PRAVEENKR2025/nifty100.git
