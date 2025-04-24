
### google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models import insert_or_update_customer

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("CustomerData").sheet1

def sync_to_sheet():
    data = [["Customer Name", "Country", "Product", "Sales"]]
    from models import fetch_all_customers
    for _, name, country, product, sales in fetch_all_customers():
        data.append([name, country, product, sales])
    sheet.clear()
    sheet.update("A1", data)

def sync_from_sheet():
    records = sheet.get_all_records()
    for row in records:
        insert_or_update_customer(
            row["Customer Name"], row["Country"], row["Product"], float(row["Sales"])
        )