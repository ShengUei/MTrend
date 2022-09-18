from dataAccess.postgresql.connection import openConnection
from model.Currency import Currency
from logger.logger import get_logger
from util.string_to_number import str_to_int

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

def insert_all_trading_details(data_dict):
    try:
        logger = get_logger()

        conn = openConnection()
        
        if(data_dict == None):
            print("All Trading Details Insert Not Run")
            logger.info("All Trading Details Insert Not Run")
            return

        for data_row in data_dict['data_list']:
            conn.execute("""
                        INSERT INTO 
                        stock_trading_details 
                            (datetime, 
                            security_code, 
                            mainland_area_investors_total_buy, mainland_area_investors_total_sell, mainland_area_investors_difference, 
                            foreign_dealers_total_buy, foreign_dealers_total_sell, foreign_dealers_difference, 
                            securities_investment_trust_companies_total_buy, securities_investment_trust_companies_total_sell, securities_investment_trust_companies_difference, 
                            dealers_difference, 
                            dealers_proprietary_total_buy, dealers_proprietary_total_sell, dealers_proprietary_difference, 
                            dealers_hedge_total_buy, dealers_hedge_total_sell, dealers_hedge_difference, 
                            total_difference)
                        VALUES 
                            (%(datetime)s, 
                            %(security_code)s, 
                            %(mainland_area_investors_total_buy)s, %(mainland_area_investors_total_sell)s, %(mainland_area_investors_difference)s, 
                            %(foreign_dealers_total_buy)s, %(foreign_dealers_total_sell)s, %(foreign_dealers_difference)s, 
                            %(securities_investment_trust_companies_total_buy)s, %(securities_investment_trust_companies_total_sell)s, %(securities_investment_trust_companies_difference)s, 
                            %(dealers_difference)s, 
                            %(dealers_proprietary_total_buy)s, %(dealers_proprietary_total_sell)s, %(dealers_proprietary_difference)s, 
                            %(dealers_hedge_total_buy)s, %(dealers_hedge_total_sell)s, %(dealers_hedge_difference)s, 
                            %(total_difference)s);
                        """,
                        {'datetime' : data_dict['current_datetime'], 
                        'security_code' : data_row[0], 
                        'mainland_area_investors_total_buy' : str_to_int(data_row[1]),
                        'mainland_area_investors_total_sell' : str_to_int(data_row[2]),
                        'mainland_area_investors_difference' : str_to_int(data_row[3]),
                        'foreign_dealers_total_buy' : str_to_int(data_row[4]),
                        'foreign_dealers_total_sell' : str_to_int(data_row[5]),
                        'foreign_dealers_difference' : str_to_int(data_row[6]),
                        'securities_investment_trust_companies_total_buy' : str_to_int(data_row[7]),
                        'securities_investment_trust_companies_total_sell' : str_to_int(data_row[8]),
                        'securities_investment_trust_companies_difference' : str_to_int(data_row[9]),
                        'dealers_difference' : str_to_int(data_row[10]),
                        'dealers_proprietary_total_buy' : str_to_int(data_row[11]),
                        'dealers_proprietary_total_sell' : str_to_int(data_row[12]),
                        'dealers_proprietary_difference' : str_to_int(data_row[13]),
                        'dealers_hedge_total_buy' : str_to_int(data_row[14]),
                        'dealers_hedge_total_sell' : str_to_int(data_row[15]),
                        'dealers_hedge_difference' : str_to_int(data_row[16]),
                        'total_difference' : str_to_int(data_row[17])})

    except BaseException as e:
        conn.rollback()
        print("BaseException : %s" % e)
        logger.error("BaseException : %s" % e)

    else:
        conn.commit()
        print("All Trading Details Insert Success")
        logger.info("All Trading Details Insert Success")
        
    finally:
        conn.close()