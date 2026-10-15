import pandas as pd
import sqlite3
from pathlib import Path

# Input cleaned dataset
csv_file = Path("data") / "Processed" / "online_retail_cleaned.csv"

# Create database folder
db_folder = Path("data") / "Database"
db_folder.mkdir(parents=True, exist_ok=True)

# Database location
db_file = db_folder / "sales.db"

# Load cleaned data
df = pd.read_csv(csv_file)

# Create SQLite database and table
with sqlite3.connect(db_file) as conn:
    df.to_sql("sales", conn, if_exists="replace", index=False)

    result = pd.read_sql_query(
        "SELECT COUNT(*) AS total_records FROM sales",
        conn
    )

    print("Database created successfully!")
    print("Records loaded:", result.iloc[0, 0])
    print("Database location:", db_file)