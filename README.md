# Malaria — pipeline PySpark

Projet de classification d'images de cellules : préparation avec PySpark, entraînement d'un modèle puis visualisation avec Streamlit.

## État actuel

Un premier notebook charge les images, identifie leur catégorie, contrôle leur lisibilité et leurs dimensions, détecte les fichiers identiques et exporte un inventaire Parquet. Il doit encore être exécuté avec le dataset. Aucun score de modèle n'est disponible à ce stade.

## Démarrer dans Google Colab

1. Ouvrir [le notebook dans Colab](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/01_exploration.ipynb).
2. Enregistrer une copie dans son Drive pour conserver les modifications et sorties.
3. Télécharger et décompresser le dataset associé au [notebook Kaggle de référence](https://www.kaggle.com/code/kushal1996/detecting-malaria-cnn/input).
4. Placer les dossiers `Parasitized` et `Uninfected` dans Google Drive.
5. Adapter `DATA_DIR` dans le notebook, puis exécuter les cellules dans l'ordre.
6. Adapter `OUTPUT_DIR` pour l'export. Un export existant n'est pas écrasé automatiquement.

Les images et les exports volumineux ne doivent pas être ajoutés au dépôt. Documenter la source et la licence du dataset avant de diffuser ses données.

## Étapes à réaliser

- [x] Première version du notebook de lecture et de contrôle.
- [ ] Exécuter le notebook sur les données et vérifier les sorties.
- [ ] Documenter le dataset et ses limites.
- [ ] Extraire les caractéristiques de couleur et de texture.
- [ ] Préparer les ensembles entraînement/test, par patient si possible.
- [ ] Construire le pipeline MLlib et entraîner un premier modèle.
- [ ] Évaluer et exporter les métriques et prédictions.
- [ ] Créer le dashboard Streamlit.
- [ ] Préparer la présentation et les instructions de reproduction.

Le choix d'un CNN reste à confirmer avec les consignes du cours. La première version vise un pipeline PySpark/MLlib.

## Travailler en groupe

Chacun travaille sur une branche et propose ses changements par pull request. Éviter de modifier simultanément le même notebook. Avant chaque modification, récupérer la dernière version du dépôt.

Répartition proposée : données et qualité ; extraction des variables ; modèle et évaluation ; dashboard et documentation. Chaque membre doit pouvoir expliquer ses choix et reproduire les résultats.

## Limites

Projet pédagogique, sans usage diagnostique. Les performances ne seront annoncées qu'après exécution et évaluation. Des images d'un même patient dans les ensembles d'entraînement et de test pourraient surestimer les performances : vérifier les identifiants disponibles et documenter toute limite.
