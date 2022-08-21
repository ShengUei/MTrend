# Note: the module name is psycopg, not psycopg3
import psycopg
from setting.connect_setting import get_conn_setting

# Connect to an existing database
# def getConnection():
#     conn = psycopg.connect(conn_str)
#     return conn

conn = psycopg.connect(get_conn_setting())

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