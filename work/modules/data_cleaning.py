import numpy as np
from scipy.stats import zscore

def apply_zscore(df, columns):
    filtres = []
    for col in columns:
        filtres.append(np.abs(zscore(df[col])) < 3)

    filtre = filtres[0]
    for f in filtres[1:]:
        filtre = filtre & f

    return df[filtre]