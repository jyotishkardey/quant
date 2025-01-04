#Stocks
dump_stock_to_file = True
stocks_output_file = "/home/jyotishkardey/quant/stoks_analysis.csv"
input_data='/home/jyotishkardey/quant/ind_nifty500list.csv'

#WhatsApp Settings

enable_whatsapp_Notification = False

#Check uptrend
chek_uptrend = True

#RSI
enable_rsi = True
rsi_lower_limit = 50
rsi_upper_limit = 80

#MACD
enable_macd = True

#ADX
enable_adx = True
adx=12

#obv
enable_obv = True

#moving average
enable_moving_average = True

#Enable Beta
check_beta = True

#FACTORS
MOMENTUM_FACTOR = True
VOLATILITY_FACTOR = False

ANALYZE_STOCKS=True

#Mutual Funds
ANALYZE_MUTUAL_FUNDS = True
dump_mutual_funds_to_file=True
top_funds_ctr = 3
enable_frequncy_distribution_top_funds = True

#Sector Analysis
ANALYZE_SECTORS = True
indian_sectoral_indices = [
    '^NSEI',  # NIFTY 50
    '^NSEBANK',  # NIFTY Bank
    'BSE-MIDCAP.BO',  # BSE Midcap
    'BSE-SMLCAP.BO',  # BSE Smallcap
    'NIFTY_TOTAL_MKT.NS',  # NIFTY Total Market
    '^CNXAUTO',  # NIFTY Auto
    '^CNXENERGY',  # NIFTY Energy
    '^CNXIT',  # NIFTY IT
    '^CNXPHARMA',  # NIFTY Pharma
    'NIFTY_HEALTHCARE.NS',  # NIFTY Healthcare
    '^CNXSERVICE',  # NIFTY Services
    '^CNXCONSUM',  # NIFTY Consumption
    '^CNXREALTY',  # NIFTY Realty
    'NIFTY_OIL_AND_GAS.NS',  # NIFTY Oil & Gas
    '^CNXFMCG',  # NIFTY FMCG
    '^CNXINFRA',  # NIFTY Infrastructure
]

periods = [5, 15, 30, 90]  # 5 days, 15 days, 1 month (30 days), 3 months (90 days)
filename = '../sector_returns.csv'

mutual_fund_output_file = "/home/jyotishkardey/quant/fund_analysis.csv"
fund_names = ['Motilal Oswal Flexicap', 'Invesco Focused Fund', 'Quant Flexicap', 'HDFC Flexicap', 'Axis Flexicap','DSP Flexicap','DSP Focused Fund','Invesco Flexicap','PGIM Flexicap','Motilal Midcap','SBI Flexicap','PPFAS Flexicap']
mutual_fund_ticker_symbols = ['0P00012ZRM.BO','0P0001KMZA.BO','0P0000IQJ7.BO','0P00005WLZ.BO','0P0001BURF.BO','0P00005V93.BO','0P0001B9ZE.BO','0P0001OAAY.BO','0P00015I1S.BO','0P00012ALU.BO','0P0000XVL2.BO','0P0000YWL1.BO']