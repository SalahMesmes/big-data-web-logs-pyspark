# Explication du projet : Big Data Web Logs avec PySpark

## Présentation du projet

Ce projet s’appelle **big-data-web-logs-pyspark**.

C’est un projet d’analyse de données orienté **Big Data**. Le but est d’analyser des logs web provenant d’un site e-commerce fictif.

Un **log web**, c’est une ligne de données qui représente une action réalisée par un utilisateur sur un site internet.

Exemples :

```text
un utilisateur visite la page d’accueil
un utilisateur clique sur un produit
un utilisateur ajoute un produit au panier
un utilisateur passe une commande
un utilisateur effectue un achat
```

Dans ce projet, toutes ces actions sont stockées dans un fichier CSV :

```text
data/logs_web_fr.csv
```

Chaque ligne du fichier représente une action utilisateur.

---

## Objectif du projet

L’objectif du projet est de comprendre le comportement des utilisateurs sur un site e-commerce.

Le projet permet de répondre à plusieurs questions :

```text
Combien de visites le site a reçues ?
Combien d’utilisateurs différents sont venus sur le site ?
Quelles pages sont les plus visitées ?
Quelles actions sont les plus fréquentes ?
Quels pays génèrent le plus de chiffre d’affaires ?
Quelles catégories de produits rapportent le plus ?
Quelles pages sont les plus lentes ?
Combien d’erreurs HTTP le site rencontre ?
Depuis quels appareils les utilisateurs visitent le site ?
```

Ce projet permet donc de transformer un fichier de logs brut en indicateurs clairs et exploitables.

---

## Technologies utilisées

### Python

Python est le langage principal du projet. Il est utilisé pour générer les données, lancer l’analyse, exporter les résultats et créer le dashboard.

### PySpark

PySpark est la technologie principale du projet. PySpark permet d’utiliser **Apache Spark avec Python**.

Spark est un outil utilisé dans le Big Data pour traiter de gros volumes de données.

Dans ce projet, PySpark est utilisé pour :

```text
charger le fichier CSV
nettoyer les données
faire des regroupements
calculer des indicateurs
exporter les résultats
```

Le fichier principal qui utilise PySpark est :

```text
src/spark_analysis.py
```

### Apache Spark

Apache Spark est le moteur de calcul utilisé derrière PySpark. Il permet de traiter des données plus efficacement qu’un traitement classique lorsque les volumes deviennent importants.

Dans ce projet, Spark tourne en local sur l’ordinateur avec :

```python
.master("local[*]")
```

Cela signifie que Spark utilise les ressources disponibles sur la machine.

Même si le fichier contient seulement 1000 lignes, l’intérêt est de montrer la logique d’un traitement Big Data.

### Java

Spark fonctionne avec Java en arrière-plan. Même si le code est écrit en Python, Spark utilise la JVM.

Pour vérifier la version de Java :

```bash
java -version
```

Il est conseillé d’utiliser Java 17 pour éviter les problèmes de compatibilité avec PySpark.

### Pandas

Pandas est utilisé pour lire les fichiers CSV exportés par PySpark.

Dans ce projet, Pandas est surtout utilisé dans :

```text
src/export_results.py
app/dashboard.py
```

PySpark fait l’analyse principale, puis Pandas lit les résultats pour les afficher dans le terminal ou dans le dashboard.

### Matplotlib

Matplotlib sert à créer les graphiques dans le dashboard.

Il est utilisé pour afficher :

```text
les pages les plus visitées
les actions les plus fréquentes
le chiffre d’affaires par pays
le chiffre d’affaires par catégorie
les visites par appareil
```

### Streamlit

Streamlit permet de créer une interface web simple et interactive.

Dans ce projet, Streamlit est utilisé dans :

```text
app/dashboard.py
```

Il permet d’afficher les résultats sous forme de métriques, graphiques et tableaux.

### CSV

Le format CSV est utilisé pour stocker les données.

Le fichier de départ est :

```text
data/logs_web_fr.csv
```

Les résultats générés par PySpark sont aussi exportés en CSV dans le dossier :

```text
output/
```

---

## Structure du projet

```text
big-data-web-logs-pyspark/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── logs_web_fr.csv
│
├── output/
│   ├── total_visites.csv
│   ├── utilisateurs_uniques.csv
│   ├── pages_plus_visitees.csv
│   ├── actions_frequentes.csv
│   ├── chiffre_affaires_par_pays.csv
│   ├── chiffre_affaires_par_categorie.csv
│   ├── temps_reponse_moyen.csv
│   ├── codes_statut.csv
│   └── visites_par_appareil.csv
│
├── src/
│   ├── generate_data.py
│   ├── spark_analysis.py
│   └── export_results.py
│
└── app/
    └── dashboard.py
```

---

## Rôle des dossiers

### `data/`

Le dossier `data` contient les données de départ.

Dans ce projet, il contient :

```text
logs_web_fr.csv
```

Ce fichier contient les logs web à analyser.

### `src/`

Le dossier `src` contient le code principal du projet.

Il contient :

```text
generate_data.py
spark_analysis.py
export_results.py
```

### `output/`

Le dossier `output` contient les résultats générés par PySpark.

Chaque fichier CSV correspond à une analyse précise.

Exemples :

```text
total_visites.csv
pages_plus_visitees.csv
chiffre_affaires_par_pays.csv
codes_statut.csv
```

### `app/`

Le dossier `app` contient l’application Streamlit.

Le fichier principal est :

```text
dashboard.py
```

C’est ce fichier qui affiche les indicateurs, les graphiques et les tableaux.

---

## Rôle des fichiers

### `requirements.txt`

Ce fichier contient les dépendances nécessaires au projet.

Exemple :

```text
pyspark
pandas
streamlit
matplotlib
```

Pour installer les dépendances :

```bash
python3 -m pip install -r requirements.txt
```

### `data/logs_web_fr.csv`

Ce fichier contient les logs web.

Chaque ligne représente une action utilisateur sur le site.

Les colonnes principales sont :

```text
IdLog
IdUtilisateur
IdSession
Horodatage
Page
Action
Appareil
Pays
TempsReponseMs
CodeStatut
CategorieProduit
ChiffreAffaires
```

---

## Description des colonnes du dataset

| Colonne | Description |
|---|---|
| `IdLog` | Identifiant unique du log |
| `IdUtilisateur` | Identifiant de l’utilisateur |
| `IdSession` | Identifiant de la session |
| `Horodatage` | Date et heure de l’action |
| `Page` | Page visitée |
| `Action` | Action réalisée par l’utilisateur |
| `Appareil` | Type d’appareil utilisé |
| `Pays` | Pays de l’utilisateur |
| `TempsReponseMs` | Temps de réponse de la page en millisecondes |
| `CodeStatut` | Code HTTP de la requête |
| `CategorieProduit` | Catégorie du produit |
| `ChiffreAffaires` | Montant généré par l’action |

---

## Exemples d’actions

Le fichier contient plusieurs types d’actions :

```text
voir_page
cliquer_produit
ajouter_panier
passer_commande
achat
```

Ces actions permettent d’analyser le parcours utilisateur.

Par exemple :

```text
voir_page = l’utilisateur consulte une page
cliquer_produit = l’utilisateur clique sur un produit
ajouter_panier = l’utilisateur ajoute un produit au panier
passer_commande = l’utilisateur commence une commande
achat = l’utilisateur réalise un achat
```

---

## Exemples de codes HTTP

Le projet analyse aussi les codes HTTP.

Exemples :

```text
200 = succès
404 = page introuvable
500 = erreur serveur
```

Cela permet d’avoir une première analyse technique du site.

---

## Fonctionnement général du projet

Le projet fonctionne en plusieurs étapes :

```text
1. Génération ou ajout du fichier CSV
2. Chargement des données avec PySpark
3. Nettoyage des données
4. Calcul des indicateurs
5. Export des résultats en CSV
6. Affichage des résultats dans Streamlit
```

---

## Étape 1 : génération ou ajout des données

Le fichier de données se trouve dans :

```text
data/logs_web_fr.csv
```

Il peut être ajouté directement ou généré avec le fichier :

```text
src/generate_data.py
```

Commande pour générer les données :

```bash
python3 src/generate_data.py
```

Cette commande crée un fichier CSV de 1000 lignes contenant des logs web fictifs.

---

## Étape 2 : chargement avec PySpark

Le fichier principal de l’analyse est :

```text
src/spark_analysis.py
```

Dans ce fichier, on crée d’abord une session Spark.

La session Spark permet de lancer un traitement avec PySpark.

Ensuite, le fichier CSV est chargé avec Spark :

```python
spark.read.option("header", True).option("inferSchema", True).csv(...)
```

Cette commande permet de lire le fichier CSV et de le transformer en DataFrame Spark.

Un DataFrame Spark ressemble à un tableau de données, mais il est conçu pour traiter de gros volumes.

---

## Étape 3 : nettoyage des données

Avant de faire les analyses, le projet nettoie les données.

Le nettoyage consiste à :

```text
supprimer les valeurs vides
garder uniquement les temps de réponse positifs
garder uniquement les chiffres d’affaires positifs ou égaux à 0
```

Cette étape est importante, car des données incorrectes peuvent fausser les résultats.

---

## Étape 4 : calcul des indicateurs

Après le nettoyage, PySpark calcule plusieurs indicateurs.

Les calculs utilisent des fonctions Spark comme :

```text
groupBy
count
sum
avg
countDistinct
orderBy
```

Ces fonctions permettent de regrouper les données et de produire des résultats utiles.

---

## Indicateurs calculés

### Nombre total de visites

Cet indicateur compte toutes les lignes du fichier.

Il permet de connaître le volume global d’activité du site.

Résultat exporté dans :

```text
output/total_visites.csv
```

### Nombre d’utilisateurs uniques

Cet indicateur compte le nombre d’utilisateurs différents.

Cela permet de savoir combien de personnes différentes ont visité le site.

Résultat exporté dans :

```text
output/utilisateurs_uniques.csv
```

### Pages les plus visitées

Cette analyse permet d’identifier les pages les plus consultées.

Exemples de pages :

```text
/accueil
/produits
/details-produit
/panier
/paiement
```

Résultat exporté dans :

```text
output/pages_plus_visitees.csv
```

### Actions les plus fréquentes

Cette analyse montre les actions les plus réalisées par les utilisateurs.

Exemples :

```text
voir_page
cliquer_produit
ajouter_panier
achat
```

Résultat exporté dans :

```text
output/actions_frequentes.csv
```

### Chiffre d’affaires par pays

Cette analyse permet de voir quels pays génèrent le plus de chiffre d’affaires.

Résultat exporté dans :

```text
output/chiffre_affaires_par_pays.csv
```

### Chiffre d’affaires par catégorie

Cette analyse permet de voir quelles catégories de produits rapportent le plus.

Exemples :

```text
Informatique
Maison
Mode
Sport
Gaming
Telephonie
```

Résultat exporté dans :

```text
output/chiffre_affaires_par_categorie.csv
```

### Temps de réponse moyen par page

Cette analyse permet de mesurer la performance technique du site.

Elle calcule le temps de réponse moyen pour chaque page.

Une page avec un temps de réponse élevé peut indiquer un problème de performance.

Résultat exporté dans :

```text
output/temps_reponse_moyen.csv
```

### Répartition des codes HTTP

Cette analyse permet de voir les réponses serveur.

Exemples :

```text
200 = succès
404 = page introuvable
500 = erreur serveur
```

Cela permet d’identifier s’il y a beaucoup d’erreurs techniques.

Résultat exporté dans :

```text
output/codes_statut.csv
```

### Visites par appareil

Cette analyse montre depuis quel appareil les utilisateurs consultent le site.

Exemples :

```text
ordinateur
mobile
tablette
```

Résultat exporté dans :

```text
output/visites_par_appareil.csv
```

---

## Étape 5 : export des résultats

Après les calculs, les résultats sont exportés dans le dossier :

```text
output/
```

Chaque analyse produit un fichier CSV.

Exemples :

```text
total_visites.csv
utilisateurs_uniques.csv
pages_plus_visitees.csv
actions_frequentes.csv
chiffre_affaires_par_pays.csv
chiffre_affaires_par_categorie.csv
temps_reponse_moyen.csv
codes_statut.csv
visites_par_appareil.csv
```

Ces fichiers sont ensuite utilisés par le dashboard Streamlit.

---

## Étape 6 : affichage avec Streamlit

Le fichier :

```text
app/dashboard.py
```

crée une interface web avec Streamlit.

Le dashboard lit les fichiers CSV du dossier `output/` et affiche les résultats sous forme claire.

Il affiche :

```text
des métriques principales
des graphiques
des tableaux
```

Pour lancer le dashboard :

```bash
python3 -m streamlit run app/dashboard.py
```

---

## Chaîne complète du projet

Voici la chaîne complète du traitement :

```text
logs_web_fr.csv
        ↓
chargement avec PySpark
        ↓
nettoyage des données
        ↓
calcul des indicateurs
        ↓
export des résultats dans output/
        ↓
lecture des résultats avec Pandas
        ↓
affichage dans Streamlit
```

---

## Comment lancer le projet

### 1. Créer un environnement virtuel

```bash
python3 -m venv venv
```

### 2. Activer l’environnement virtuel

Sur macOS ou Linux :

```bash
source venv/bin/activate
```

Sur Windows :

```bash
venv\\Scripts\\activate
```

### 3. Installer les dépendances

```bash
python3 -m pip install -r requirements.txt
```

### 4. Vérifier Java

PySpark a besoin de Java pour fonctionner.

```bash
java -version
```

Il est recommandé d’utiliser Java 17.

### 5. Générer les données

Cette étape est optionnelle si le fichier `data/logs_web_fr.csv` existe déjà.

```bash
python3 src/generate_data.py
```

### 6. Lancer l’analyse PySpark

```bash
python3 src/spark_analysis.py
```

Cette commande génère les fichiers de résultats dans le dossier `output/`.

### 7. Afficher les résultats dans le terminal

Cette étape est optionnelle.

```bash
python3 src/export_results.py
```

### 8. Lancer le dashboard

```bash
python3 -m streamlit run app/dashboard.py
```

Une page s’ouvre ensuite dans le navigateur.

---

## Pourquoi ce projet est intéressant ?

Ce projet est intéressant, car il montre une première approche du Big Data.

Il montre que je sais :

```text
charger un fichier CSV
nettoyer des données
utiliser PySpark
faire des agrégations
calculer des indicateurs
exporter des résultats
créer un dashboard
visualiser des données
organiser un projet Python
```

Il montre aussi une chaîne complète de traitement de données :

```text
données brutes → analyse → résultats → visualisation
```

---

## Ce que ce projet montre à un recruteur

Ce projet montre que je ne travaille pas seulement avec Pandas ou du Python classique.

Il montre que j’ai découvert un outil utilisé dans le Big Data : **PySpark**.

Il montre aussi que je comprends les bases de l’analyse de logs web, qui est un cas proche de ce qu’on peut rencontrer en entreprise.

Le projet met en avant des compétences en :

```text
Python
Big Data
PySpark
analyse de données
data engineering
visualisation
dashboard
```

---

## Résumé 

Ce projet analyse les actions des utilisateurs sur un site e-commerce.

Le fichier CSV contient des logs web.

PySpark lit ce fichier, nettoie les données et calcule des indicateurs.

Les résultats sont exportés dans des fichiers CSV.

Streamlit affiche ensuite ces résultats dans un dashboard.

