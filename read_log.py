import pandas as pd
import os

CSV_PATH = "log.csv"

if not os.path.exists(CSV_PATH):
    print("log.csv not found. Run 'python main.py' to generate log entries.")
    raise SystemExit(1)

try:
    df = pd.read_csv(CSV_PATH, parse_dates=["Timestamp"]) if os.path.getsize(CSV_PATH) > 0 else pd.DataFrame()
    if df.empty:
        print("log.csv is empty.")
    else:
        # Show last 5 records in a clean table
        print("\nLast 5 records in log.csv:\n")
        print(df.tail(5).to_string(index=False))
except Exception as e:
    print(f"Failed to read CSV: {e}")
    raise
