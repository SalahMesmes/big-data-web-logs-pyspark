from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "output"


def display_csv_file(filename: str):
    """
    Affiche le contenu d'un fichier CSV exporté par PySpark.
    """
    file_path = OUTPUT_DIR / filename

    if not file_path.exists():
        print(f"Fichier introuvable : {file_path}")
        return

    df = pd.read_csv(file_path)

    print()
    print("=" * 60)
    print(f"Fichier : {filename}")
    print("=" * 60)
    print(df)


def main():
    """
    Affiche les résultats principaux exportés par l'analyse PySpark.
    """

    files = [
        "total_visites.csv",
        "utilisateurs_uniques.csv",
        "pages_plus_visitees.csv",
        "actions_frequentes.csv",
        "chiffre_affaires_par_pays.csv",
        "chiffre_affaires_par_categorie.csv",
        "temps_reponse_moyen.csv",
        "codes_statut.csv",
        "visites_par_appareil.csv"
    ]

    print("Résumé des résultats exportés par PySpark")

    for file in files:
        display_csv_file(file)


if __name__ == "__main__":
    main()