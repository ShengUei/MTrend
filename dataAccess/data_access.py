# Note: the module name is psycopg, not psycopg3
import psycopg
from dataAccess.connection import openConnection

def get_all_exchange_rate():
    conn = openConnection()

    try:
        list = conn.execute("""
                            SELECT * 
                            FROM foreign_exchange_rate
                            """).fetchall()

    except BaseException:
        conn.rollback()
        print("BaseException")

    else:
        conn.commit()

    finally:
        conn.close()

    return list

def insert_all_exchange_rate(input_object_list):
    conn = openConnection()
    
    try:
        # cur = conn.cursor()
        # with cur.copy("COPY foreign_exchange_rate (quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell) FROM STDIN") as copy:
            # for object in input_object_list:
            #     copy.write_row(object)
        for object in input_object_list:
            conn.execute("""
                        INSERT INTO 
                        foreign_exchange_rate (quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell)
                        VALUES (%(quoted_date)s, %(currency)s, %(cash_buy)s, %(cash_sell)s, %(spot_buy)s, %(spot_sell)s);
                        """,
                        {'quoted_date' : object.quoted_date, 
                        'currency' : object.currency, 
                        'cash_buy' : object.cash_buying,
                        'cash_sell' : object.cash_selling,
                        'spot_buy' : object.spot_buying,
                        'spot_sell' : object.spot_selling})

    except BaseException  as e:
        conn.rollback()
        print("BaseException")
        print(e)

    else:
        conn.commit()
        print("Insert Success")

    finally:
        conn.close()
