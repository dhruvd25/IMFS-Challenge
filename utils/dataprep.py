import yfinance as yf
from utils.dbutils import *


def get_historical_info_single(ticker: str, start_date: str = None, end_date: str = None):
    '''
    Function to return historical pricing information for given ticker
    :param ticker: Name of ticker
    :param start_date: Starting date form which history is needed
    :param end_date: End date till which history is needed
    '''
    import yfinance as yf
    ticker_info = yf.Ticker(ticker.upper())
    historical_info = ticker_info.history(start=start_date, end=end_date)
    return historical_info


def get_historical_info_multiple(tickers: list, start_date: str = None, end_date: str = None):
    '''
    Function to return historical pricing information for given ticker
    :param ticker: Name of ticker
    :param start_date: Starting date form which history is needed
    :param end_date: End date till which history is needed
    '''
    history = {}
    for ticker in tickers:
        history[ticker] = get_historical_info_single(
            ticker, start_date=start_date, end_date=end_date)
    return history


def get_ticker_info(ticker: str):
    '''
    Function to return basic attributes for given ticker
    :param ticker: string format ticker
    :return: ticker name, ticker isin, ticker sector, company name
    '''
    tick_data = yf.Ticker(ticker.upper())
    ticker_info = tick_data.info
    
    try:
        sector = ticker_info['sector']
    except:
        sector = None
        print(f"SECTOR MISSING FOR {ticker}")

    try:
        name = ticker_info['longName']
    except:
        try:
            name = ticker_info['shortName']
        except:
            name = None
            print(f"Name MISSING FOR {ticker}")

    try:
        isin = tick_data.isin
    except:
        isin = None
        print(f"Name MISSING FOR {ticker}")


    return ticker, isin, sector, name


def pool_call(ticker):
    '''
    Wrapper function used for multiprocessing
    '''
    return ETL(ticker).execute()


class ETL():
    def __init__(self, ticker, start_date: str = '2018-01-01', end_date: str = None):
        '''
        :param ticker: string format ticker 
        :param start_date: start date for which the data is needed for given ticker, current default 2018-01-01
        :paream end_date: end date till which historical data is needed
        '''
        self.ticker = ticker.upper()
        self.start_date = start_date
        self.end_date = end_date

    def process_historical(self):
        '''
        '''
        self.out_df = get_historical_info_single(
            self.ticker, start_date=self.start_date, end_date=self.end_date)
        return True

    def clean_data(self):
        '''
        Helper function to clean historical data for given ticker
        '''
 
        self.out_df.reset_index(inplace=True)
        self.out_df.Date = self.out_df.Date.astype(str)
        self.out_df['Ticker'] = self.ticker
        self.out_df = self.out_df[[
            'Ticker', 'Date', 'Open', 'Close', 'Volume']]
        self.vals = tuple(self.out_df.itertuples(index=False, name=None))
        return True

    def insert_rows(self):
        '''
        Insert data for given ticker to database
        '''
        query_insert = '''INSERT INTO historical_price VALUES (?,?,?,?,?) '''
        executemany(query_insert, self.vals)
        return True

    def execute(self):

        self.process_historical()
        self.clean_data()
        self.insert_rows()
        return True


def create_db_tables():
    '''
    Create required tables in database
    '''
    execute("DROP TABLE IF EXISTS historical_price")
    query = """CREATE TABLE historical_price (
                                        ticker text,
                                        date text,
                                        open real,
                                        close real,
                                        volume real,
                                        PRIMARY KEY(ticker,date)
                                        ) 
            """
    execute(query)

    execute("DROP TABLE IF EXISTS ticker_info")
    query_ticker_info = """CREATE TABLE ticker_info (
                                            ticker text,
                                            isin text,
                                            sector text,
                                            company_name text,
                                            PRIMARY KEY(ticker,isin)
                                            )
                        """
    execute(query_ticker_info)

    execute("DROP TABLE IF EXISTS index_value")
    query_index_value = """CREATE TABLE index_value (date text,
                                        index_open real,
                                        index_close real,
                                        PRIMARY KEY(date)) """
    execute(query_index_value)
    return True


def create_daily_index_open_close():
    '''
    Populate index_value table in database
    '''
    populate_index_history = '''INSERT INTO index_value (date, index_open,index_close)
    SELECT date as date,
                    ROUND(SUM(open)/COUNT(open),2) as index_open,
                    ROUND(SUM(close)/COUNT(close),2) as index_close
    FROM historical_price
    GROUP BY date '''
    execute(populate_index_history)

    return True