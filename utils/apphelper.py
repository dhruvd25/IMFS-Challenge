from utils.dbutils import *

def get_index_open_close(date: str):
    '''
    Function returns open, close and average volume for the given date
    :param date: string format date
    :return if valid date dictionary else None
    '''

    query = f'''SELECT ROUND(SUM(open)/COUNT(open),2) index_open,
                    ROUND(SUM(close)/COUNT(close),2) as index_close,
                    ROUND(AVG(volume)) as avg_vol
                FROM historical_price WHERE date='{date}' '''

    data = fetch(query, fetch_type='all')
    if len(data[0][0]) > 0:
        return {"Index Open": data[0][0][0],
                "Index Close": data[0][0][1],
                "Average Volume": data[0][0][2]}
    else:
        return None


def return_sector_open_close_volume(date: str):
    '''
    Function returns weighted sector wise contribution to the index for input date
    :param date: string format date  
    '''
    query = f'''
                SELECT COALESCE(t3.sector,'Sector N/A'), sum(t3.open), sum(t3.close), avg(t3.volume)
                FROM (SELECT t1.ticker,t2.sector,t1.open,t1.close,t1.volume
                FROM historical_price t1 
                LEFT JOIN ticker_info t2
                ON t1.ticker = t2.ticker
                WHERE t1.date ='{date}')t3
                GROUP BY t3.sector
            '''
    data = fetch(query, fetch_type='all', with_cols=True)[0]
    price_sum_open = 0
    price_sum_close = 0
    for i in data:
        price_sum_open += i[1]
        price_sum_close += i[2]
    output = []
    for i in data:
        output.append([date, i[0],
                    round((i[1]/price_sum_open)*100, 2),
                    round((i[2]/price_sum_close)*100, 2),
                    round(i[3])])
    return output


def get_total_index():
    '''
    Function to return date, open and close value for all dates in the database
    '''
    query = f'''SELECT * FROM index_value '''
    data = fetch(query, fetch_type='all', with_cols=True)
    return data[0], data[1]