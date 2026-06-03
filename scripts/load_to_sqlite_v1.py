import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

print("Loaded successfully")

conn.close()