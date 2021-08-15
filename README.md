## IMFS Data Engineering Challenge

## Utility functions
- __./utils/dbutils__: Database utility function to query and write against database. Current code hardcodes database location in class, should be modified to pass another location 

- __./utils/dataprep__: Utility functions used to clean up data. Methods included:
    - getting historical pricing data from yfinance api
    - processing historical pricing information for given ticker to preserver required information
    - Wrapper class to process and write data to database
    - Function to create required tables in database with appropriate schema

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

### Validate Tickers: 
In order to check if _constituents_history.pkl_ contains stock tickers, we use _company_ticker.json_ file available at https://www.sec.gov/files/company_tickers.json. This file contains all companies traded on the US stock exchange along with their company names and tickers.

Delisted Tickers:
RHT, TIF, CXO, GWR, PE, ZAYO, LOXO, ELLI, USG, TCF, CLGX, CMD, CTB
