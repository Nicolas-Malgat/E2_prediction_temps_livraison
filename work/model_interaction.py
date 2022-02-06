from joblib import dump, load
from pathlib import Path
import pandas as pd
import sqlite3

def predict_delivery_time(form_data: list, database_path='../datas/CLEAN/E2/', pickle_folder='work/pickle/'):
    # Recuperation du nommage des colonnes

    con = sqlite3.connect(database_path + 'E2.db')
    X = pd.read_sql('select * from preprocessor_input LIMIT 0', con, index_col='index')
    con.close()

    # Preparation de la data
    form_data = pd.DataFrame(
        data=[form_data],
        columns=X.columns
    )

    # Chargement et prediction des données
    preprocessor = load(pickle_folder + 'preprocessor' + '.pkl')
    model = load(pickle_folder + 'model' + '.pkl')

    # Je n'ai pas reussi a enlever le warning
    # Forme de dataframe pour enlever un warning
    # form_data = pd.DataFrame(
    #     preprocessor.transform(form_data)
    # )
    # return form_data
    # print(type(form_data), form_data.columns)

    form_data = pd.DataFrame(
        preprocessor.transform(form_data)
    )
    y_pred = model.predict(form_data)[0]
    form_data.insert(0, 'y_pred', y_pred)

    con = sqlite3.connect(database_path + 'E2.db')
    form_data.to_sql(name='predictions', con=con, if_exists='append')
    con.close()

    return y_pred
