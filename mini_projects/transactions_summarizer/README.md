# Transaction Summarizer (mini ETL)

Loads a CSV file of transactions and prints:
- total spent
- total income
- totals by merchant
- totals by date
- high-amount flags

## Run
```
python summarizer.py
```

## CSV format
date,merchant,amount,currency
(negative amount = expense, positive = income)
