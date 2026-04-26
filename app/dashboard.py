from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "output"


def load_output_file(filename: str) -> pd.DataFrame:
    file_path = OUTPUT_DIR / filename
    return pd.read_csv(file_path)


st.set_page_config(
    page_title="Dashboard Big Data Logs Web",
    page_icon="📊",
    layout="wide"
)

st.title("Analyse Big Data de logs web avec PySpark")

st.write(
    "Ce dashboard présente les résultats d'une analyse de logs web réalisée avec PySpark. "
    "Les données représentent des actions utilisateurs sur un site e-commerce."
)

try:
    total_visites = load_output_file("total_visites.csv")["TotalVisites"].iloc[0]
    utilisateurs_uniques = load_output_file("utilisateurs_uniques.csv")["UtilisateursUniques"].iloc[0]

    col1, col2 = st.columns(2)

    col1.metric("Nombre total de visites", f"{total_visites:,}")
    col2.metric("Utilisateurs uniques", f"{utilisateurs_uniques:,}")

    st.divider()

    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Pages les plus visitées")
        pages = load_output_file("pages_plus_visitees.csv")

        fig, ax = plt.subplots()
        ax.barh(pages["Page"], pages["NombreVisites"])
        ax.set_xlabel("Nombre de visites")
        ax.set_ylabel("Page")
        ax.invert_yaxis()
        st.pyplot(fig)

    with right_col:
        st.subheader("Actions les plus fréquentes")
        actions = load_output_file("actions_frequentes.csv")

        fig, ax = plt.subplots()
        ax.bar(actions["Action"], actions["NombreActions"])
        ax.set_xlabel("Action")
        ax.set_ylabel("Nombre")
        ax.tick_params(axis="x", rotation=30)
        st.pyplot(fig)

    st.divider()

    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Chiffre d'affaires par pays")
        ca_pays = load_output_file("chiffre_affaires_par_pays.csv")

        fig, ax = plt.subplots()
        ax.bar(ca_pays["Pays"], ca_pays["ChiffreAffairesTotal"])
        ax.set_xlabel("Pays")
        ax.set_ylabel("Chiffre d'affaires")
        ax.tick_params(axis="x", rotation=30)
        st.pyplot(fig)

    with right_col:
        st.subheader("Chiffre d'affaires par catégorie")
        ca_categorie = load_output_file("chiffre_affaires_par_categorie.csv")

        fig, ax = plt.subplots()
        ax.bar(ca_categorie["CategorieProduit"], ca_categorie["ChiffreAffairesTotal"])
        ax.set_xlabel("Catégorie")
        ax.set_ylabel("Chiffre d'affaires")
        ax.tick_params(axis="x", rotation=30)
        st.pyplot(fig)

    st.divider()

    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Temps de réponse moyen par page")
        temps = load_output_file("temps_reponse_moyen.csv")

        fig, ax = plt.subplots()
        ax.barh(temps["Page"], temps["TempsReponseMoyenMs"])
        ax.set_xlabel("Temps moyen en ms")
        ax.set_ylabel("Page")
        ax.invert_yaxis()
        st.pyplot(fig)

    with right_col:
        st.subheader("Visites par appareil")
        appareils = load_output_file("visites_par_appareil.csv")

        fig, ax = plt.subplots()
        ax.bar(appareils["Appareil"], appareils["NombreVisites"])
        ax.set_xlabel("Appareil")
        ax.set_ylabel("Nombre de visites")
        st.pyplot(fig)

    st.divider()

    st.subheader("Répartition des codes HTTP")
    codes = load_output_file("codes_statut.csv")
    st.dataframe(codes, use_container_width=True)

    st.subheader("Données exportées par PySpark")
    st.write("Chiffre d'affaires par pays")
    st.dataframe(ca_pays, use_container_width=True)

    st.write("Chiffre d'affaires par catégorie")
    st.dataframe(ca_categorie, use_container_width=True)

except FileNotFoundError:
    st.error(
        "Les fichiers de résultats sont introuvables. "
        "Lance d'abord la commande : python3 src/spark_analysis.py"
    )