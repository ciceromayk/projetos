import streamlit as st
from pages.google_sheets import load_status

st.title("Dashboard de Projetos")

df = load_status()

progress = df.groupby("projeto")["status"].mean() / 4

progress = progress.sort_values(ascending=False)

for projeto, valor in progress.items():

    st.subheader(projeto)

    st.progress(float(valor))

    st.write(f"{round(valor*100)} % concluído")
