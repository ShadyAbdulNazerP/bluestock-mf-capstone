-- Top 5 Funds by AUM
SELECT *
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM nav_history_clean;

-- Transactions by State
SELECT state,
COUNT(*)
FROM investor_transactions_clean
GROUP BY state;

-- Expense Ratio < 1%
SELECT *
FROM scheme_performance_clean
WHERE expense_ratio_pct < 1;

-- Category Count
SELECT category,
COUNT(*)
FROM fund_master
GROUP BY category;

-- Average Return by Category
SELECT category,
AVG(return_1yr_pct)
FROM scheme_performance_clean
GROUP BY category;

-- Risk Grade Count
SELECT risk_grade,
COUNT(*)
FROM scheme_performance_clean
GROUP BY risk_grade;

-- Top Fund Houses by AUM
SELECT fund_house,
SUM(aum_crore)
FROM aum_by_fund_house
GROUP BY fund_house;

-- Benchmark Count
SELECT benchmark,
COUNT(*)
FROM scheme_performance_clean
GROUP BY benchmark;

-- Average Sharpe Ratio
SELECT AVG(sharpe_ratio)
FROM scheme_performance_clean;