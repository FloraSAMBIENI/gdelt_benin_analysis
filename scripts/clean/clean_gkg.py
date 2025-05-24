import pandas as pd
import os

os.makedirs('cleaned_data', exist_ok=True)

# Charger les données
gkg_path = 'data/benin_gkg.csv'
df = pd.read_csv(gkg_path)

# Supprimer les lignes vides
df.dropna(how='all', inplace=True)

# Supprimer les doublons
df.drop_duplicates(inplace=True)

# Convertir DATE si présente
if 'DATE' in df.columns:
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce', format='%Y%m%d%H%M%S')

df.info()

# Enregistrer
df.to_csv('cleaned_data/clean_gkg.csv', index=False)
print("✅ Nettoyage de benin_gkg terminé.")
