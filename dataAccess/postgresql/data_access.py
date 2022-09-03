from dataAccess.postgresql.connection import openConnection
from model.Currency import Currency
from logger.logger import get_logger

def get_currency_exchange_rate_by_date(date, currency):
    logger = get_logger()

    conn = openConnection()
    
    try:
        record = conn.execute("""
                                 SELECT quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell
                                 FROM foreign_exchange_rate
                                 WHERE quoted_date::date = %(quoted_date)s AND currency ILIKE %(currency)s;
                                 """,
                                 {'quoted_date' : date, 
                                 'currency' : '%{}%'.format(currency)}).fetchone()

    except BaseException as e:
        conn.rollback()
        print("BaseException : %s" % e)
        logger.error("BaseException : %s" % e)
        return None

    else:
        conn.commit()
        print("Get %s Exchange Rate is Success" % currency)
        logger.info("Get %s Exchange Rate is Success" % currency)
        currency_obj = Currency()
        
        currency_obj.quoted_date = record.get('quoted_date')
        currency_obj.currency = record.get('currency')
        currency_obj.cash_buying = record.get('cash_buy')
        currency_obj.cash_selling = record.get('cash_sell')
        currency_obj.spot_buying = record.get('spot_buy')
        currency_obj.spot_selling = record.get('spot_sell')

        return currency_obj
        
    finally:
        conn.close()

def insert_all_exchange_rate(input_object_list):
    logger = get_logger()

    conn = openConnection()
    
    try:
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

    except BaseException as e:
        conn.rollback()
        print("BaseException : %s" % e)
        logger.error("BaseException : %s" % e)

    else:
        conn.commit()
        print("All Currency Exchange Rate Insert Success")
        logger.info("All Currency Exchange Rate Insert Success")
        
    finally:
        conn.close()