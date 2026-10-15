import pandas as pd
from pathlib import Path

# File locations
input_file = Path("data") / "Raw" / "Online Retail.xlsx"
output_file = Path("data") / "Processed" / "online_retail_cleaned.csv"

# Load original data
df = pd.read_excel(input_file)

print("Original rows:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing product descriptions
df = df.dropna(subset=["Description"])

# Keep valid sales quantities and prices
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Exclude cancelled invoices (invoice numbers beginning with C)
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Create output folder
output_file.parent.mkdir(parents=True, exist_ok=True)

# Save cleaned data
df.to_csv(output_file, index=False)

print("Cleaned rows:", len(df))
print("Rows removed:", 541909 - len(df))
print("Total revenue:", round(df["Revenue"].sum(), 2))
print("Saved cleaned dataset to:", output_file)