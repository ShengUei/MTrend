# Note: the module name is psycopg, not psycopg3
import psycopg

#DataBase infomation
host = ""
port = ""
dbname = ""
user = ""
password = ""
sslmode = "allow"

conn_str = "host={0} port={1} user={2} dbname={3} password={4} sslmode={5}".format(host, port, user, dbname, password, sslmode)

# Connect to an existing database
# def getConnection():
#     conn = psycopg.connect(conn_str)
#     return conn

conn = psycopg.connect(conn_str)

if conn is not None:
    print("conn success")
    # cur = conn.cursor()
    # cur.execute("INSERT INTO foreign_exchange_rate (quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell) \
    #             VALUES (%s, %s, %s, %s, %s, %s)", 
    #             ("2022/08/14 09:25", "JPY", "0.2154", "0.2282", "0.2222", "0.2272"))

    # record = cur.execute("Select * From foreign_exchange_rate").fetchall()
    record = conn.execute("Select * From foreign_exchange_rate").fetchall()

    for data in record:
        print(data)
    
    # conn.commit()
    conn.close()
else:
    print("conn failure")

