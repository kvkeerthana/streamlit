import streamlit as st
import pandas as pd

st.title("Student Data Dashboard")

df = pd.read_excel("data/students.xlsx")

st.dataframe(df)