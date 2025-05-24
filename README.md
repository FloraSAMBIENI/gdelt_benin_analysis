# 📊 Analyse des Données relatives au Bénin de la base de données GDELT 

Ce projet a été réalisé avec pour objectif d’extraire les données relatives au Bénin de la base de données GDELT, de les analyser pour identifier les tendances, les événements majeurs et les sentiments exprimés, et de les structurer pour faciliter leur utilisation dans des recherches ultérieures et des analyses prédictives.
   
---

## 🗂 Structure du projet
```
├── cleaned_data/
│ ├── clean_events.csv
│ ├── clean_gkg.csv
│ ├── clean_mentions.csv
│
├── data/
│ ├── benin_events.csv
│ ├── benin_gkg.csv
│ ├── benin_mentions.csv
│
├── outputs/
│ ├── analyse_results/
│ │  ├── evenements_majeurs.csv
│ │  ├── localisation_benin.csv
│ │  ├── mentions_benin.csv
│ │  ├── sentiments_benin.csv
│ │  ├── tendances_benin.csv
│ ├── openai_responses/
│ │  ├── analyse_evenements_majeurs.txt
│ │  ├── analyse_localisation.txt
│ │  ├── analyse_mentions.txt
│ │  ├── analyse_sentiments.txt
│ │  ├── analyse_tendances.txt
│ ├── visualisations/
│ │  ├── evenements_majeurs.png
│ │  ├── localisation_benin.png
│ │  ├── mentions_benin.png
│ │  ├── sentiments_benin.png
│ │  ├── tendance_evenements.png
│
├── scripts/
│ ├── analyses/
│ │  ├── analyse_complete.py
│ │  ├── analyse_evenements_maj.py
│ │  ├── analyse_localisation.py
│ │  ├── analyse_mentions.py
│ │  ├── analyse_sentiments.py
│ │  ├── analyse_tendances.py
│ ├── analyses_openai/
│ │  ├── analyse_evenements_majeurs.py
│ │  ├── analyse_localisation.py
│ │  ├── analyse_mentions.py
│ │  ├── analyse_sentiments.py
│ │  ├── analyse_tendance.py
│ ├── clean/
│ │  ├── clean_events.py
│ │  ├── clean_gkg.py
│ │  ├── clean_mentions.py
│ ├── visualisations/
│ │  ├── visualisations.py
│
├── .env.example
├── README.md
├── requirements.txt
```

---


## 📥 Extraction des données  

L’extraction des données a été réalisée depuis Google BigQuery, en filtrant spécifiquement les informations liées au Bénin à partir des tables publiques du projet GDELT (Global Database of Events, Language, and Tone).

Les catégories extraites sont :

    events (événements)

    mentions (mentions dans les documents)

    gkg (Global Knowledge Graph, contenant les lieux, thèmes, sentiments...)

Les données ont été exportées au format CSV et sont dans le dossier data :

    benin_events.csv

    benin_mentions.csv

    benin_gkg.csv


---

## 🧹 Nettoyage des données 

Un nettoyage a été appliqué aux trois fichiers extraits :

    Suppression des lignes complètement vides
    Suppression des doublons 
    Conversion des colonnes  aux bons formats 

Les fichiers nettoyés ont été enregistrés dans le dossier cleaned_data/:

    clean_events.csv
    clean_gkg.csv
    clean_mentions.csv
---

## 📊 Analyse des données 

    analyse_tendances.py
    → Analyse du nombre d’événements par mois (benin_events.csv)
    → Produit tendances_benin.csv

    analyse_mentions.py
    → Compte du nombre de mentions mensuelles (benin_mentions.csv)
    → Produit mentions_benin.csv

    analyse_sentiments.py
    → Moyenne mensuelle des tonalités (MentionDocTone) issues de benin_mentions.csv
    → Produit sentiments_benin.csv

    analyse_evenements_maj.py
    → Sélection des top 10 événements selon le nombre de mentions (NumMentions)
    → Produit evenements_majeurs.csv

    analyse_localisation.py
    → Extraction des lieux les plus fréquents depuis la colonne V2Locations de benin_gkg.csv
    → Produit localisation_benin.csv

Toutes les fonctions sont appelées automatiquement par le script principal analyse_complete.py, qui charge les données nettoyées et enregistre les résultats dans outputs\analyse_results.

---

## 📈 Visualisations des données 

Les visualisations ont été générées à l’aide de matplotlib et seaborn, à partir des fichiers résultats d’analyse.

    📌 Tendance des événements → tendance_evenements.png

    📌 Événements majeurs → evenements_majeurs.png

    📌 variations du ton moyen → sentiments_benin.png

    📌 Nombre de mentions par date → mentions_benin.png 

    📌 Lieux les plus mentionnés → localisation_benin.png

Script : visualisations.py
Les images sont dans outputs/visualisations/

---

## 🤖 Analyse des données par Azure openAI

Pour enrichir les résultats d’analyse avec une interprétation automatique, les cinq fichiers CSV finaux ont été envoyés à l’API Azure OpenAI. Chaque fichier a été converti en texte tabulaire et un prompt spécifique a été généré pour demander une analyse descriptive, des hypothèses et des tendances observées.

Les scripts associés sont dans scripts\analyses_openai:

    analyse_evenements_majeurs.py  → analyse_evenements_majeurs.txt

    analyse_localisation.py   → analyse_localisation.txt

    analyse_mentions.py     → analyse_mentions.txt

    analyse_sentiments.py    → analyse_sentiments.txt

    analyse_tendance.py     → analyse_tendances.txt

Toutes les fichiers txt sont enregistrés dans le dossier outputs\openai_responses, prêts à être consultés pour enrichir un rapport, une visualisation ou une présentation.

---

## Résultats 

Les résultats finaux sont organisés comme suit :

    Fichiers d’analyse : outputs\analyse_results

    Graphiques : outputs\visualisations

    Synthèses générées par Azure OpenAI : outputs\openai_responses

---

## 📦 Données volumineuses

Les fichiers CSV des dossiers cleaned_data et data sont disponibles ici :

🔗 [Accéder aux fichiers CSV sur Google Drive](LIEN_ICI)


