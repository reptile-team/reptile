import os
import sys
import configparser
from abc import ABCMeta, abstractmethod, abstractproperty

# this may be a bug, the may be revised in future
# you should be place the config.conf file in your project root directory
config_ini_file = "./config.conf"

class BaseDatabase(metaclass = ABCMeta):
    """this is a abstracted base class, he will be implement by database sub class"""

    @abstractproperty
    def config_key(self):
        pass

    def __init__(self):
        self.database = {}

    def database_config_parse(self):
        """initialize database params from app config file"""
        config = configparser.ConfigParser()
        config.read(config_ini_file)

        if self.config_key in config:
            for key in config[self.config_key]:
                self.database[key] = config[self.config_key][key]
        else:
            print("not found database section in config conf file")
            sys.exit()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

