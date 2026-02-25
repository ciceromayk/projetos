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

# ACESSO DIRETO PELA CHAVE DA PLANILHA
sheet = client.open_by_key("1muzEFsb3MsDkQFhhrehtwCwbrMgqi2A08StwqNjlmXs")

worksheet = sheet.worksheet("STATUS")


def load_status():

    data = worksheet.get_all_records()

    df = pd.DataFrame(data)

    return df
