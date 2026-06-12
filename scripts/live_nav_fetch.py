import requests
import pandas as pd

url = "https://api.mfapi.in/mf/119551"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(
    data["data"]
)

print(nav_df.head())

nav_df.to_csv(
    "../data/raw/live_nav.csv",
    index=False
)