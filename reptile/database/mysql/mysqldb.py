import sys
from reptile.database.basedb import BaseDatabase

class MysqlDatabase(BaseDatabase):

	@property
	def config_key(self):
		return "DATABASE"

	def __init__(self):
		"""invoke parent class init"""

		BaseDatabase.__init__(self)
		self.database_config_parse()

	def connect(self):
		pass

	def destroy(self):
		pass

