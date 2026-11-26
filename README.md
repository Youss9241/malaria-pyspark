# Classification de cellules — PySpark

## Objectif

Classer des images de cellules dans deux catégories : `Parasitized` (infectées) et `Uninfected` (non infectées). Le projet suit un pipeline de traitement avec PySpark, d'entraînement avec MLlib et de visualisation avec Streamlit.

Point de départ : [notebook Kaggle](https://www.kaggle.com/code/kushal1996/detecting-malaria-cnn/input). Le dataset associé doit être téléchargé séparément.

## Méthode

1. Charger les images avec Spark et identifier leur catégorie à partir du dossier.
2. Contrôler les fichiers illisibles, les dimensions et les doublons.
3. Extraire 40 variables : moyennes et écarts-types RGB, histogrammes de couleur et texture LBP.
4. Séparer les données d'entraînement et de test.
5. Entraîner un Random Forest de 100 arbres, avec une profondeur maximale de 8.
6. Calculer l'accuracy, la précision, le rappel, le F1-score et l'AUC.
7. Exporter les résultats et les consulter dans Streamlit.

La classe infectée est la classe positive pour le calcul de la précision, du rappel et du F1-score.

## Organisation

| Fichier | Contenu |
| --- | --- |
| `notebooks/01_exploration.ipynb` | Lecture, nettoyage et inventaire Parquet |
| `notebooks/02_training.ipynb` | Extraction des variables, entraînement et évaluation |
| `app.py` | Dashboard des résultats |
| `requirements.txt` | Dépendances du dashboard |

## Exécution

### Notebooks dans Google Colab

1. Décompresser les images dans Google Drive en conservant les dossiers `Parasitized` et `Uninfected`.
2. Ouvrir [01_exploration](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/01_exploration.ipynb), adapter `DATA_DIR`, puis exécuter les cellules.
3. Ouvrir [02_training](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/02_training.ipynb) et adapter `DATA_DIR` et `INVENTORY_DIR`.
4. Renseigner `PATIENT_MAP_CSV` avec un CSV contenant `path,patient_id` si les identifiants patients sont disponibles. Sinon, activer `ALLOW_IMAGE_SPLIT`.
5. Exécuter les cellules, puis télécharger `dashboard_results.zip`.

### Dashboard en local

Décompresser les exports dans un dossier `outputs` à la racine du dépôt, puis lancer :

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Avancement

Les notebooks et le dashboard sont écrits. L'exécution complète sur le dataset et la validation des résultats restent à effectuer. Aucun score n'est encore présenté.

## Limites

Une séparation par image peut placer des cellules d'un même patient dans l'entraînement et le test. La séparation par patient est à privilégier lorsque les identifiants sont disponibles. Le test est réservé à l'évaluation finale.

Ce projet porte sur la classification d'images et ne constitue pas un outil de diagnostic médical.
