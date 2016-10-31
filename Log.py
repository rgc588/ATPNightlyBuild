import logging


class Log:
    logger = logging
    logging.basicConfig(filename='run.log', level=logging.INFO)
