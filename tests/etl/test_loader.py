import pandas as pd
from src.etl.loader import process_file

def test_process_file(tmp_path):
    # Create a temporary Excel file
    df = pd.DataFrame({
        "company_id": [1, 2],
        "year": ["FY2020", "2021"],
        "ticker": ["RELIANCE.NS", "TCS.BSE"]
    })
    file_path = tmp_path / "test.xlsx"
    df.to_excel(file_path, index=False)

    processed = process_file(file_path)

    assert processed["year"].tolist() == [2020, 2021]
    assert processed["ticker"].tolist() == ["RELIANCE", "TCS"]
