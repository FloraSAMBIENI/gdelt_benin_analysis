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
        "Voici les 100 lieux les plus mentionnés dans des articles liés au Bénin, extraits des données GKG de GDELT :\n\n"
        f"{text}\n\n"
        "Analyse ces données pour identifier les lieux les plus récurrents, expliquer pourquoi certains pays ou villes peuvent apparaître "
        "souvent, et propose des hypothèses sur les types d'articles ou événements qui peuvent être associés à ces lieux."
    )
    return prompt

# Fonction d'appel à l'API avec gestion du quota
def call_openai_api(prompt):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur : {e}"

# Point d’entrée
if __name__ == "__main__":
    chemin_csv = "outputs/localisation_benin.csv"
    if os.path.exists(chemin_csv):
        df = pd.read_csv(chemin_csv)

        # Sélectionner le top 100
        df_top100 = df.head(100)

        # Générer le prompt
        prompt = generer_prompt(df_top100)

        # Appel à l'API
        resultat = call_openai_api(prompt)

        # Créer le dossier de sortie s’il n’existe pas
        os.makedirs("outputs/openai_responses", exist_ok=True)

        # Enregistrer dans un fichier texte
        chemin_resultat = "outputs/openai_responses/analyse_localisation.txt"
        with open(chemin_resultat, "w", encoding="utf-8") as f:
            f.write(resultat)

        print("✅ Résultat sauvegardé dans", chemin_resultat)
    else:
        print(f"❌ Fichier non trouvé : {chemin_csv}")
