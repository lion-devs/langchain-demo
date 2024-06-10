import logging


def get_logger(name: str):
    """
    Get a logger with the specified name, creating it if necessary.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create a console handler
    stream_handler = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Add the formatter to the console handler
    stream_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(stream_handler)

    return logger
