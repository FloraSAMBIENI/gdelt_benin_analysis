import os
import pandas as pd
from openai import AzureOpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les infos depuis .env
api_key = os.getenv("AZURE_OPENAI_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
model_name = os.getenv("AZURE_OPENAI_MODEL")

# Initialiser le client Azure OpenAI
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint
)

# Fonction pour générer un prompt basé sur un DataFrame
def generer_prompt(df):
    text = df.to_string(index=False)
    prompt = (
        "Voici des données mensuelles sur le nombre d'événements au Bénin extraites de GDELT :\n\n"
        f"{text}\n\n"
        "Analyse les tendances dans ces données. Identifie les mois avec un pic d'événements, "
        "les baisses, et propose des hypothèses ou interprétations possibles."
    )
    return prompt

# Fonction d'appel à l'API
def call_openai_api(prompt):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur : {e}"

# Point d'entrée
if __name__ == "__main__":
    # Charger le fichier CSV
    chemin_csv = "outputs/tendances_benin.csv"
    if os.path.exists(chemin_csv):
        df = pd.read_csv(chemin_csv)
        prompt = generer_prompt(df)
        resultat = call_openai_api(prompt)
        print("\n🧠 Analyse générée par Azure OpenAI :\n")
        print(resultat)
    else:
        print(f"Fichier non trouvé : {chemin_csv}")



# Créer un dossier s'il n'existe pas

os.makedirs("outputs/openai_responses", exist_ok=True)

# Enregistrer dans un fichier texte
with open("outputs/openai_responses/analyse_tendances.txt", "w", encoding="utf-8") as f:
    f.write(resultat)

print("✅ Résultat sauvegardé dans outputs/openai_responses/analyse_tendances.txt")

