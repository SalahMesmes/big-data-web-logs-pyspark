import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "logs_web_fr.csv"


def generate_web_logs(nombre_lignes: int = 1000):
    """
    Génère un fichier CSV de logs web en français.
    Chaque ligne représente une action utilisateur sur un site e-commerce.
    """

    random.seed(42)

    pages = [
        "/accueil",
        "/produits",
        "/details-produit",
        "/panier",
        "/commande",
        "/paiement",
        "/contact",
        "/connexion",
        "/promotion"
    ]

    actions = [
        "voir_page",
        "cliquer_produit",
        "ajouter_panier",
        "passer_commande",
        "achat"
    ]

    appareils = [
        "ordinateur",
        "mobile",
        "tablette"
    ]

    pays = [
        "France",
        "Allemagne",
        "Italie",
        "Espagne",
        "Belgique",
        "Suisse",
        "Pays-Bas"
    ]

    categories = [
        "Informatique",
        "Maison",
        "Mode",
        "Sport",
        "Beaute",
        "Gaming",
        "Telephonie"
    ]

    lignes = []
    date_debut = datetime(2025, 1, 1)

    for i in range(1, nombre_lignes + 1):
        action = random.choices(
            actions,
            weights=[0.45, 0.25, 0.15, 0.08, 0.07],
            k=1
        )[0]

        page = random.choice(pages)

        id_utilisateur = f"UTIL{random.randint(1, 300):04d}"
        id_session = f"SESSION{random.randint(1, 600):05d}"

        horodatage = date_debut + timedelta(
            days=random.randint(0, 364),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )

        appareil = random.choice(appareils)
        pays_client = random.choice(pays)
        temps_reponse_ms = random.randint(80, 2500)

        code_statut = random.choices(
            [200, 404, 500],
            weights=[0.90, 0.07, 0.03],
            k=1
        )[0]

        categorie_produit = random.choice(categories)

        chiffre_affaires = 0.0

        if action == "achat" and code_statut == 200:
            chiffre_affaires = round(random.uniform(20, 500), 2)

        lignes.append({
            "IdLog": i,
            "IdUtilisateur": id_utilisateur,
            "IdSession": id_session,
            "Horodatage": horodatage.strftime("%Y-%m-%d %H:%M:%S"),
            "Page": page,
            "Action": action,
            "Appareil": appareil,
            "Pays": pays_client,
            "TempsReponseMs": temps_reponse_ms,
            "CodeStatut": code_statut,
            "CategorieProduit": categorie_produit,
            "ChiffreAffaires": chiffre_affaires
        })

    df = pd.DataFrame(lignes)

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)

    print("Fichier CSV généré avec succès.")
    print(f"Chemin : {DATA_PATH}")
    print(f"Nombre de lignes : {len(df)}")


if __name__ == "__main__":
    generate_web_logs(1000)