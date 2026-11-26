"""Dashboard des résultats exportés par notebooks/02_training.ipynb."""
import json
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Malaria · Résultats", page_icon="🔬", layout="wide")
st.title("Classification des cellules")
st.caption("Projet pédagogique · PySpark et Random Forest · Sans usage diagnostique")
folder = Path(st.sidebar.text_input("Dossier des exports", "outputs")).expanduser()
required = ["metrics.json", "predictions.csv", "confusion_matrix.csv",
            "class_counts.csv", "feature_importance.csv"]
missing = [name for name in required if not (folder / name).is_file()]
if missing:
    st.info("Exécutez les deux notebooks dans Colab, puis décompressez dashboard_results.zip dans le dossier outputs.")
    st.write("Fichiers attendus :", ", ".join(missing))
    st.link_button("Ouvrir le notebook d'entraînement", "https://colab.research.google.com/github/Youss9241/malaria-pyspark/blob/main/notebooks/02_training.ipynb")
    st.stop()

try:
    metrics = json.loads((folder / "metrics.json").read_text(encoding="utf-8"))
    predictions = pd.read_csv(folder / "predictions.csv")
    matrix = pd.read_csv(folder / "confusion_matrix.csv", index_col=0)
    counts = pd.read_csv(folder / "class_counts.csv")
    importance = pd.read_csv(folder / "feature_importance.csv")
    needed = {"category", "predicted_category", "probability_parasitized"}
    if not needed.issubset(predictions.columns):
        raise ValueError("Colonnes manquantes dans predictions.csv")
    for key in ["accuracy", "precision_parasitized", "recall_parasitized", "f1_parasitized"]:
        if not 0 <= float(metrics[key]) <= 1:
            raise ValueError(f"Métrique invalide : {key}")
except (OSError, ValueError, KeyError) as exc:
    st.error(f"Impossible de lire les exports : {exc}")
    st.stop()

st.sidebar.write("Séparation :", metrics.get("split_method", "Non renseignée"))
st.sidebar.write("Exécution UTC :", metrics.get("created_at_utc", "Non renseignée"))
if metrics.get("split_method", "").startswith("image_hash"):
    st.warning("Séparation par image : des cellules d'un même patient peuvent être présentes dans les deux ensembles. Ces scores ne mesurent pas une généralisation à de nouveaux patients.")
cols = st.columns(4)
for col, (label, key) in zip(cols, [
    ("Accuracy", "accuracy"), ("Précision · infectées", "precision_parasitized"),
    ("Rappel · infectées", "recall_parasitized"), ("F1 · infectées", "f1_parasitized")
]):
    col.metric(label, f"{metrics[key]:.1%}")
st.write(f"Entraînement : {metrics.get('n_train', '?')} images · Test : {metrics.get('n_test', '?')} images")
baseline = metrics.get("majority_baseline_accuracy")
if baseline is not None:
    st.caption(f"Référence : prédire toujours la classe majoritaire de l'entraînement donne {baseline:.1%} sur ce test.")

data_tab, model_tab, error_tab = st.tabs(["Données", "Évaluation", "Prédictions"])
with data_tab:
    st.subheader("Répartition de l'inventaire après nettoyage")
    st.bar_chart(counts.set_index("category")["count"])
    st.dataframe(counts, hide_index=True)
with model_tab:
    st.subheader("Matrice de confusion")
    st.caption("Lignes : catégorie réelle · Colonnes : catégorie prédite")
    st.dataframe(matrix)
    st.subheader("Variables les plus utilisées par le modèle")
    st.bar_chart(importance.nlargest(12, "importance").set_index("feature")["importance"])
    st.caption("L'importance d'une variable ne démontre pas une relation causale.")
    with st.expander("Paramètres et métriques de l'exécution"):
        st.json(metrics)
with error_tab:
    category = st.selectbox("Catégorie réelle", ["Toutes", "Parasitized", "Uninfected"])
    errors_only = st.checkbox("Afficher uniquement les erreurs", value=True)
    view = predictions
    if category != "Toutes":
        view = view[view["category"] == category]
    if errors_only:
        view = view[view["category"] != view["predicted_category"]]
    st.write(f"{len(view)} prédictions sélectionnées")
    st.dataframe(view.head(500), hide_index=True)
    st.caption("Table limitée à 500 lignes. Les chemins désignent les images dans l'environnement Colab ; les images ne sont pas incluses dans l'export.")
    st.download_button("Télécharger la sélection CSV", view.to_csv(index=False),
                       file_name="predictions_selection.csv", mime="text/csv")
