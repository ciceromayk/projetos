import streamlit as st
import plotly.express as px
from pages.google_sheets import load_status

st.title("Raio X dos Projetos")

df = load_status()

matrix = df.pivot(
    index="disciplina",
    columns="projeto",
    values="status"
)

fig = px.imshow(matrix, color_continuous_scale="RdYlGn")

st.plotly_chart(fig, use_container_width=True)

st.dataframe(matrix, use_container_width=True)
