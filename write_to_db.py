import pymysql.cursors

def write_to_db(lat, lon, strength):
    query = "insert into tmo600 (lat,lon,strength) values ({0},{1},{2})".format(lat,lon,strength)
    con = pymysql.connect(host='127.0.0.1', port=3306, user='tmo600', passwd='tmo600', db='tmo600')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
