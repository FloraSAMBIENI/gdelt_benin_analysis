import pandas as pd

def analyser_sentiments(mentions_df):
    # Convertir la colonne MentionTimeDate en datetime
    mentions_df['MentionTimeDate'] = pd.to_datetime(mentions_df['MentionTimeDate'], errors='coerce')

    # Extraire l'année et le mois
    mentions_df['YearMonth'] = mentions_df['MentionTimeDate'].dt.to_period('M')

    # Grouper par mois et calculer le ton moyen
    sentiments_mensuels = mentions_df.groupby('YearMonth')['MentionDocTone'].mean().reset_index()
    sentiments_mensuels.columns = ['YearMonth', 'AvgTone']

    return sentiments_mensuels