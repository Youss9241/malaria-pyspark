# Malaria PySpark

Classification d'images de cellules avec PySpark et Random Forest. Les résultats sont consultables dans Streamlit.

## Démarrage

1. Télécharger le dataset associé au [notebook Kaggle](https://www.kaggle.com/code/kushal1996/detecting-malaria-cnn/input).
2. Décompresser les images dans Google Drive, en conservant les dossiers Parasitized et Uninfected.
3. Ouvrir [01_exploration dans Colab](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/01_exploration.ipynb), adapter DATA_DIR et exécuter les cellules.
4. Ouvrir [02_training dans Colab](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/02_training.ipynb), adapter DATA_DIR et INVENTORY_DIR.
5. Renseigner PATIENT_MAP_CSV si les identifiants patients sont disponibles. Sinon, activer ALLOW_IMAGE_SPLIT : l'évaluation par image ne garantit pas la généralisation à de nouveaux patients.
6. Exécuter le notebook et télécharger dashboard_results.zip.
7. Décompresser le ZIP dans outputs à la racine du dépôt.

## Dashboard

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Le dashboard affiche la répartition des catégories, les scores, la matrice de confusion, l'importance des variables et les erreurs de classification.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| notebooks/01_exploration.ipynb | Lecture Spark, contrôle des images, doublons et inventaire Parquet |
| notebooks/02_training.ipynb | Variables RGB/LBP, séparation, entraînement et exports |
| app.py | Consultation des résultats |
| requirements.txt | Dépendances du dashboard |

## Travail restant

- Exécuter les notebooks sur le dataset et contrôler les sorties.
- Documenter la source, la licence et les éventuels identifiants patients.
- Comparer les résultats à la classe majoritaire.
- Examiner les erreurs et préparer la présentation.

Le code est disponible ; aucun entraînement sur le dataset n'a encore été vérifié. Le modèle utilise 40 caractéristiques de couleur et texture, avec 100 arbres et une profondeur maximale de 8. Le test est réservé à l'évaluation finale.

## Travail en groupe

Créer une branche par partie, puis une pull request. Éviter les modifications simultanées du même notebook. Les données, modèles et exports restent hors du dépôt.

Projet pédagogique, sans usage diagnostique.
