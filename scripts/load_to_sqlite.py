from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

from dbm import sqlite3

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

files = Path("data/processed").glob("*.csv")

for file in files:

    table_name = file.stem

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(table_name)
print("Loaded successfully")

import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

tables = pd.read_sql(
"""
SELECT name
FROM sqlite_master
WHERE type='table'
""",
conn
)

print(tables)