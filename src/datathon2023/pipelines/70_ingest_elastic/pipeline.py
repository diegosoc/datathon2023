import os

from kedro.pipeline import node
from kedro.pipeline.modular_pipeline import pipeline

from .node import upload_data_to_elastic


def create_pipeline(**kwargs) -> pipeline:
    tags = ['70', 'inges_elastic']
    first_pipeline= pipeline(
        [
            node(

                func=upload_data_to_elastic,
                inputs=['demograficas_municipios','params:gasto_turistico_mapping','params:cloud_id', 'params:apikey_key'],
                outputs=None,

                name="upload_data_to_elastic",
            )
        ],
        tags=tags,

    )

    return first_pipeline