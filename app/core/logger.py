import logging
import json

logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(message)s"
)


def log_event(event: dict):
    logging.info(json.dumps(event))