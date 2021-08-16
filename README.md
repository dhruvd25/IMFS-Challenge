# IMFS Data Engineering Challenge

## Overview
- Section 1: Read data from yfinance api
- Section 2: Extract, Load and Transform Data
    - __[processdata.py](./processdata.py)__ handels all ETL process needed to load, transform and extract data to __database.db__  (SQLite3 Database we will be using for the rest of the process)
- Section 3: 
    ![Alt text](./images/app_view.png?raw=true "Web App Sample View")
## Utility functions
- __[dbutils.py](./utils/dbutils.py)__: Database utility function to query and write against database. Current code hardcodes database location in class, should be modified to pass another location 

- __[dataprep.py](./utils/dataprep.py)__: Utility functions used to clean up data. Methods included:
    - getting historical pricing data from yfinance api [Extract]
    - processing historical pricing information for given ticker to preserver required information [Transform]
    - Function to create required tables in database with appropriate schema [Load]
    - Wrapper class to process and write data to database [ETL]
    - Function to populate database with index value calculation [Load]

- __[apphelper.py](./utils/apphelper.py)__: Utility functions used to query data from database and pass information to app server for display.
Contains the following queries:
    -  get_index_open_close: return the price weighted value of index open and close for input date
    - return_sector_open_close_volume: returns the percent weight of a sector contributing to the total index value for open and close on the given date, along with sector wise average volume 
    - get_total_index: returns close value of index across all the dates present in the database

## Database
- __ticker_info__: Table to store attributes relating to a given ticker

| Column | Datatype | Constraint |
| :---:| :---: | --- | 
| ticker | text| Primary Key
| isin   | text| Primary Key
| sector | text|
| company_name  | text|


- __historical_price__: Table to store historical price of tickers starting 2018-present 

| Column | Datatype | Constraint |
| :---:| :---: | --- | 
| ticker | text| Primary Key
| date   | text| Primary Key
| open   | real|
| close  | real|
| volume | real|

- __index_value__: Table to store calculated historical index open and close

| Column | Datatype | Constraint |
| :---:| :---: | --- | 
| date   | text| Primary Key
| index_open   | real|
| index_close  | real|


### Validate Tickers: 
In order to check if _constituents_history.pkl_ contains stock tickers, we use _company_ticker.json_ file available at https://www.sec.gov/files/company_tickers.json. This file contains all companies traded on the US stock exchange along with their company names and tickers.

Delisted Tickers:
RHT, TIF, CXO, GWR, PE, ZAYO, LOXO, ELLI, USG, TCF, CLGX, CMD, CTB

### Additional Caveats
- Since we do not have visiblity into index constituents for a given day, all valid tickers present in original file are assumed to make up the index (Price weighted Total stock index from the universe of all valid stocks)