import numpy as np
import pandas as pd
from scipy.stats import zscore

def apply_zscore(df, columns):
    filtres = []
    for col in columns:
        filtres.append(np.abs(zscore(df[col])) < 3)

    filtre = filtres[0]
    for f in filtres[1:]:
        filtre = filtre & f

    return df[filtre]

""" Pour un pd.Dataframe contenant les colonnes longeur, largeur et hauteur
    renvoie un pd.Series avec autant de lignes contemant la somme des trois colonnes ci-dessus
"""
def get_volume(df):

    def product_tuple(t):
        return sum([
            np.product([
                t[0][j],
                t[1][j],
                t[2][j]
            ])
            for j in range(len(t[0]))
        ])

    serie_volume = pd.Series()
    temp = [
        pd.Series(
            product_tuple(elems),
            index=[i]
        )
        for i, elems 
        in enumerate(df.itertuples(index=False))
    ]
    return serie_volume.append(temp).rename('volume')

""" Pour un pd.Dataframe contenant les une colonne avec des listes
    renvoie un pd.Dataframe avec autant de lignes et en colonne les elements contenus dans les listes
    Le resultat sur la forme s'apparente a un OneHotEncoder
"""
def category_list_encoding(df, column):
    categories_encoding = [
        pd.DataFrame(
            pd.get_dummies(item).max().values.reshape(1, len(item)),
            columns=item
        )
        for item
        in df[column]
    ]

    df_categories = pd.concat(
        categories_encoding
    )

    df_categories = df_categories.reset_index(drop=True)
    df_categories = df_categories.replace(np.nan, 0)
    df = pd.merge(df, df_categories, left_index=True, right_index=True)
    df = df.drop(columns=column)
    return df