import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

# employees = pd.read_sql("""
# SELECT * FROM employees
#                         WHERE lastName = 'Patterson';
# """, conn)
# print(employees)

# employees = pd.read_sql("""
# SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
#   FROM orderDetails
#  WHERE rounded_price_int = 30;
# """, conn)

# employees = pd.read_sql("""
# SELECT *, strftime("%m", orderDate) AS month
#   FROM orders
#  WHERE month = "01";
# """, conn)

employees = pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
  FROM orders
 WHERE days_late > 0;
""", conn)

print(employees)

conn.close()