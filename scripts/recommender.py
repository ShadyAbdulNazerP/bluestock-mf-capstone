import pandas as pd

scorecard = pd.read_csv(
    "../reports/fund_scorecard.csv"
)

perf = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

merged = perf.merge(
    scorecard,
    on="amfi_code",
    suffixes=("_perf", "_score")
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

filtered = merged[
    merged["risk_grade"] == risk
]

top3 = filtered.sort_values(
    "sharpe_ratio_score",
    ascending=False
).head(3)

print(
    top3[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio_score",
            "cagr",
            "fund_score"
        ]
    ]
)