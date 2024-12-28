import yfinance as yf
import pandas as pd
import talib

# Function to check if the stock is in uptrend for the last 15 days
def is_uptrend(data):
    return data['Close'].iloc[-1] > data['Close'].iloc[0]

# Function to check RSI
def check_rsi(data):
    rsi = talib.RSI(data['Close'], timeperiod=14)
    return 50 < rsi[-1] < 80

# Function to check MACD buy signal
def check_macd(data):
    macd, macdsignal, macdhist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return macd[-1] > macdsignal[-1]

# Get list of Nifty 500 stocks (assuming this list is available)
nifty_500_stocks = ['RELIANCE.NS']  # Add all Nifty 500 stocks here

# Filter stocks based on criteria
filtered_stocks = []
for stock in nifty_500_stocks:
    ticker =  yf.Ticker(stock)
    data = ticker.history(period='1mo')
    if is_uptrend(data) and check_rsi(data) and check_macd(data):
        filtered_stocks.append(stock)

print("Filtered Stocks:", filtered_stocks)

