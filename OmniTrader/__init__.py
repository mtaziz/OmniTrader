import pymysql
import tushare as ts

#load pymysql as mysqldb - mysqldb does not work with python 3 as ConfigParser is renamed
pymysql.install_as_MySQLdb()
ts.set_token('b61cc25954846cdf24f900b744a4965122a83f6de89311e9d552b8ee365b4df4')
