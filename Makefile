load:
    python src/etl/loader.py

ratios:
    python src/etl/ratios.py

test:
    pytest tests/etl/

report:
    python src/etl/report.py

dashboard:
    streamlit run dashboard.py

clean:
    rm -rf output/*.csv db/nifty100.db
