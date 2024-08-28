import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
import db_dtypes as db
import plotly.express as px
import time
import geopandas as gpd
import plotly.graph_objects as go


# Backend
st.set_page_config(layout="wide", initial_sidebar_state='expanded')
with open('style.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# Logo - Titre
image = "https://i.goopics.net/an3xxk.png"
image_2 = "https://d26jy9fbi4q9wx.cloudfront.net/assets/logo-ae2beeecce25d711f577b08deb9adfc6c02b673ed106b8d6c3da0f1721d9da33.svg"
container = st.container()
container.markdown(
    f'''
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <img src="{image}" style="width: 200px; margin-right: 10px; margin-bottom: 8px;">
        <h1 style="color: #113f60; margin: 0;">La résidence secondaire à prix accessible !</h1>
        <img src="{image_2}" style="width: 100px; margin-right: 10px; margin-bottom: 20px;">
    </div>
    ''',
    unsafe_allow_html=True
)
# La GROSSE BARRE
st.markdown(
 """
    <div style="height: 4px; background-color: #113f60;width: 100%; margin-top: 20px;"></div>
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
 # Mapping
#geodata = gpd.read_file('data_geo/departements.geojson')
#df_geo = pd.merge(geodata, top_10, left_on='code', right_on='department_code', how='inner')
#df_geo = df_geo.drop(['code', 'nom'], axis=1)

# Création d'une map "choropleth", elle affichera les 10 départements selectionnés.
       #fig = px.choropleth_mapbox(df_geo, 
                               #geojson=df_geo.geometry, 
                               #locations=df_geo.index,  
                               #mapbox_style="carto-positron", 
                               #hover_name='department_name',
                               #color= "colorank",  
                               #color_discrete_map=color_dict, 
                               #center={ "lat": 46.8, "lon": 1.8}, 
                               #custom_data=['department_name', 'geographie'], 
                               #zoom=4.2, 
                               #opacity=0.9) 
                                

       #fig.update_traces(
       #hovertemplate=
           #"<b>%{customdata[0]}</b><br>Relief: %{customdata[1]}"
       #)

       #fig.update_layout(margin={"r": 0, "t": 10, "l": 0, "b": 0}, showlegend=False, legend_itemwidth=35, width=650)
       #col1.plotly_chart(fig, use_container_width=True)



# Graph tableau
    #with col2: 

            #top_10["avg_sales_maison"] = top_10["avg_sales_maison"].round(decimals=0)
            #top_10["avg_sales_maison"] = top_10["avg_sales_maison"].astype(int)
            #top_10["avg_sales_appt"] = top_10["avg_sales_appt"].round(decimals=0)
            #top_10["avg_sales_appt"] = top_10["avg_sales_appt"].astype(int)

            #def add_euro_symbol(value):
                #return f"{value} €"

            #top_10["avg_sales_maison"] = top_10["avg_sales_maison"].map(add_euro_symbol)
            #top_10["avg_sales_appt"] = top_10["avg_sales_appt"].map(add_euro_symbol)

            #top_10_renamed = top_10[["department_code", "department_name", "avg_sales_maison", "avg_sales_appt"]].rename(
                    #columns={"department_code": "Numéros", "department_name": "Départements", "avg_sales_maison":"Prix moyen d'une maison",
                             #"avg_sales_appt":"Prix moyen d'un appart"})

           # top_10_no_index = top_10_renamed.reset_index(drop=True)
           # table_html = top_10_no_index.to_html(index=False)

            #style_css = """
                #<style>
               # th {
                   # background-color: #E1DCCA; 
               # }
               # th:nth-child(1) {
                #text-align: center; 
                #  }
                #th:nth-child(2) {
                #text-align: center;
                #}
               # }
               # th:nth-child(3) {
                #text-align: center;
               # }
                #}
                #th:nth-child(4) {
                #text-align: center;
                #}
                #td {
                #text-align: center; 
                #}
                #</style>
            #"""
 




