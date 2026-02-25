import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import plotly.express as px
from google_sheets import load_status

st.title("Raio X dos Projetos")

df = load_status()

matrix = df.pivot(
    index="disciplina",
    columns="projeto",
    values="status"
)

fig = px.imshow(
    matrix,
    color_continuous_scale="RdYlGn",
    aspect="auto"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(matrix, use_container_width=True)
