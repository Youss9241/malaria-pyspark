# Malaria — pipeline PySpark

Projet de classification d'images de cellules : préparation avec PySpark, entraînement d'un modèle puis visualisation avec Streamlit.

## État actuel

Le notebook `02_training.ipynb` et le dashboard `app.py` sont maintenant disponibles. Ils doivent être exécutés avec les données pour produire de vrais résultats.

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

## Entraîner le modèle

Après l'exploration, ouvrir [02_training.ipynb dans Colab](https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/02_training.ipynb).

1. Enregistrer une copie dans Drive et exécuter l'installation.
2. Adapter DATA_DIR et INVENTORY_DIR.
3. Fournir si possible un CSV path,patient_id via PATIENT_MAP_CSV. Le chemin doit correspondre exactement au chemin Spark de l'inventaire.
4. Si ces identifiants sont indisponibles, activer ALLOW_IMAGE_SPLIT et documenter la limite.
5. Exécuter dans l'ordre : caractéristiques RGB/LBP, séparation déterministe, pipeline MLlib, évaluation et exports.
6. Télécharger dashboard_results.zip à la fin.

Le notebook fixe les paramètres avant le test. Pour comparer d'autres paramètres, réserver une validation distincte au sein de l'entraînement ; ne pas choisir les paramètres sur le test.

## Lancer le dashboard sur le PC

Dans le dossier du dépôt :

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Décompresser les fichiers de dashboard_results.zip dans un dossier outputs à la racine du dépôt. Le dashboard affiche une instruction d'attente tant que ces exports ne sont pas présents. Il ne contient aucun score de démonstration.

## État de cette deuxième version

Le code de préparation, entraînement, export et visualisation est fourni. La checklist ci-dessus décrit les étapes à valider sur les vraies données : elle ne signifie pas que le modèle a déjà été entraîné. Les notebooks sont prévus pour Colab ; le dashboard ne nécessite pas Spark sur le PC.
