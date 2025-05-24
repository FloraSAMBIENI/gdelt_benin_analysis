import pandas as pd
import os

os.makedirs('cleaned_data', exist_ok=True)

# Charger les données
mentions_path = 'data/benin_mentions.csv'
df = pd.read_csv(mentions_path)

# Supprimer les lignes vides
df.dropna(how='all', inplace=True)

# Supprimer les doublons
df.drop_duplicates(inplace=True)

# Convertir DATE si présente
if 'MentionTimeDate' in df.columns:
    df['MentionTimeDate'] = pd.to_datetime(df['MentionTimeDate'], errors='coerce', format='%Y%m%d%H%M%S')

if 'EventTimeDate' in df.columns:
    df['EventTimeDate'] = pd.to_datetime(df['EventTimeDate'], errors='coerce', format='%Y%m%d%H%M%S')


df.info()

# Enregistrer
df.to_csv('cleaned_data/clean_mentions.csv', index=False)
print("✅ Nettoyage de benin_mentions terminé.")
