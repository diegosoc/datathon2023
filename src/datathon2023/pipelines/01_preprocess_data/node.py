import pandas as pd


def concat_files(
    comportamientos_municipios: pd.DataFrame,
    demograficas_municipios: pd.DataFrame,
    socioeconomicas_municipios: pd.DataFrame,
):
    dataframe = pd.concat([comportamientos_municipios, demograficas_municipios, socioeconomicas_municipios])
    return dataframe
