import sqlite3
from pathlib import Path

db_file = Path("data") / "Database" / "sales.db"

with sqlite3.connect(db_file) as conn:

    # Query 1: Total revenue
    print("\n1. TOTAL REVENUE")
    query1 = """
    SELECT ROUND(SUM(Revenue), 2) AS total_revenue
    FROM sales;
    """
    print(conn.execute(query1).fetchall())

    # Query 2: Top 10 countries by revenue
    print("\n2. TOP 10 COUNTRIES")
    query2 = """
    SELECT Country, ROUND(SUM(Revenue), 2) AS revenue
    FROM sales
    GROUP BY Country
    ORDER BY revenue DESC
    LIMIT 10;
    """
    for row in conn.execute(query2):
        print(row)

    # Query 3: Monthly revenue
    print("\n3. MONTHLY REVENUE")
    query3 = """
    SELECT SUBSTR(InvoiceDate, 1, 7) AS month,
           ROUND(SUM(Revenue), 2) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month;
    """
    for row in conn.execute(query3):
        print(row)

    # Query 4: Top 10 products by revenue
    print("\n4. TOP 10 PRODUCTS")
    query4 = """
    SELECT Description, ROUND(SUM(Revenue), 2) AS revenue
    FROM sales
    GROUP BY Description
    ORDER BY revenue DESC
    LIMIT 10;
    """
    for row in conn.execute(query4):
        print(row)