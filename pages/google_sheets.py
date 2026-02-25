import pandas as pd

SHEET_URL = "https://docs.google.com/spreadsheets/d/1muzEFsb3MsDkQFhhrehtwCwbrMgqi2A08StwqNjlmXs/export?format=csv"

def load_status():

    df = pd.read_csv(SHEET_URL)

    return df
