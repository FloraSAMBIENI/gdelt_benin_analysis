import pandas as pd
from collections import Counter

def analyser_localisation(gkg_df):
    """
    Analyse les localisations mentionnées dans la colonne V2Locations
    du fichier GKG nettoyé (benin_gkg.csv).

    Retourne un DataFrame contenant les lieux les plus fréquemment mentionnés.
    """
    lieux = []
    for ligne in gkg_df['V2Locations'].dropna():
        blocs = ligne.split(';')
        for bloc in blocs:
            champs = bloc.split('#')
            if len(champs) > 1:
                lieu = champs[1].strip()
                if lieu:
                    lieux.append(lieu)
    
    compteur = Counter(lieux)
    df_freq = pd.DataFrame(compteur.items(), columns=['Lieu', 'Occurrences'])
    df_freq = df_freq.sort_values(by='Occurrences', ascending=False)
    
    return df_freq
