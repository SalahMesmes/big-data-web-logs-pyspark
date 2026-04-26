from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, countDistinct, desc, round, sum


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "logs_web_fr.csv"
OUTPUT_DIR = ROOT_DIR / "output"


def create_spark_session():
    """
    Création d'une session Spark locale.
    local[*] signifie que Spark utilise tous les cœurs disponibles sur la machine.
    """
    return (
        SparkSession.builder
        .appName("Analyse Big Data de logs web")
        .master("local[*]")
        .getOrCreate()
    )


def load_logs(spark):
    """
    Chargement du fichier CSV de logs web.
    """
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(DATA_PATH))
    )


def save_single_csv(spark_df, output_name: str):
    """
    Spark exporte normalement les résultats dans un dossier avec plusieurs fichiers.
    Cette fonction permet d'obtenir un seul fichier CSV propre.
    """
    temp_dir = OUTPUT_DIR / f"{output_name}_temp"
    final_file = OUTPUT_DIR / f"{output_name}.csv"

    spark_df.coalesce(1).write.mode("overwrite").option("header", True).csv(str(temp_dir))

    part_file = list(temp_dir.glob("part-*.csv"))[0]

    if final_file.exists():
        final_file.unlink()

    part_file.rename(final_file)

    for file in temp_dir.glob("*"):
        file.unlink()

    temp_dir.rmdir()


def run_analysis():
    spark = create_spark_session()
    df = load_logs(spark)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Nettoyage simple des données
    df = df.dropna()
    df = df.filter(col("TempsReponseMs") > 0)
    df = df.filter(col("ChiffreAffaires") >= 0)

    # KPI principaux
    total_visites = df.select(count("*").alias("TotalVisites"))

    utilisateurs_uniques = df.select(
        countDistinct("IdUtilisateur").alias("UtilisateursUniques")
    )

    pages_plus_visitees = (
        df.groupBy("Page")
        .agg(count("*").alias("NombreVisites"))
        .orderBy(desc("NombreVisites"))
    )

    actions_frequentes = (
        df.groupBy("Action")
        .agg(count("*").alias("NombreActions"))
        .orderBy(desc("NombreActions"))
    )

    chiffre_affaires_par_pays = (
        df.groupBy("Pays")
        .agg(round(sum("ChiffreAffaires"), 2).alias("ChiffreAffairesTotal"))
        .orderBy(desc("ChiffreAffairesTotal"))
    )

    chiffre_affaires_par_categorie = (
        df.groupBy("CategorieProduit")
        .agg(round(sum("ChiffreAffaires"), 2).alias("ChiffreAffairesTotal"))
        .orderBy(desc("ChiffreAffairesTotal"))
    )

    temps_reponse_moyen = (
        df.groupBy("Page")
        .agg(round(avg("TempsReponseMs"), 2).alias("TempsReponseMoyenMs"))
        .orderBy(desc("TempsReponseMoyenMs"))
    )

    codes_statut = (
        df.groupBy("CodeStatut")
        .agg(count("*").alias("Nombre"))
        .orderBy("CodeStatut")
    )

    visites_par_appareil = (
        df.groupBy("Appareil")
        .agg(count("*").alias("NombreVisites"))
        .orderBy(desc("NombreVisites"))
    )

    # Export des résultats
    save_single_csv(total_visites, "total_visites")
    save_single_csv(utilisateurs_uniques, "utilisateurs_uniques")
    save_single_csv(pages_plus_visitees, "pages_plus_visitees")
    save_single_csv(actions_frequentes, "actions_frequentes")
    save_single_csv(chiffre_affaires_par_pays, "chiffre_affaires_par_pays")
    save_single_csv(chiffre_affaires_par_categorie, "chiffre_affaires_par_categorie")
    save_single_csv(temps_reponse_moyen, "temps_reponse_moyen")
    save_single_csv(codes_statut, "codes_statut")
    save_single_csv(visites_par_appareil, "visites_par_appareil")

    print("Analyse PySpark terminée avec succès.")
    print(f"Résultats exportés dans : {OUTPUT_DIR}")

    spark.stop()


if __name__ == "__main__":
    run_analysis()