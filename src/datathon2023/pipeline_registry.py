"""Project pipelines."""
import logging

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

logger = logging.getLogger(__name__)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()

    pipelines['__default__'] = sum(pipelines.values())

    logger.info(f'Pipelines: {list(pipelines.keys())} has been created')
    return pipelines
