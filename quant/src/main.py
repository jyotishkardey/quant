import yfinance as yf
import pandas as pd
import talib
from datetime import datetime

#Utility APIS
from csv_utils import *
from whatsApp  import *
from settings  import *

# Function to check if the stock is in uptrend for the last week, 15 days and 1 month
def is_uptrend(data):
    if chek_uptrend == False:
        return
    return len(data['Close']) > 50 and data['Close'].iloc[-1] > data['Close'].iloc[-5]  and data['Close'].iloc[-5] > data['Close'].iloc[-15] and data['Close'].iloc[-15] > data['Close'].iloc[-25]

# Function to check RSI
def check_rsi(data):
    if enable_rsi == False:
        return
    rsi = talib.RSI(data['Close'], timeperiod=14)
    return rsi_lower_limit < rsi.iloc[-1] < rsi_upper_limit

# Function to check MACD buy signal
def check_macd(data):
    if enable_macd == False:
        return
    macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return macd.iloc[-1] > macdsignal.iloc[-1]

def check_adx(data):
    if enable_adx == False:
        return
    data['ADX'] = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=14)
    return data['ADX'].iloc[-1] > adx

def is_obv_increasing(data):
    if enable_obv == False:
        return
    # Calculate OBV
    data['OBV'] = talib.OBV(data['Close'], data['Volume'])

    # Calculate the difference in OBV
    data['OBV_Diff'] = data['OBV'].diff()

    # Get the last 5 elements
    last_few =data['OBV_Diff'][-1:]
    # Check if the OBV is increasing (most recent difference is positive)
    #return all(x > 0 for x in last_few)
    #Check if current OBV is greater than 15 days earlier's OBV
    return data['OBV'].iloc[-1] > data['OBV'].iloc[-15]

def compare_moving_average(data):
    if enable_moving_average == False:
        return
    # Calculate the 50-day and 200-day moving averages
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()
    # Check if the 50-day MA is greater than the 200-day MA
    if data['50_MA'].iloc[-1] > data['200_MA'].iloc[-1]:
        return True
    else:
        return False

def check_beta(ticker):
    if check_beta == False:
        return
    key_to_check = 'beta' 
    if key_to_check not in ticker.info:
        return False
    return ticker.info['beta'] < 1

def factor_momentum(data):
    if MOMENTUM_FACTOR == False:
        return
    return is_uptrend(data) and check_rsi(data) and check_macd(data) and is_obv_increasing(data) and compare_moving_average(data) and check_adx(data)

def factor_volatility(ticker):
    if VOLATILITY_FACTOR == False:
        return True
    return check_beta(ticker)

# Filter stocks based on criteria
def analyze_stoks():
    if ANALYZE_STOCKS == False:
        return
    messageBody = ""
    output = ""
    i = 0
    nifty_500_stocks = read_csv(input_data,'Symbol','.NS')
    company_names_column = read_csv_column(input_data,'Company Name')
    industry_column = read_csv_column(input_data,'Industry')
    filtered_stocks = []
    filtered_sector = []

    #Get 1 year time frame
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(years=1)

    for stock in nifty_500_stocks:
        i += 1
        print("Analysing " + str(i) + "  "+ company_names_column[i-1] + " ...")
        ticker =  yf.Ticker(stock)
        #Get 1 year data
        data = ticker.history(interval='1d', start=start_date, end=end_date)
        if factor_momentum(data) and factor_volatility(ticker):
            filtered_stocks.append(company_names_column[i-1])
            filtered_sector.append(industry_column[i-1])

    print("==============RESULTS==========")
    i = 0
    for stock in filtered_stocks:
        i += 1
        print (str(i) + ".  [" + stock + "]  " + filtered_sector[i-1])
        messageBody += str(i) + "  [" + stock + "]  " + filtered_sector[i-1] + "\n"
        #Send WhatsApp alert
        if(len(messageBody) > 1000):
            sendWhatsAppNotification(messageBody,enable_whatsapp_Notification)
            messageBody = ""
    update_frequencies(filtered_stocks, filtered_sector, stocks_output_file, dump_stock_to_file)

def analyze_mutual_funds():
    if ANALYZE_MUTUAL_FUNDS == False:
        return
    columns = ['Date']
    result    = []
    rows = []
    columns.append(fund_names)
    #Get 1 year time frame
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(years=1)

    i = 0
    for ticker_symbol in mutual_fund_ticker_symbols:
        i += 1
        ticker =  yf.Ticker(ticker_symbol)

        #Get 1 year data
        data = ticker.history(interval='1d', start=start_date, end=end_date)

        # Calculate percetage daily returns and round it to 2 decimal places
        data['Daily_Return'] = round(data['Close'].pct_change() * 100, 2)
        
        if i == 1:
            # The Date column might not be explicitly present in the DataFrame. 
            # Instead, the Date is likely part of the DataFrame index
            # Reset index to access Date column
            data.reset_index(inplace=True)

            # Display the daily returns
            datetime_str = str(data['Date'][-1:])
            date = datetime_str.split()
            result.append(date[1])

        return_val = data['Daily_Return'][-1:]
        result.append(return_val.values[0])

    print(columns)
    print(result)
    rows.append(result)
    result =[]
    dump_mutual_fund_data(columns, result, mutual_fund_output_file, dump_mutual_funds_to_file)
    

analyze_stoks()
analyze_mutual_funds()
