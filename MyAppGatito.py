import streamlit as st
st.title("Mi primer app")
st.button("SI")
st.button("NO")
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
st.write(df)
st.map(df)