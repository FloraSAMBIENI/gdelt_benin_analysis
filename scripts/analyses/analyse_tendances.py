import pandas as pd

def analyser_tendances(events_df):
    events_df['YearMonth'] = events_df['SQLDATE'].dt.to_period('M')
    tendances = events_df.groupby('YearMonth').size().reset_index(name='Nombre_événements')
    return tendances
