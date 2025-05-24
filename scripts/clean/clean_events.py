import pandas as pd
import os

# Créer le dossier cleaned_data s'il n'existe pas
os.makedirs('cleaned_data', exist_ok=True)

# Charger les données
events_path = 'data/benin_events.csv'
df = pd.read_csv(events_path)

# Supprimer les lignes complètement vides
df.dropna(how='all', inplace=True)

# Supprimer les doublons éventuels
df.drop_duplicates(inplace=True)

# Conversion de la colonne SQLDATE
if 'SQLDATE' in df.columns:
    df['SQLDATE'] = pd.to_datetime(df['SQLDATE'], errors='coerce', format='%Y%m%d')

# Conversion de la colonne MonthYear (format: YYYYMM)
if 'MonthYear' in df.columns:
    df['MonthYear'] = pd.to_datetime(df['MonthYear'], errors='coerce', format='%Y%m')

# Conversion de la colonne Year (format: YYYY)
if 'Year' in df.columns:
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce', format='%Y')


df.info()

# Enregistrer le résultat
df.to_csv('cleaned_data/clean_events.csv', index=False)
print("✅ Nettoyage de benin_events terminé.")

