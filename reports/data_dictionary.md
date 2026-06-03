# Data Dictionary

## 01_fund_master.csv

| Column            | Data Type | Description                    |
| ----------------- | --------- | ------------------------------ |
| amfi_code         | Integer   | Unique AMFI scheme identifier  |
| fund_house        | Text      | Asset Management Company (AMC) |
| scheme_name       | Text      | Mutual fund scheme name        |
| category          | Text      | Fund category                  |
| sub_category      | Text      | Fund sub-category              |
| plan              | Text      | Direct/Regular plan            |
| launch_date       | Date      | Scheme launch date             |
| benchmark         | Text      | Benchmark index                |
| expense_ratio_pct | Float     | Expense ratio percentage       |
| risk_category     | Text      | Risk classification            |

Source: Fund Master Dataset

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Fund identifier |
| date      | Date      | NAV date        |
| nav       | Float     | Net Asset Value |

Source: NAV History Dataset

---

## 07_scheme_performance.csv

| Column            | Data Type | Description                 |
| ----------------- | --------- | --------------------------- |
| amfi_code         | Integer   | Fund identifier             |
| return_1yr_pct    | Float     | 1-year return (%)           |
| return_3yr_pct    | Float     | 3-year return (%)           |
| return_5yr_pct    | Float     | 5-year return (%)           |
| alpha             | Float     | Alpha performance metric    |
| beta              | Float     | Beta risk metric            |
| sharpe_ratio      | Float     | Risk-adjusted return metric |
| expense_ratio_pct | Float     | Expense ratio (%)           |
| risk_grade        | Text      | Risk classification         |

Source: Scheme Performance Dataset

---

## 08_investor_transactions.csv

| Column           | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| investor_id      | Integer   | Investor identifier     |
| transaction_id   | Integer   | Transaction identifier  |
| amfi_code        | Integer   | Fund identifier         |
| transaction_date | Date      | Transaction date        |
| amount_inr       | Float     | Transaction amount      |
| state            | Text      | Investor state          |
| city             | Text      | Investor city           |
| kyc_status       | Text      | KYC verification status |

Source: Investor Transactions Dataset
