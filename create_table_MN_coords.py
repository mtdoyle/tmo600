import pymysql.cursors

charset = "CHARACTER SET utf8 COLLATE utf8_general_ci"

query = "create table if not exists tmo600MNcoords " \
        "(lat varchar(20) {0}, lon varchar(20) {0})".format(charset)
con = pymysql.connect(host='127.0.0.1', port=3306, user='tmo600', passwd='tmo600', db='tmo600')
cur = con.cursor()

cur.execute(query)
con.commit()



