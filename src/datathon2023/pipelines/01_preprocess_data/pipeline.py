import os

from kedro.pipeline import node
from kedro.pipeline.modular_pipeline import pipeline

from .node import concat_files


def create_pipeline(**kwargs) -> pipeline:
    tags = ['01', 'preprocess_data']
    first_pipeline = pipeline(
        [
            node(
                func=concat_files,
                inputs=['comportamientos_municipios', 'demograficas_municipios', 'socioeconomicas_municipios'],
                outputs='gasto_turistico',
                name='cosa',
            )
        ],
        tags=tags,
    )

    return first_pipeline
