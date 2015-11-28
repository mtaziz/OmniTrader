import pymysql
import dropbox
import logging

logger = logging.getLogger('stocks.management.readDropbox')

logger.info('Initiating OmniTrader')

#load pymysql as mysqldb - mysqldb does not work with python 3 as ConfigParser is renamed
pymysql.install_as_MySQLdb()


logger.info("Linking to Dropbox account...")
dbx = dropbox.Dropbox('DO8936TNbkgAAAAAAAAAg4zB4LdJK2SBNBPdjaTWM5mpzjU8dFmp1MV5DNiEXDzk')
