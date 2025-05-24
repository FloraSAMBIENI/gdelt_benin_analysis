import pandas as pd

def extraire_evenements_majeurs(events_df, top_n=10):
    top_events = events_df.sort_values(by='NumMentions', ascending=False).head(top_n)
    return top_events[['SQLDATE', 'Actor1Name', 'Actor2Name', 'EventCode', 'NumMentions']]
