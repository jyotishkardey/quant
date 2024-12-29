import yfinance as yf
import pandas as pd
import talib
from datetime import datetime

#Utility APIS
from csv_utils import *
from whatsApp  import *

# Function to check if the stock is in uptrend for the last week, 15 days and 1 month
def is_uptrend(data):
    return len(data['Close']) > 50 and data['Close'].iloc[-1] > data['Close'].iloc[-25]  and data['Close'].iloc[-1] > data['Close'].iloc[-5] and data['Close'].iloc[-15]

# Function to check RSI
def check_rsi(data):
    rsi = talib.RSI(data['Close'], timeperiod=14)
    return 50 < rsi.iloc[-1] < 80

# Function to check MACD buy signal
def check_macd(data):
    macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return macd.iloc[-1] > macdsignal.iloc[-1]



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
        if is_uptrend(data) and check_rsi(data) and check_macd(data):
            filtered_stocks.append(stock)

    print("==============RESULTS==========")
    i = 0
    for stock in filtered_stocks:
        i += 1
        print (str(i) + ".  " + stock)
        messageBody += str(i) + "  " + str(stock) + "\n"
        '''
        #Send WhatsApp alert
        if(len(messageBody) > 1000):
            sendWhatsAppNotification(messageBody)
            messageBody = ""
        '''
main()
