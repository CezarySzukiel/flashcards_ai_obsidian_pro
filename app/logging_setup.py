import atexit
import os
import tomllib
from pathlib import Path

import logging.config


def setup_logging():
    if os.getenv("TESTS") == "1":
        return

    config_file = Path(".logging_configs/config.toml")
    with open(config_file, "rb") as file:
        config = tomllib.load(file)
    logging.config.dictConfig(config)

    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
