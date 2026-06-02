CREATE TABLE fund_master (
    amfi_code INTEGER,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT
);
import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

query = """
SELECT *
FROM fund_master
LIMIT 5
"""

df = pd.read_sql(query, conn)

df