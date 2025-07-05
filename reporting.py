import matplotlib.pyplot as plt
import pandas as pd
from pipeline import *

def plot_qualite(df_qualite):
    df_qualite = df_qualite.set_index('colonne')
    df_qualite[['taux_completude (%)', 'taux_unicite (%)', 'Taux_validaty(%)', 'Taux_Cohrence(%)']]\
        .plot(kind='bar', figsize=(10,6))
    plt.title("Qualité des colonnes")
    plt.ylabel("Pourcentage (%)")
    plt.ylim(0, 110)
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig("reports.png")
if __name__ == "__main__":
    df = pd.read_csv("Client_Data_Sample.csv", sep=';', dtype={'telephone': str})

    vis=analyser_dataframe(df)  # ta fonction qui renvoie le DataFrame résumé
    plot_qualite(vis)
