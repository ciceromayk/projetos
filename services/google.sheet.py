import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)

sheet = client.open("PROJECT_XRAY_DB")

def load_status():

    worksheet = sheet.worksheet("STATUS")

    data = worksheet.get_all_records()

    return pd.DataFrame(data)
