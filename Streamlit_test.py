import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
 
# Backend
#st.set_page_config(layout="wide", initial_sidebar_state='expanded')
#credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
#client = bigquery.Client(credentials=credentials)

#with open('style.css') as f:
 #   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#query = ("SELECT * FROM `projet-prello.transform_prello.score_table_full` ")

#query_job = client.query(query)
#query_result = query_job.result()
#data = query_result.to_dataframe()

st.write("""
# My first app
Hello *world!*
""")
# Logo
image = "https://i.goopics.net/an3xxk.png"
container = st.container()
container.markdown(
        f'<div style="display: flex; justify-content: center; margin-top: 0px; margin-bot: 0px;">'
        f'<img src="{image}" style="width: 5;">'
        f'</div>',
        unsafe_allow_html=True
    )
# Titre
st.markdown(
    '<h1 style="text-align: center; margin-top: 0px">La résidence secondaire à prix accessible !</h1>',
    unsafe_allow_html=True
)
st.markdown(" ")
# Position et couleur du titre
st.markdown(
    """
    <div style="height: 4px; background-color: #113f60;"></div>
    """,
    unsafe_allow_html=True
