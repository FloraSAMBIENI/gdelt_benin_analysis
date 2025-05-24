import pandas as pd

def analyser_mentions(mentions_df):
    # Conversion de la colonne MentionTimeDate en datetime
    mentions_df['MentionTimeDate'] = pd.to_datetime(mentions_df['MentionTimeDate'], errors='coerce')

    # Supprimer les lignes avec des dates invalides
    mentions_df = mentions_df.dropna(subset=['MentionTimeDate'])

    # Extraire l'année et le mois
    mentions_df['YearMonth'] = mentions_df['MentionTimeDate'].dt.to_period('M')

    # Compter le nombre de mentions par mois
    freq_mentions = mentions_df.groupby('YearMonth').size().reset_index(name='Nombre_mentions')

    return freq_mentions
