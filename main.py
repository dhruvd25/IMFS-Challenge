from pickle5 import pickle
from utils.dbutils import *
import sqlite3
from utils.dataprep import *
import json
import requests

# resp = requests.get('https://www.sec.gov/files/company_tickers.json')
# company_ticker = resp.json()

# with open('./data/constituents_history.pkl', 'rb') as fp:
#     data = pickle.load(fp)

# daily_ticks = {}
# all_tickers = {}
# daily_price = {}

# for i in data.iterrows():
#     if len(i[1][0]) > 0:
#         daily_ticks[i[0]] = []
#         daily_price[i[0]] = []
#         for attribs in i[1][0]:
#             daily_ticks[i[0]].append(attribs[0])
#             daily_price[i[0]].append(attribs[11]['raw'])
#             if attribs[0] in all_tickers.keys():
#                 all_tickers[attribs[0]] += 1
#             else:
#                 all_tickers[attribs[0]] = 1

# valid_stocks = []
# for i, j in company_ticker.items():
#     if j['ticker'] in all_tickers.keys():
#         valid_stocks.append(j['ticker'])

# execute("DROP TABLE IF EXISTS historical_price")
# query = """CREATE TABLE historical_price (ticker text,
#                                         date text,
#                                         open real,
#                                         close real,
#                                         volume real,
#                                         PRIMARY KEY(ticker,date)) """
# execute(query)

# execute("DROP TABLE IF EXISTS ticker_info")
# query_ticker_info = """CREATE TABLE ticker_info (ticker text,
#                                         isin text,
#                                         sector real,
#                                         company_name text,
#                                         PRIMARY KEY(ticker,isin)) """
# execute(query_ticker_info)

# query_insert = '''INSERT INTO historical_price VALUES (?,?,?,?,?) '''
# for i in values:
#     executemany(query_insert,i)

# insert_query_tick_info = '''INSERT INTO ticker_info VALUES (?,?,?,?) '''
# executemany(insert_query_tick_info,tuple(ticker_inf0))
# date = '2018-01-02'
# query = f'''SELECT ROUND(SUM(open)/COUNT(open),2) index_open,
#                   ROUND(SUM(close)/COUNT(close),2) as index_close,
#                   ROUND(AVG(volume)) as avg_vol
#             FROM historical_price WHERE date='{date}' '''
# fetch(query,fetch_type='all',with_cols='true')
if __name__=='__main__':
    valid_stocks = ['A', 'AA', 'AAL', 'AAN', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABNB', 'ABT', 'ACA', 'ACAD', 'ACC', 'ACGL', 'ACHC', 'ACI', 'ACIW', 'ACM', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADNT', 'ADP', 'ADS', 'ADSK', 'ADT', 'AEE', 'AEO', 'AEP', 'AES', 'AET', 'AFG', 'AFL', 'AFRM', 'AGCO', 'AGIO', 'AGNC', 'AGO', 'AGR', 'AIG', 'AIRC', 'AIT', 'AIV', 'AIZ', 'AJG', 'AKAM', 'AKR', 'AL', 'ALB', 'ALE', 'ALEX', 'ALGM', 'ALGN', 'ALGT', 'ALK', 'ALKS', 'ALL', 'ALLE', 'ALLO', 'ALLY', 'ALNY', 'ALSN', 'ALV', 'ALXN', 'AMAT', 'AMCR', 'AMCX', 'AMD', 'AME', 'AMED', 'AMG', 'AMGN', 'AMH', 'AMP', 'AMRX', 'AMT', 'AMWL', 'AMZN', 'AN', 'ANET', 'ANGI', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APD', 'APH', 'APLE', 'APO', 'APTV', 'AR', 'ARE', 'ARES', 'ARMK', 'ARNC', 'ARRY', 'ARW', 'ASAN', 'ASB', 'ASGN', 'ASH', 'ATGE', 'ATH', 'ATHN', 'ATI', 'ATO', 'ATR', 'ATUS', 'ATVI', 'AVA', 'AVB', 'AVGO', 'AVIR', 'AVLR', 'AVNS', 'AVNT', 'AVT', 'AVTR', 'AVY', 'AWI', 'AWK', 'AXON', 'AXP', 'AXS', 'AXTA', 'AYI', 'AYX', 'AZO', 'AZPN', 'B', 'BA', 'BAC', 'BAH', 'BAX', 'BBBY', 'BBY', 'BC', 'BCO', 'BDC', 'BDN', 'BDX', 'BECN', 'BEN', 'BERY', 'BFAM', 'BG', 'BGCP', 'BGS', 'BHF', 'BIG', 'BIIB', 'BILL', 'BIO', 'BJ', 'BK', 'BKD', 'BKH', 'BKI', 'BKNG', 'BKR', 'BKU', 'BLI', 'BLK', 'BLKB', 'BLL', 'BLMN', 'BLUE', 'BMBL', 'BMRN', 'BMY', 'BOH', 'BOKF', 'BPMC', 'BPOP', 'BR', 'BRKR', 'BRO', 'BRX', 'BSX', 'BSY', 'BTU', 'BURL', 'BWA', 'BWXT', 
    'BX', 'BXMT', 'BXP', 'BXS', 'BYD', 'BYND', 'C', 'CA', 'CABO', 'CACC', 'CACI', 'CAG', 'CAH', 'CAKE', 'CAR', 'CARG', 'CARR', 'CARS', 'CASY', 'CAT', 'CATY', 'CB', 'CBOE', 'CBRE', 'CBRL', 'CBSH', 'CBT', 'CC', 'CCI', 'CCK', 'CCL', 'CDAY', 'CDEV', 'CDK', 'CDNS', 'CDW', 'CE', 'CEIX', 'CERN', 'CF', 'CFFN', 'CFG', 'CFR', 'CFX', 'CG', 'CGNX', 'CHD', 'CHDN', 'CHE', 'CHGG', 'CHH', 'CHK', 'CHRW', 'CHTR', 'CHWY', 'CHX', 'CI', 'CIEN', 'CIM', 'CINF', 'CIT', 'CL', 'CLB', 'CLH', 'CLI', 'CLR', 'CLVS', 'CLVT', 'CLX', 'CMA', 'CMC', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMP', 'CMPR', 'CMS', 'CNA', 'CNC', 'CNDT', 'CNK', 'CNO', 'CNP', 'CNX', 'CNXC', 'COF', 'COG', 'COHR', 'COIN', 'COLD', 'COLM', 'COMM', 'CONE', 'COO', 'COP', 'COR', 'COST', 'COTY', 'COUP', 'CPB', 'CPRI', 'CPRT', 'CPT', 'CR', 'CREE', 'CRI', 'CRL', 'CRM', 'CRNC', 'CRS', 'CRUS', 'CRWD', 'CSCO', 'CSGP', 'CSL', 'CSX', 'CTAS', 'CTLT', 'CTSH', 'CTVA', 'CTXS', 'CUBE', 'CUZ', 'CVA', 'CVET', 'CVI', 'CVLT', 'CVNA', 'CVS', 'CVX', 'CW', 'CWK', 'CXP', 'CXW', 'CZR', 'D', 'DAL', 'DAN', 'DAR', 'DASH', 'DBD', 'DBX', 'DCI', 'DCT', 'DD', 'DDD', 'DDOG', 'DDS', 'DE', 'DECK', 'DEI', 'DELL', 'DFS', 'DG', 'DGX', 'DHC', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DK', 'DKNG', 'DKS', 'DLB', 'DLR', 'DLTR', 'DLX', 'DNB', 'DNOW', 'DOC', 'DOCU', 'DOV', 'DOW', 'DOX', 'DPZ', 'DRE', 'DRH', 'DRI', 'DRQ', 'DT', 'DTE', 'DTM', 'DUK', 'DVA', 'DVN', 'DXC', 'DXCM', 'DY', 'EA', 'EAF', 'EAT', 'EBAY', 
    'EBS', 'ECL', 'ED', 'EDR', 'EEFT', 'EFX', 'EGP', 'EHC', 'EIX', 'EL', 'ELAN', 'ELS', 'EME', 'EMN', 'EMR', 'ENDP', 'ENPH', 'ENR', 'ENS', 'ENTG', 'EOG', 'EPAM', 'EPC', 'EPR', 'EQC', 'EQH', 'EQIX', 'EQR', 'EQT', 'ERIE', 'ES', 'ESGR', 'ESI', 'ESNT', 'ESS', 'ESTC', 'ETN', 'ETR', 'ETRN', 'ETSY', 'EVR', 'EVRG', 'EW', 'EWBC', 'EXAS', 'EXC', 'EXEL', 'EXP', 'EXPD', 'EXPE', 'EXR', 'EYE', 'F', 'FAF', 'FANG', 'FAST', 'FB', 'FBHS', 'FCFS', 'FCN', 'FCNCA', 'FCPT', 'FCX', 'FDS', 'FDX', 'FE', 'FEYE', 'FFIN', 'FFIV', 'FGEN', 'FHB', 'FHI', 'FHN', 'FICO', 'FIS', 'FISV', 'FITB', 'FIVE', 'FIVN', 'FIZZ', 'FL', 'FLO', 'FLR', 'FLS', 'FLT', 'FMC', 'FNB', 'FND', 'FNF', 'FOX', 'FOXA', 'FR', 'FRC', 'FRT', 'FSLR', 'FSLY', 'FTDR', 'FTI', 'FTNT', 'FTV', 'FUL', 'FULT', 'FWONA', 'FWONK', 'G', 'GATX', 'GBCI', 'GCP', 'GD', 'GDDY', 'GDOT', 'GDRX', 'GE', 'GEO', 'GGG', 'GH', 'GHC', 'GILD', 'GIS', 'GL', 'GLPI', 'GLW', 'GM', 'GME', 'GMED', 'GNRC', 'GNTX', 'GNW', 'GOOG', 'GOOGL', 'GPC', 'GPK', 'GPN', 'GPOR', 'GPS', 'GRA', 'GRMN', 'GRPN', 'GRUB', 'GS', 'GT', 'GTES', 'GTX', 'GWRE', 'GWW', 'H', 'HAE', 'HAIN', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCSG', 'HD', 'HE', 'HEI', 'HELE', 'HES', 'HFC', 'HGV', 'HHC', 'HI', 'HIG', 'HII', 'HIW', 'HLF', 'HLT', 'HNI', 'HOG', 'HOLX', 'HOMB', 'HON', 'HP', 'HPE', 'HPP', 'HPQ', 'HQY', 'HR', 'HRB', 'HRC', 'HRL', 'HSIC', 'HST', 'HSY', 'HTA', 'HUBB', 'HUBS', 'HUM', 'HUN', 'HWC', 'HWM', 'HXL', 'HZNP', 'IAA', 
    'IAC', 'IART', 'IBKR', 'IBM', 'IBOC', 'ICE', 'ICPT', 'ICUI', 'IDA', 'IDCC', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INGN', 'INGR', 'INT', 'INTC', 'INTU', 'INVH', 'IONS', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'ISBC', 'ISRG', 'IT', 'ITRI', 'ITT', 'ITW', 'IVR', 'IVZ', 'J', 'JACK', 'JAZZ', 'JBGS', 'JBHT', 'JBL', 'JBLU', 'JCI', 'JCOM', 'JEF', 'JHG', 'JKHY', 'JLL', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KAR', 'KBR', 'KDP', 'KEX', 'KEY', 'KEYS', 'KFY', 'KHC', 'KIM', 'KKR', 'KLAC', 'KLXE', 'KMB', 'KMI', 'KMPR', 'KMT', 'KMX', 'KNX', 'KO', 'KR', 'KRC', 'KRG', 'KSS', 'KSU', 'KTB', 'L', 'LAD', 'LAMR', 'LANC', 'LAZ', 'LAZR', 'LB', 'LBRDA', 'LBRDK', 'LBTYA', 'LBTYK', 'LC', 'LDOS', 'LEA', 'LECO', 'LEG', 'LEN', 'LEVI', 'LFUS', 'LGND', 'LH', 'LHCG', 'LHX', 'LII', 'LILA', 'LILAK', 'LIN', 'LITE', 'LIVN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNG', 'LNT', 'LOPE', 'LOW', 'LPLA', 'LPNT', 'LPX', 'LRCX', 'LSI', 'LSTR', 'LSXMA', 'LSXMK', 'LULU', 'LUMN', 'LUV', 'LVS', 'LW', 'LXP', 'LYB', 'LYFT', 'LYV', 'M', 'MA', 'MAA', 'MAC', 'MAN', 'MANH', 'MAR', 'MAS', 'MASI', 'MAT', 'MAXR', 'MCD', 'MCFE', 'MCHP', 'MCK', 'MCO', 'MCY', 'MD', 'MDB', 'MDGL', 'MDLZ', 'MDP', 'MDRX', 'MDT', 'MDU', 'MET', 'MFA', 'MGLN', 'MGM', 'MHK', 'MIC', 'MIDD', 'MKC', 'MKL', 'MKSI', 'MKTX', 'MLHR', 'MLI', 'MLM', 'MMC', 'MMM', 'MMS', 'MNST', 'MO', 'MOH', 'MON', 'MORN', 'MOS', 'MPC', 'MPW', 'MPWR', 'MRC', 'MRCY', 'MRK', 'MRNA', 'MRO', 'MRVI', 'MRVL', 'MS',
    'MSA', 'MSCI', 'MSFT', 'MSGE', 'MSGS', 'MSI', 'MSM', 'MTB', 'MTCH', 'MTD', 'MTDR', 'MTG', 'MTN', 'MTX', 'MTZ', 'MU', 'MUR', 'MUSA', 'MXIM', 'MYGN', 'NABL', 'NATI', 'NAV', 'NAVI', 'NBIX', 'NBR', 'NCLH', 'NCNO', 'NCR', 'NDAQ', 'NDSN', 'NEE', 'NEM', 'NEOG', 'NET', 'NEU', 'NEWR', 'NFG', 'NFLX', 'NGVT', 'NHI', 'NI', 'NJR', 'NKE', 'NKLA', 'NKTR', 'NLOK', 'NLSN', 'NLY', 'NNN', 'NOC', 'NOV', 'NOW', 'NRG', 'NRZ', 'NSC', 'NSP', 'NTAP', 'NTCT', 'NTNX', 'NTRS', 'NUAN', 'NUE', 'NUS', 'NUVA', 'NVAX', 'NVCR', 'NVDA', 'NVR', 'NVT', 'NWE', 'NWL', 'NWS', 'NWSA', 'NXPI', 'NXST', 'NYCB', 'NYT', 'O', 'OAS', 'OC', 'ODFL', 'ODP', 'OFC', 'OGE', 'OGN', 'OGS', 'OHI', 'OI', 'OII', 'OKE', 'OKTA', 'OLED', 'OLLI', 'OLN', 'OMC', 'OMF', 'OMI', 'ON', 'ONEM', 'OPEN', 'OPK', 'ORCL', 'ORI', 'ORLY', 'OSH', 'OSK', 'OTIS', 'OUT', 'OVV', 'OXY', 'OZK', 'PACW', 'PAG', 'PANW', 'PAY', 'PAYC', 'PAYX', 'PB', 'PBCT', 'PBF', 'PBH', 'PBI', 'PCAR', 'PCG', 'PCH', 'PCRX', 'PCTY', 'PDCE', 'PDCO', 'PDM', 'PEAK', 'PEB', 'PEG', 'PEGA', 'PEN', 'PEP', 'PFE', 'PFG', 'PFGC', 'PFPT', 'PG', 'PGR', 'PGRE', 'PH', 'PHM', 'PII', 'PINC', 'PINS', 'PK', 'PKG', 'PKI', 'PLAN', 'PLD', 'PLNT', 'PLTK', 'PLTR', 'PM', 'PNC', 'PNFP', 'PNM', 'PNR', 'PNW', 'PODD', 'POOL', 'POR', 'POST', 'POWI', 'PPC', 'PPD', 'PPG', 'PPL', 'PRA', 'PRAA', 'PRAH', 'PRG', 'PRGO', 'PRI', 'PRU', 'PSA', 'PSB', 'PSTG', 'PSX', 'PTC', 'PTEN', 'PTON', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QDEL', 
    'QRTEA', 'QRVO', 'QS', 'R', 'RAD', 'RAMP', 'RARE', 'RBC', 'RBLX', 'RCL', 'RDN', 'RDUS', 'RE', 'REG', 'REGN', 'REXR', 'REYN', 'REZI', 'RF', 'RGA', 'RGC', 'RGEN', 'RGLD', 'RH', 'RHI', 'RHP', 'RIG', 'RJF', 'RKT', 'RL', 'RLGY', 'RLI', 'RLJ', 'RMD', 'RNG', 'RNR', 'ROK', 'ROKU', 'ROL', 'ROP', 'ROST', 'RPAI', 'RPM', 'RPRX', 'RRC', 'RS', 'RSG', 'RTX', 'RVI', 'RYN', 'S', 'SABR', 'SAGE', 'SAIC', 'SAM', 'SATS', 'SAVE', 'SBAC', 'SBGI', 'SBH', 'SBNY', 'SBRA', 'SBUX', 'SC', 'SCHW', 'SCI', 'SEB', 'SEDG', 'SEE', 'SEIC', 'SF', 'SFM', 'SGEN', 'SGFY', 'SGMS', 'SHC', 'SHLS', 'SHO', 'SHOO', 'SHW', 'SIG', 'SIGI', 'SIRI', 'SITC', 'SITE', 'SIVB', 'SIX', 'SJI', 'SJM', 'SKT', 'SKX', 'SLAB', 'SLB', 'SLCA', 'SLG', 'SLGN', 'SLM', 'SM', 'SMAR', 'SMG', 'SMTC', 'SNA', 'SNAP', 'SNOW', 'SNPS', 'SNV', 'SNX', 'SO', 'SON', 'SPB', 'SPG', 'SPGI', 'SPLK', 'SPR', 'SQ', 'SR', 'SRC', 'SRCL', 'SRE', 'SRPT', 'SSNC', 'ST', 'STAY', 'STE', 'STL', 'STLD', 'STMP', 'STOR', 'STT', 'STWD', 'STX', 'STZ', 'SUI', 'SUM', 'SVC', 'SWI', 'SWK', 'SWKS', 'SWN', 'SWX', 'SXT', 'SYF', 'SYK', 'SYNA', 'SYNH', 'SYY', 'T', 'TAP', 'TCBI', 'TDC', 'TDG', 'TDOC', 'TDS', 'TDY', 'TECH', 'TEL', 'TEN', 'TER', 'TEX', 'TFC', 'TFSL', 'TFX', 'TGNA', 'TGT', 'THC', 'THG', 'THO', 'THS', 'TJX', 'TKR', 'TMO', 'TMUS', 'TMX', 'TNDM', 'TNET', 'TOL', 'TPL', 'TPR', 'TPX', 'TREE', 'TREX', 'TRGP', 'TRIP', 'TRMB', 'TRMK', 'TRN', 'TROW', 'TRU', 'TRV', 
    'TSCO', 'TSE', 'TSLA', 'TSN', 'TT', 'TTC', 'TTD', 'TTEK', 'TTWO', 'TUP', 'TW', 'TWLO', 'TWO', 'TWOU', 'TWTR', 'TXG', 'TXN', 'TXRH', 'TXT', 'TYL', 'U', 'UA', 'UAA', 'UAL', 'UBER', 'UBSI', 'UDR', 'UE', 'UFS', 'UGI', 'UHAL', 'UHS', 'UI', 'ULTA', 'UMBF', 'UMPQ', 'UNFI', 'UNH', 'UNIT', 'UNM', 'UNP', 'UNVR', 'UPS', 'UPST', 'URBN', 'URI', 'USB', 'USFD', 'USM', 'UTHR', 'UWMC', 'V', 'VAC', 'VAL', 'VC', 'VEEV', 'VER', 'VFC', 'VIA', 'VIAC', 'VIACA', 'VIAV', 'VICI', 'VIR', 'VIRT', 'VLO', 'VLY', 'VMC', 'VMEO', 'VMI', 'VMW', 'VNE', 'VNO', 'VNT', 'VOYA', 'VRNT', 'VRSK', 'VRSN', 'VRTX', 'VSAT', 'VSH', 'VST', 'VTR', 'VTRS', 'VVC', 'VVV', 'VZ', 'W', 'WAB', 'WAFD', 'WAL', 'WAT', 'WBA', 'WBS', 'WBT', 'WCC', 'WDAY', 'WDC', 'WEC', 'WELL', 'WEN', 'WEX', 'WFC', 'WH', 'WHR', 'WLK', 'WLL', 'WLTW', 'WM', 'WMB', 'WMG', 'WMT', 'WOOF', 'WOR', 'WORK', 'WPC', 'WPG', 'WRB', 'WRE', 'WRI', 'WRK', 'WSM', 'WSO', 'WST', 'WTFC', 'WTM', 'WTRG', 'WU', 'WW', 'WWD', 'WWE', 'WWW', 'WY', 'WYNN', 'X', 'XEC', 'XEL', 'XHR', 'XL', 'XLNX', 'XLRN', 'XM', 'XOM', 'XPO', 'XRAY', 'XRX', 'XYL', 'Y', 'YELP', 'YUM', 'Z', 'ZBH', 'ZBRA', 'ZEN', 'ZG', 'ZI', 'ZION', 'ZM', 'ZNGA', 'ZS', 'ZTS']

    from multiprocessing import Pool
    with Pool(5) as pool:
        ticker_info = pool.map(get_ticker_info,valid_stocks)

    with open('ticker_info.pkl', 'wb') as fp:
        pickle.dump(ticker_info, fp)
    print(ticker_info)