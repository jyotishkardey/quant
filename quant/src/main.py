import yfinance as yf
import pandas as pd
import talib
from datetime import datetime

#Utility APIS
from csv_utils import *
from whatsApp  import *

# Function to check if the stock is in uptrend for the last week, 15 days and 1 month
def is_uptrend(data):
    return len(data['Close']) > 50 and data['Close'].iloc[-1] > data['Close'].iloc[-5]  and data['Close'].iloc[-5] > data['Close'].iloc[-15] and data['Close'].iloc[-15] > data['Close'].iloc[-25]

# Function to check RSI
def check_rsi(data):
    rsi = talib.RSI(data['Close'], timeperiod=14)
    return 50 < rsi.iloc[-1] < 80

# Function to check MACD buy signal
def check_macd(data):
    macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return macd.iloc[-1] > macdsignal.iloc[-1]

def check_adx(data):
    data['ADX'] = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=14)
    return data['ADX'].iloc[-1] > 12

def is_obv_increasing(data):
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
    # Calculate the 50-day and 200-day moving averages
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()
    # Check if the 50-day MA is greater than the 200-day MA
    if data['50_MA'].iloc[-1] > data['200_MA'].iloc[-1]:
        return True
    else:
        return False

def check_beta(ticker):
    key_to_check = 'beta' 
    if key_to_check not in ticker.info:
        return False
    return ticker.info['beta'] < 1

def factor_momentum(data):
    return is_uptrend(data) and check_rsi(data) and check_macd(data) and is_obv_increasing(data) and compare_moving_average(data) and check_adx(data)

def factor_volatility(ticker):
    return check_beta(ticker)

# Filter stocks based on criteria
def main():
    messageBody = ""
    output = ""
    i = 0
    nifty_500_stocks = read_csv('../ind_nifty500list.csv','Symbol','.NS')
    filtered_stocks = []

    #Get 1 year time frame
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(years=1)

    for stock in nifty_500_stocks:
        i += 1
        print("Analysing " + str(i) + "  "+ stock + " ...")
        ticker =  yf.Ticker(stock)
        #Get 1 year data
        data = ticker.history(interval='1d', start=start_date, end=end_date)
        if factor_momentum(data): #and factor_volatility(ticker):
            filtered_stocks.append(stock)

    print("==============RESULTS==========")
    i = 0
    for stock in filtered_stocks:
        i += 1
        print (str(i) + ".  " + stock)
        messageBody += str(i) + "  " + str(stock) + "\n"
        #Send WhatsApp alert
        if(len(messageBody) > 1000):
            sendWhatsAppNotification(messageBody)
            messageBody = ""
main()
