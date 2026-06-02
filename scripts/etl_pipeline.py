import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

files = data_path.glob("*.csv")

for file in files:

    print("\n" + "="*50)
    print("FILE:", file.name)

    df = pd.read_csv("data/raw/01_fund_master.csv")

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())