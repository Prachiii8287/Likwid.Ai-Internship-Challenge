
### customer_utils.py
import pandas as pd
from models import insert_or_update_customer, fetch_all_customers
from collections import defaultdict

def process_excel_file(filepath):
    df = pd.read_excel(filepath)
    for _, row in df.iterrows():
        insert_or_update_customer(
            row["Customer Name"], row["Country"], row["Product"], float(row["Sales"])
        )

def get_dashboard_data():
    rows = fetch_all_customers()
    geo_sales = defaultdict(float)
    product_sales = defaultdict(float)

    for _, name, country, product, sales in rows:
        geo_sales[country] += sales
        product_sales[product] += sales

    top_geo = sorted(geo_sales.items(), key=lambda x: x[1], reverse=True)[:10]
    top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        "top_geography": top_geo,
        "top_products": top_products
    }
