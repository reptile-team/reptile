from reptile.database.basedb import BaseDatabase

class MysqlDatabase(BaseDatabase):

	@property
	def config_key(self):
		return "MYSQL"

	def __init__(self):
		super().__init__()
		self.database_config_parse()

	def connect(self):
		pass

	def destroy(self):
		pass

