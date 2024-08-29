import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
data = pd.read_csv("New_merged_df_streamlit.csv")

# Assurez-vous que le code est bien un entier
data['code'] = data['code'].astype(int)

# Calcul du score final
data["score_final"] = data["prix_moyen_m²_2021"] + data["total_nb_second_home"]

# Sélectionner le TOP 10 basé sur le score
top_10 = data.nsmallest(10, 'score_final')

# Réinitialisation de l'index pour le tableau
top_10 = top_10.reset_index(drop=True).reset_index()
top_10['index'] += 1
top_10 = top_10.set_index('index')

# Renommer les colonnes
top_10_renamed = top_10.rename(columns={
    "code": "Code Département",
    "nom": "Nom du Département",
    "prix_moyen_m²_2021": "Prix Moyen au m² en 2021"
})

# Créer deux colonnes
col1, col2 = st.columns([1, 1])

# Afficher le tableau dans la première colonne
with col1:
    st.header("Top 10 Départements")
    st.dataframe(top_10_renamed[["Code Département", "Nom du Département", "Prix Moyen au m² en 2021"]])

# Créer le graphique scatter et l'afficher dans la deuxième colonne
with col2:
    st.subheader("Total POI vs Prix Moyen du m²")
    fig_scatter = px.scatter(
        top_10,
        x="prix_moyen_m²_2021",
        y="total_poi_tourist",
        color="nom",
        text="nom",
        title="Total POI vs Prix Moyen du m²",
        labels={"prix_moyen_m²_2021": "Prix Moyen du m²", "total_poi_tourist": "Total POI Touristique"}
    )
    fig_scatter.update_traces(textposition='top center')
    st.plotly_chart(fig_scatter)

# Si besoin d'ajouter le graphique bar plus bas dans la page
st.subheader("Nombre de Résidences Secondaires par Département")
fig_bar = px.bar(
    top_10,
    x="nom",
    y="total_nb_second_home",
    color="nom",
    title="Nombre de Résidences Secondaires par Département",
    labels={"total_nb_second_home": "Nombre de Résidences Secondaires"}
)
mean_value = top_10["total_nb_second_home"].mean()
fig_bar.add_shape(
    type="line",
    x0=-0.5, x1=len(top_10)-0.5,
    y0=mean_value, y1=mean_value,
    line=dict(color="Red", width=2, dash="dash")
)
st.plotly_chart(fig_bar)
