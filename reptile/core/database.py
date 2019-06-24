import sys
import configparser

config_ini_file = "./config/config.ini"

class Database():

	def __init__(self):
		self.database = {}
		self.config_key = "DATABASE"
		
		self.database_config_parse()

	def database_config_parse(self):

		"""initialize database params from app config file"""
		config = configparser.ConfigParser()
		config.read(config_ini_file)

		if self.config_key in config:
			for key in config[self.config_key]:
				self.database[key] = config[self.config_key][key]
		else:
			print("not found database section in config ini file")
			sys.exit()

	def connect(self):
		pass

	def destroy(self):
		pass

