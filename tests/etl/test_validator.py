import pandas as pd
from src.etl import validator

def test_dq01_pk_uniqueness():
    df = pd.DataFrame({"company_id":[1,2,2]})
    assert validator.dq01_pk_uniqueness(df,"company_id") == False

