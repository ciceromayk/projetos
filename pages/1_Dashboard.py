import streamlit as st
from google_sheets import load_status

st.title("Dashboard de Projetos")

df = load_status()

progress = df.groupby("projeto")["status"].mean() / 4

for projeto, valor in progress.items():

    st.subheader(projeto)

    st.progress(float(valor))
