from kedro.pipeline import node
from kedro.pipeline.modular_pipeline import pipeline

from .node import concat_files, geodata


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
    second_pipeline = pipeline(
        [
            node(
                func=geodata,
                inputs=['geodata', 'gasto_turistico'],
                outputs='gasto_turistico_with_geodata',
                name='cosa2',
            )
        ],
        tags=tags,
    )

    return first_pipeline + second_pipeline
