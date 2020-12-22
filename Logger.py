import logging


class Logger:
    FILE_PATH = "logs.txt"

    def __init__(self):
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename=self.FILE_PATH,
                            level=logging.DEBUG, format=LOG_FORMAT)

    def log(self, value):
        logger = logging.getLogger()
        logger.info(value)
