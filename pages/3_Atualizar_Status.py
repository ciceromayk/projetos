import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

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

worksheet = sheet.worksheet("STATUS")

data = worksheet.get_all_records()

df = pd.DataFrame(data)

st.title("✏️ Atualizar Status")

projetos = df["projeto"].unique()
disciplinas = df["disciplina"].unique()

projeto = st.selectbox("Projeto", projetos)

disciplina = st.selectbox("Disciplina", disciplinas)

status = st.selectbox(
    "Status",
    [0,1,2,3,4]
)

if st.button("Salvar"):

    for i,row in df.iterrows():

        if row["projeto"] == projeto and row["disciplina"] == disciplina:

            worksheet.update_cell(i+2,3,status)

    st.success("Status atualizado")
