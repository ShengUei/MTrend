
#DataBase infomation
host = ""
port = ""
dbname = ""
user = ""
password = ""
sslmode = "allow"

conn_setting = "host={0} port={1} user={2} dbname={3} password={4} sslmode={5}".format(host, port, user, dbname, password, sslmode)

def get_conn_setting():
    return conn_setting

