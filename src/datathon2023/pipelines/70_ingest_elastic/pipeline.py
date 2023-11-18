import os

from kedro.pipeline import node
from kedro.pipeline.modular_pipeline import pipeline

from .node import cosa


def create_pipeline(**kwargs) -> pipeline:
    tags = ['70', 'inges_elastic']
    first_pipeline= pipeline(
        [
            node(

                func=cosa,
                inputs=['params:cloud_id', 'params:apikey_id', 'params:apikey_key'],
                outputs=None,

                name="cosa2",
            )
        ],
        tags=tags,

    )

    return first_pipeline
