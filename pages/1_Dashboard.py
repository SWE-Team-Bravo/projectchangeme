import streamlit as st
from utils.db import get_db

st.title("Dashboard")

db = get_db()

if db is None:
    st.warning("Database is not configured as of now.")
else:
    st.success("Database connection established successfully!")
