import os
import pandas as pd
from openai import AzureOpenAI
from dotenv import load_dotenv

# 1. Charger les variables d'environnement
load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL")

# 2. Fonction pour appeler l’API Azure OpenAI
def call_openai_api(prompt):
    client = AzureOpenAI(
        api_key=API_KEY,
        api_version=API_VERSION,
        azure_endpoint=ENDPOINT
    )
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur : {e}"

# 3. Lire le fichier CSV des événements majeurs
df_events = pd.read_csv("outputs/evenements_majeurs.csv")

# 4. Transformer tout le DataFrame en texte
texte_evenements = df_events.to_string(index=False)

# 5. Construire le prompt
prompt = f"""Voici des événements majeurs survenus au Bénin selon les données de GDELT.
Analyse ces événements et donne un résumé clair de ce que ces données indiquent :
{texte_evenements}
"""

# 6. Appel à l’API et récupération de l’analyse
analyse = call_openai_api(prompt)

# 7. Enregistrement du résultat dans un fichier texte
with open("outputs/openai_responses/analyse_evenements_majeurs.txt", "w", encoding="utf-8") as f:
    f.write(analyse)

print("✅ Analyse enregistrée dans outputs/openai_responses/analyse_evenements_majeurs.txt")
