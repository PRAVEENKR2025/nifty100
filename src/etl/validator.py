import pandas as pd

# DQ‑01: Primary Key uniqueness
def dq01_pk_uniqueness(df, col):
    return df[col].is_unique

# DQ‑02: Composite PK (company_id, year)
def dq02_company_year_pk(df):
    return df[['company_id','year']].drop_duplicates().shape[0] == df.shape[0]

# DQ‑03: Foreign Key integrity
def dq03_fk_integrity(df, fk_col, ref_df, ref_col):
    return df[fk_col].isin(ref_df[ref_col]).all()

# DQ‑04: Balance Sheet balance <1%
def dq04_bs_balance(df):
    return ((abs(df['assets'] - df['liabilities']) / df['assets']) < 0.01).all()

# DQ‑05: OPM cross‑check
def dq05_opm(df):
    return (df['operating_profit'] / df['sales']).between(0,1).all()

# DQ‑06: Positive sales
def dq06_positive_sales(df):
    return (df['sales'] > 0).all()


def run_validations(dataframes):
    failures = []
    # Example: companies table
    if not dq01_pk_uniqueness(dataframes['companies'], 'company_id'):
        failures.append(("DQ‑01", "CRITICAL", "companies", "PK not unique"))

    # Add checks for each rule
    return pd.DataFrame(failures, columns=["rule_id","severity","table","description"])

# … continue until DQ‑16 (net cash, tax rate, dividend cap, URL validity, EPS sign, coverage, etc.)
