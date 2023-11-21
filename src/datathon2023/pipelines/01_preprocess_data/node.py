import pandas as pd


def concat_files(
    comportamientos_municipios: pd.DataFrame,
    demograficas_municipios: pd.DataFrame,
    socioeconomicas_municipios: pd.DataFrame,
):
    dataframe = pd.concat([comportamientos_municipios, demograficas_municipios, socioeconomicas_municipios])
    return dataframe


def geodata(geodata: pd.DataFrame, df: pd.DataFrame):

    #after some preprocessing we have detected some values that are not the same in geodata and in df like
    # La Oliva is Oliva, La
    geodata= geodata.replace('Oliva, La', 'La Oliva')
    #We need the unique values in geodata
    geodata= geodata.drop_duplicates(subset=['municipio_geo'])
    geodata = geodata.merge(df, left_on='municipio_geo', right_on='municipio', how='inner')

    return geodata
