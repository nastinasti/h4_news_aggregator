import logging
import datetime


class NEWSLogging:
    def __init__(self):
        self.logger = logging.getLogger('news_logger')
        self.logger.setLevel(logging.INFO)

        self.formatter = logging.Formatter('%(levelname)s: %(message)s')
        self.fh = logging.FileHandler('advanced.log')
        self.fh.setLevel(logging.ERROR)
        self.fh.setFormatter(self.formatter)

        self.ch = logging.StreamHandler(f'%(datetime)s - %(class_name)s - %(message)s')
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)