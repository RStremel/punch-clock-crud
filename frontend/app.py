import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Punch Clock App",
    page_icon=":stopwatch:",
    layout="centered", 
    initial_sidebar_state="auto",
    menu_items={
        "About": "A punch clock webapp that performs CRUD operation in a Postgres database using SQLAlchemy, FastAPI and Pydantic, hosted on Streamlit and containerized in Docker.",
        "Get Help": "https://github.com/RStremel/punch-clock-crud"
    })

# st.image("frontend\logo.png", width=200)

st.title("Punch Clock App :stopwatch:", help="Attention, workers: don't forget to punch in and out of the clock as you begin and end your shifts. We are watching you!")