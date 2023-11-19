import pandas as pd


def concat_files(
    comportamientos_municipios: pd.DataFrame,
    demograficas_municipios: pd.DataFrame,
    socioeconomicas_municipios: pd.DataFrame,
):
    dataframe = pd.concat([comportamientos_municipios, demograficas_municipios, socioeconomicas_municipios])
    return dataframe


def geodata(geodata: pd.DataFrame, df: pd.DataFrame):
    geodata = geodata.merge(df, left_on='municipio_geo', right_on='municipio', how='inner')
    return geodata
