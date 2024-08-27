import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
 
# Backend
st.set_page_config(layout="wide", initial_sidebar_state='expanded')
#credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
#client = bigquery.Client(credentials=credentials)

with open('style.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#query = ("SELECT * FROM `projet-prello.transform_prello.score_table_full` ")

#query_job = client.query(query)
#query_result = query_job.result()
#data = query_result.to_dataframe()

# Logo - Titre
image = "https://i.goopics.net/an3xxk.png"
container = st.container()
container.markdown(
    f'''
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <img src="{image}" style="width: 200px; margin-right: 10px;">
        <h1 style="color: #113f60; margin: 0;">La résidence secondaire à prix accessible !</h1>
    </div>
    ''',
    unsafe_allow_html=True
)
# La GROSSE BARRE
st.markdown(
 """
    <div style="height: 4px; background-color: #113f60;width: 100%; margin-top: 10px;"></div>
    """,
    unsafe_allow_html=True)

#Création d'une variable pour chaque critère. Par défaut sur False, elle sera changée en True si un critère est selectionné dans la selectbox.
Critere_1 = False
Critere_2 = False
Critere_3 = False
Critere_4 = False
Critere_5 = False
Critere_6 = False

# Création des colonnes pour les selectbox
col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

# Critere 1
with col1:
     critere_1 = st.selectbox(
       "",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Choix",
       key="Critere 1"
)
# Critere 2
with col2:
     critere_2 = st.selectbox(
       "",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Choix",
       key="Critere 2"
     )
 # Critere 3
with col3:
     critere_3 = st.selectbox(
       "",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Choix",
       key="Critere 3"
     )
 # Critere 4
with col4:
     critere_4 = st.selectbox(
       "",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Choix",
       key="Critere 4"
     )
 # Critere 2
with col5:
     critere_5 = st.selectbox(
       "",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Choix",
       key="Critere 5"
     )
 # Critere 1
with col6:
     critere_6 = st.selectbox(
       "",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Choix",
       key="Critere 6"
)
 




