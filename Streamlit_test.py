import streamlit as st
import pandas as pd
import numpy as np
import db_dtypes as db
import plotly.express as px
import time
import geopandas as gpd
import plotly.graph_objects as go

# Chargement des données
data = pd.read_csv("merged_df_streamlit.csv")
geojson_data = gpd.read_file("departements.geojson")



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

# Création des variables pour les critères
POI_selected = False
Sun_selected = False
Population_selected = False
Relief_selected = False

# Création des colonnes pour les selectbox
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Critère POI
with col1:
    POI_selected = st.selectbox(
        "Une envie de visiter des lieux touristique ?",
        ("Oui!", "Vite fait", "Pas envie"),
        index=None,
        placeholder="Choix",
        key="Critere 1"
    )

# Filtrage des données selon POI
if POI_selected == "Oui!":
    data = data[data["total_poi_tourist"] >= 500]
elif POI_selected == "Vite fait":
    data = data[data["total_poi_tourist"] >= 250]
elif POI_selected == "Pas envie":
    data = data[data["total_poi_tourist"] < 250]

# Critère Soleil
with col2:
    Sun_selected = st.selectbox(
        "Et le soleil ?",
        ("J'en veut !", "Pourquoi pas", "Le moins possible"),
        index=None,
        placeholder="Choix",
        key="Critere 2"
    )

# Filtrage des données selon Sun
if Sun_selected == "J'en veut !":
    data = data[data["jour_soleil_an"] >= 180]
elif Sun_selected == "Pourquoi pas":
    data = data[data["jour_soleil_an"] >= 135]
elif Sun_selected == "Le moins possible":
    data = data[data["jour_soleil_an"] < 135]

# Critère Population
with col3:
    Population_selected = st.selectbox(
        "Tu préfère la tranquillité ?",
        ("Oui", "Peu importe"),
        index=None,
        placeholder="Choix",
        key="Critere 3"
    )

# Filtrage des données selon Population
if Population_selected == "Oui":
    data = data[data["population_2019"] <= 2000000]
elif Population_selected == "Peu importe":
    data = data[data["population_2019"] > 1000000]

# Critère Relief
with col4:
    Relief_selected = st.selectbox(
        "En terme de relief ?",
        ("Mer", "Montagne", "Plaine"),
        index=None,
        placeholder="Choix",
        key="Critere 4"
    )

# Filtrage des données selon Relief
if Relief_selected == "Mer":
    data = data[data['relief'] == 'Mer']
elif Relief_selected == "Montagne":
    data = data[data['relief'] == 'Montagne']
elif Relief_selected == "Plaine":
    data = data[data['relief'] == 'Plaine']

# Calcul du score final
data["score_final"] = data["prix_moyen_m²_2021"] + data["nb_second_home_2018"]

# Sélectionner le TOP 10 basé sur le score
top_10 = data.nsmallest(10, 'score_final')

# Réinitialisation de l'index pour le tableau
top_10 = top_10.reset_index(drop=True).reset_index()
top_10['index'] += 1
top_10 = top_10.set_index('index')

# Tableau top 10
st.header("Top 10 Départements")
st.dataframe(top_10[["code", "nom", "prix_moyen_m²_2021"]])

# Graphique Scatter
st.subheader("En 2021 le prix moyen du m² tout départements confondu était de 3000€")
size_value = data["total_poi_tourist"]
fig_scatter = px.scatter(
    top_10,
    x="prix_moyen_m²_2021",
    y="total_poi_tourist",
    color = "nom" ,
    text="nom",
    title="Total POI vs Prix Moyen du m²",
    labels={"prix_moyen_m²_2021": "Prix Moyen du m²", "total_poi_tourist": "Total POI Touristique"}
)
fig_scatter.update_traces(textposition='top center')
st.plotly_chart(fig_scatter)

# Graphique Bar
fig_bar = px.bar(
    top_10,
    x="nom",
    y="nb_second_home_2018",
    color = "nom",
    title="Nombre de Résidences Secondaires par Département",
    labels={"nb_second_home_2018": "Nombre de Résidences Secondaires"}
)
mean_value = top_10["nb_second_home_2018"].mean()
fig_bar.add_shape(
    type="line",
    x0=-0.5, x1=len(top_10)-0.5,
    y0=mean_value, y1=mean_value,
    line=dict(color="Red", width=2, dash="dash")
)
st.plotly_chart(fig_bar)

#Maping
color_dict = {
    1: 'blue', 2: 'green', 3: 'purple', 4: 'red', 5: 'orange',
    6: 'yellow', 7: 'pink', 8: 'cyan', 9: 'magenta', 10: 'brown'
}
geojson_data = pd.merge(geojson_data, top_10, left_on='code', right_on='code', how='inner')
geojson_data = geojson_data.drop(['code', 'nom_geo'], axis=1)
geojson_data['colorank'] = geojson_data['prix_moyen_m²_2021'].rank(ascending=True)
fig = px.choropleth_mapbox(geojson_data,
                           geojson=geojson_data.geometry,
                           locations=geojson_data.index,
                           mapbox_style="carto-positron",
                           hover_name='nom_data',
                           color="colorank",
                           color_discrete_map=color_dict,
                           center={"lat": 46.8, "lon": 1.8},
                           custom_data=['nom_data'],
                           zoom=4.2,
                           opacity=0.9)

fig.show()
