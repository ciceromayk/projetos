import streamlit as st
import pandas as pd
import plotly.express as px
from services.google_sheets import load_status
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

st.title("🔎 Raio X dos Projetos")

df = load_status()

matrix = df.pivot(
    index="disciplina",
    columns="projeto",
    values="status"
)

fig = px.imshow(
    matrix,
    color_continuous_scale=[
        (0.0,"red"),
        (0.25,"orange"),
        (0.5,"blue"),
        (0.75,"purple"),
        (1.0,"green")
    ],
    aspect="auto"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(matrix, use_container_width=True)
