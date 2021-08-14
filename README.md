## IMFS Data Engineering Challenge

## Utility functions
- __./utils/dbutils__: Database utility function to query and write against database. Current code hardcodes database location in class, should be modified to pass another location 

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
- RHT: No data found, symbol may be delisted
- TIF: No data found, symbol may be delisted
- CXO: No data found, symbol may be delisted
- GWR: No data found, symbol may be delisted
- PE: No data found, symbol may be delisted
- ZAYO: No data found, symbol may be delisted
- LOXO: No data found, symbol may be delisted
- ELLI: No data found, symbol may be delisted
- USG: No data found, symbol may be delisted
- TCF: No data found, symbol may be delisted
- CLGX: No data found, symbol may be delisted
- CMD: No data found, symbol may be delisted
- CTB: No data found, symbol may be delisted

