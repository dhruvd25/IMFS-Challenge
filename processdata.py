import yfinance as yf
import json
from pickle5 import pickle
from utils.dbutils import *
import sqlite3
from utils.dataprep import *
import requests
from multiprocessing import Pool



class ETL():
    def __init__(self, ticker, start_date: str = '2018-01-01', end_date: str = None):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def process_historical(self):
        self.out_df = get_historical_info_single(
            self.ticker, start_date=self.start_date, end_date=self.end_date)
        return True

    def clean_data(self):
        self.out_df.reset_index(inplace=True)
        self.out_df.Date = self.out_df.Date.astype(str)
        self.out_df['Ticker'] = self.ticker
        self.out_df = self.out_df[[
            'Ticker', 'Date', 'Open', 'Close', 'Volume']]
        self.vals = tuple(self.out_df.itertuples(index=False, name=None))
        return True

    def insert_rows(self):
        query_insert = '''INSERT INTO historical_price VALUES (?,?,?,?,?) '''
        executemany(query_insert, self.vals)
        return True

    def execute(self):
        self.process_historical()
        self.clean_data()
        self.insert_rows()
        return True


def pool_call(ticker):
    return ETL(ticker).execute()


def create_db_tables():

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
                                            sector real,
                                            company_name text,
                                            PRIMARY KEY(ticker,isin)
                                            )
                        """
    execute(query_ticker_info)
    return True

if __name__ == '__main__':

    resp = requests.get('https://www.sec.gov/files/company_tickers.json')
    company_ticker = resp.json()
    with open('./data/constituents_history.pkl', 'rb') as fp:
        data = pickle.load(fp)

    daily_ticks = {}
    all_tickers = {}

    for i in data.iterrows():
        if len(i[1][0]) > 0:
            daily_ticks[i[0]] = []
            for attribs in i[1][0]:
                daily_ticks[i[0]].append(attribs[0])
                if attribs[0] in all_tickers.keys():
                    all_tickers[attribs[0]] += 1
                else:
                    all_tickers[attribs[0]] = 1

    valid_stocks = []
    for i, j in company_ticker.items():
        if j['ticker'] in all_tickers.keys():
            valid_stocks.append(j['ticker'])
    
    print('Creating Tables in database')
    # create_db_tables()

    print('Performing ETL.....')
    with Pool(5) as pool:
        output = pool.map(pool_call, valid_stocks)
    print('Rows added to DB!')
