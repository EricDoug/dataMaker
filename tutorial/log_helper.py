# -*- coding:utf-8 -*-
__author__ = 'EricDoug'
from logging import Formatter
from logging.handlers import RotatingFileHandler
import logging


def tutorial_log():
    handler = RotatingFileHandler('tutorial.log', mode='a', maxBytes=10000000, backupCount=10)
    handler.setFormatter(Formatter("%(levelname)s [%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
    logger = logging.getLogger("tutorial.log")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
