import pandas as pd
import os

from analyse_tendances import analyser_tendances
from analyse_evenements_maj import extraire_evenements_majeurs
from analyse_sentiments import analyser_sentiments
from analyse_mentions import analyser_mentions
from analyse_localisation import analyser_localisation


# Créer le dossier de sortie s'il n'existe pas
os.makedirs('outputs', exist_ok=True)

# Charger les datasets nettoyés
events_df = pd.read_csv('cleaned_data/clean_events.csv', parse_dates=['SQLDATE'])
gkg_df = pd.read_csv('cleaned_data/clean_gkg.csv')
mentions_df = pd.read_csv('cleaned_data/clean_mentions.csv')

# ANALYSES
tendances_df = analyser_tendances(events_df)
tendances_df.to_csv('outputs/tendances_benin.csv', index=False)

evenements_df = extraire_evenements_majeurs(events_df)
evenements_df.to_csv('outputs/evenements_majeurs.csv', index=False)

sentiments_df = analyser_sentiments(mentions_df)
sentiments_df.to_csv('outputs/sentiments_benin.csv', index=False)

mentions_stats_df = analyser_mentions(mentions_df)
mentions_stats_df.to_csv('outputs/mentions_benin.csv', index=False)

localisation_df = analyser_localisation(gkg_df)
localisation_df.to_csv("outputs/localisation_benin.csv", index=False)

print("✅ Toutes les analyses ont été exécutées et sauvegardées dans le dossier outputs/")
