import getpass
import os

from tools import logger

log = logger.get_logger(__name__)


def check_env(key: str):
    if not os.environ.get(key):
        log.info(f"Environment variable {key} not found.")
        os.environ[key] = getpass.getpass('Please enter the value: ')
    return os.environ[key]
