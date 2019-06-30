# coding=utf-8
import sys

sys.path.append('../../')

from reptile.database.mysqldb import MysqlDatabase

mysql = MysqlDatabase()

print(mysql.database)