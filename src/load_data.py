import pandas as pd
from pathlib import Path

# Locate the dataset from the project root
file_path = Path("data") / "Raw" / "Online Retail.xlsx"

# Load the Excel dataset
df = pd.read_excel(file_path)

# Display the first 5 rows
print(df.head())

# Display dataset dimensions
print("\nDataset shape:", df.shape)

# Display column names
print("\nColumns:")
print(df.columns.tolist())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
# Total number of records
print("\nTotal records:", len(df))

# Missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate rows:", df.duplicated().sum())

# Basic sales statistics
print("\nSales statistics:")
print(df[["Quantity", "UnitPrice"]].describe())