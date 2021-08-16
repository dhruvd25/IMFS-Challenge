import yfinance as yf
import json
from pickle5 import pickle
from utils.dbutils import *
import sqlite3
from utils.dataprep import *
import requests
from multiprocessing import Pool

if __name__ == '__main__':

    resp = requests.get('https://www.sec.gov/files/company_tickers.json')
    company_ticker = resp.json()
    with open('./data/constituents_history.pkl', 'rb') as fp:
        data = pickle.load(fp)

    # keep track of all tickers provided in original file
    all_tickers = {}

    # Dictionary to keep track of valid ticker
    meta_data = {}
    meta_data['valid_stock_ticker'] = []
    meta_data['non_stock_ticker'] = []
    meta_data['delisted_ticker'] = ["RHT", "TIF", "CXO", "GWR", "PE",
                                    "ZAYO", "LOXO", "ELLI", "USG", "TCF", "CLGX", "CMD", "CTB"]

    for i in data.iterrows():
        if len(i[1][0]) > 0:
            for attribs in i[1][0]:
                if attribs[0] in all_tickers.keys():
                    all_tickers[attribs[0]] += 1
                else:
                    all_tickers[attribs[0]] = 1

    # get all stocks present in file read from SEC
    all_stocks = []
    for i, j in company_ticker.items():
        all_stocks.append(j['ticker'])

    # filter out all tickers which aren't stock tickers
    for i, j in all_tickers.items():
        if i not in all_stocks:
            meta_data['non_stock_ticker'].append(i)

    # subset tickers from all tickers to just valid tickers

    for i, j in company_ticker.items():
        if j['ticker'] in all_tickers.keys():
            meta_data['valid_stock_ticker'].append(j['ticker'])

    # Remove all delisted stocks from valid stock list
    meta_data['valid_stock_ticker'] = list(
        set(meta_data['valid_stock_ticker']) - set(meta_data['delisted_ticker']))

    with open('./data/meta_data.json','w') as fp:
        json.dump(meta_data,fp)

    print('Creating Tables in database')
    create_db_tables()

    print('Performing ETL.....')
    print('Processing Historical Pricing information')
    with Pool(5) as pool:
        output = pool.map(pool_call, meta_data['valid_stock_ticker'])
    print('Historical Prices added to DB!')

    print("Processing additional information for tickers")
    with Pool(5) as pool:
        ticker_info = pool.map(
            get_ticker_info, meta_data['valid_stock_ticker'])
    print('Ticker information added to DB!')