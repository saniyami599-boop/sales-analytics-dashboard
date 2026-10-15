import pandas as pd

# Load cleaned data
df = pd.read_csv("data/Processed/online_retail_cleaned.csv")

# Convert invoice dates to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Monthly revenue
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Revenue"].sum().sort_index()

print("\nMONTHLY REVENUE")
print(monthly_sales)

# Top 10 products by revenue
top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY REVENUE")
print(top_products)

# Revenue by country
country_sales = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 COUNTRIES BY REVENUE")
print(country_sales)
import matplotlib.pyplot as plt
from pathlib import Path

# Create a folder for charts
charts_dir = Path("reports") / "charts"
charts_dir.mkdir(parents=True, exist_ok=True)

# Chart 1: Monthly revenue
monthly_sales.plot(kind="line", marker="o", figsize=(12, 6))
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(charts_dir / "monthly_revenue.png")
plt.show()
plt.close()

# Chart 2: Top 10 products
top_products.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig(charts_dir / "top_products.png")
plt.show()
plt.close()

# Chart 3: Top 10 countries
country_sales.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig(charts_dir / "top_countries.png")
plt.show()
plt.close()

print("\nAll charts saved in reports/charts/")