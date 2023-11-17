"""Project settings. There is no need to edit this file unless you want to change values
from the Kedro defaults. For further information, including these default values, see
https://kedro.readthedocs.io/en/stable/kedro_project_setup/settings.html."""

import datetime
import os
from pathlib import Path

from kedro.config import OmegaConfigLoader

# Installed plugins for which to disable hook auto-registration.
# Should be automated Kedro-viz, and kedro-mlflow
DISABLE_HOOKS_FOR_PLUGINS = ("kedro-mlflow",) #noneeded for this project

# Class that manages storing KedroSession data.
# from kedro.framework.session.store import BaseSessionStore
# SESSION_STORE_CLASS = BaseSessionStore
# Keyword arguments to pass to the `SESSION_STORE_CLASS` constructor.
# SESSION_STORE_ARGS = {
#     "path": "./sessions"
# }

# Directory that holds configuration.
# CONF_SOURCE = "conf"

# Class that manages how configuration is loaded.
# from kedro.config import OmegaConfigLoader

CONFIG_LOADER_CLASS = OmegaConfigLoader
# Keyword arguments to pass to the `CONFIG_LOADER_CLASS` constructor.

CONFIG_LOADER_ARGS = {
    'config_patterns': {
        'spark': ['spark*/'],
        'mlflow*': ['mlflow*/'],  # the star is important or the hook give error (the hook should be updated)
    },
    # 'globals_pattern': '*globals.yml',
}


# Class that manages Kedro's library components.
# from kedro.framework.context import KedroContext
# CONTEXT_CLASS = KedroContext

# Class that manages the Data Catalog.
# from kedro.io import DataCatalog
# DATA_CATALOG_CLASS = DataCatalog
