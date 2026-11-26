# Malaria Detection — Apache Spark

## 1. Présentation du projet

L'objectif est de classer des images microscopiques de cellules sanguines en deux catégories : infectées et non infectées. Apache Spark assure la lecture et la préparation des données, puis MLlib est utilisé pour entraîner un modèle de classification.

## 2. Dataset

Le jeu de données retenu est [Cell Images for Detecting Malaria](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria), disponible sur Kaggle.

Les images sont réparties dans deux dossiers :

| Dossier | Description | Label du modèle |
| --- | --- | --- |
| Parasitized | Cellules infectées | 1 |
| Uninfected | Cellules non infectées | 0 |

Le nombre d'images exploitées sera relevé lors de l'exécution, avant et après nettoyage. Les données sont téléchargées séparément et ne sont pas stockées dans ce dépôt.

## 3. Technologies

- Python et PySpark : lecture et traitement.
- Pillow, NumPy et scikit-image : caractéristiques des images.
- Spark MLlib : pipeline et Random Forest.
- Scikit-learn : calcul des métriques d'évaluation.
- Pandas et Streamlit : consultation des exports.

## 4. Pipeline

### Étape 1 — Lire les données

Création de la SparkSession et chargement des images avec la source binaryFile. Chaque ligne contient le chemin, le contenu du fichier et sa catégorie.

### Étape 2 — Transformer les données

Identification de la catégorie avec withColumn, comptage avec groupBy et filtrage des fichiers non reconnus. Une UDF vérifie les dimensions et la lisibilité. Un hash permet de repérer les fichiers strictement identiques.

### Étape 3 — Préparer les variables

Les images sont redimensionnées en 64 × 64 pixels. L'extraction produit 40 variables : moyennes et écarts-types RGB, histogrammes de couleur et texture LBP.

StringIndexer encode les catégories. VectorAssembler rassemble les variables dans un vecteur. Ces étapes sont intégrées au Pipeline MLlib.

### Étape 4 — Entraîner et évaluer

Un Random Forest de 100 arbres, avec une profondeur maximale de 8, est ajusté sur l'entraînement. La séparation vise environ 80 % d'entraînement et 20 % de test.

La séparation est effectuée par patient lorsque des identifiants vérifiés sont disponibles. Sinon, une séparation par hash d'image peut être activée, avec une limite de généralisation à documenter.

L'évaluation comprend l'accuracy, la précision, le rappel, le F1-score, l'AUC et la matrice de confusion. La cellule infectée est la classe positive. Une prédiction constante de la classe majoritaire sert de référence.

### Étape 5 — Écrire les résultats

Le modèle est sauvegardé, les prédictions sont exportées en Parquet et CSV, et les métriques en JSON. Chaque exécution utilise un dossier daté. Les exports existants ne sont pas écrasés.

### Étape 6 — Visualiser

Le dashboard Streamlit lit les exports et affiche la répartition des catégories, les métriques, la matrice de confusion, l'importance des variables et les erreurs. Les prédictions peuvent être filtrées par catégorie.

## 5. Organisation du dépôt

| Fichier | Rôle |
| --- | --- |
| notebooks/01_exploration.ipynb | Chargement, contrôle et inventaire des images |
| notebooks/02_training.ipynb | Variables, entraînement, évaluation et exports |
| app.py | Dashboard Streamlit |
| requirements.txt | Dépendances du dashboard |

## 6. Exécution

1. Télécharger et décompresser le dataset dans Google Drive.
2. Ouvrir [01_exploration dans Colab](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/01_exploration.ipynb), adapter DATA_DIR et exécuter les cellules.
3. Ouvrir [02_training dans Colab](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/02_training.ipynb), adapter DATA_DIR et INVENTORY_DIR.
4. Renseigner PATIENT_MAP_CSV avec les colonnes path,patient_id, ou activer ALLOW_IMAGE_SPLIT si ces identifiants sont indisponibles.
5. Exécuter les cellules et télécharger dashboard_results.zip.
6. Décompresser les exports dans un dossier outputs à la racine du dépôt.

Pour lancer le dashboard :

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 7. Avancement et limites

Les notebooks et le dashboard sont écrits. L'exécution complète sur le dataset et la vérification des résultats restent à effectuer. Aucun score n'est encore disponible.

Une séparation par image peut placer des cellules d'un même patient dans l'entraînement et le test. Elle ne permet donc pas, à elle seule, de mesurer les performances sur de nouveaux patients.

Le projet est réalisé dans un cadre pédagogique et expérimental. Il ne constitue pas un outil médical de diagnostic.
