# -*- coding:utf-8 -*-
__author__ = 'EricDoug'

from ConfigParser import ConfigParser
from log_helper import tutorial_log

class Config_Read:
    '''
    配置的读取
    '''
    def __init__(self, title_name):
        self.title_name = title_name

    @property
    def _get_config_info(self):
        config = ConfigParser()
        try:
            config.read('./config.ini')
        except Exception as e:
            tutorial_log().error(e.message)

        db_info = {
            "host": config.get(self.title_name, "host"),
            "port": int(config.get(self.title_name, "port")),
            "user": config.get(self.title_name, "user"),
            "passwd": config.get(self.title_name, "passwd"),
            "db": config.get(self.title_name, "db")
        }

        return db_info
