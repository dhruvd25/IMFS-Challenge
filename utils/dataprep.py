import yfinance as yf

def get_historical_info_single(ticker:str, start_date:str=None, end_date:str=None):
    '''
    Function to return historical pricing information for given ticker
    :param ticker: Name of ticker
    :param start_date: Starting date form which history is needed
    :param end_date: End date till which history is needed
    '''
    import yfinance as yf
    ticker_info =yf.Ticker(ticker.upper())
    historical_info = ticker_info.history(start=start_date, end=end_date)
    return historical_info

def get_historical_info_multiple(tickers:list, start_date:str=None, end_date:str=None):
    '''
    Function to return historical pricing information for given ticker
    :param ticker: Name of ticker
    :param start_date: Starting date form which history is needed
    :param end_date: End date till which history is needed
    '''
    history = {}
    for ticker in tickers:
        history[ticker] = get_historical_info_single(ticker,start_date=start_date,end_date=end_date)
    return history

def get_ticker_info(ticker:str):
    tick_data = yf.Ticker(ticker)
    ticker_info = tick_data.info
    try:
        sector = ticker_info['sector']
    except: 
        sector = None
        print(f"SECTOR MISSING FOR {ticker}")
    try:
        name = ticker_info['longName']
    except: 
        name = None
        print(f"ISIN MISSING FOR {ticker}")

    return ticker,tick_data.isin,sector,name

def clean_data(ticker,in_df):
    in_df.reset_index(inplace=True)
    in_df.Date = in_df.Date.astype(str)
    in_df['Ticker'] = ticker
    in_df = in_df [['Ticker','Date','Open','Close','Volume']]
    vals = tuple(in_df.itertuples(index=False, name=None))
    return vals