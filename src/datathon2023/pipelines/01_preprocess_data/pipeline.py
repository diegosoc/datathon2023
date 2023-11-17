import os

from kedro.pipeline import node
from kedro.pipeline.modular_pipeline import pipeline

from .node import cosa


def create_pipeline(**kwargs) -> pipeline:
    tags = ['01', 'preprocess_data']
    first_pipeline= pipeline(
        [
            node(
                cosa,
                inputs="cobertura_5g",
                outputs="example",
                name="cosa",
            )
        ],

    )

    return first_pipeline
