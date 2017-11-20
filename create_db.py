import pymysql.cursors


def createDB(con):
    cur = con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS tmo600;')
    cur.execute('create user if not exists \'tmo600\'@\'*\' identified by \'tmo600\';')
    cur.execute('grant all on *.* to \'tmo600\'@\'%\' identified by \'tmo600\';')

charset = "CHARACTER SET utf8 COLLATE utf8_general_ci"

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='password')
createDB(con)
query = "create table if not exists tmo600 " \
        "(lat varchar(20) {0}, lon varchar(20) {0}, strength varchar(1) {0})".format(charset)
con2 = pymysql.connect(host='127.0.0.1', port=3306, user='tmo600', passwd='tmo600', db='tmo600')
cur = con2.cursor()

cur.execute(query)
con.commit()



