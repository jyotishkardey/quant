import pandas as pd
import os
from datetime import date

import pandas as pd

def read_csv_column(file_path, column_name):
    df = pd.read_csv(file_path)
    return df[column_name].tolist()

def get_current_date():
    # Get the current date
    return date.today()

def read_csv(file, column, suffix):
    ret = []
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Get a list of all values from a specific column 
    column_values = df[column].tolist()
   
    #Add .NS suffix indication NSE . This format is required for yfinance lib
    for stock in column_values:
        stock_suffixed = stock + suffix
        ret.append(stock_suffixed)
    
    return ret

def update_frequencies(stocks,output_file):
    data_dict = {}
    # Check if the file does not exist
    if not os.path.exists(output_file):
        generate_New_csv(stocks,output_file)
    else:
        stock_column = read_csv_column(output_file,'Stocks')
        frequency_column = read_csv_column(output_file,'Frequency')

        stock_dict = {}
        i = 0
        for stock in stock_column:
            stock_dict[stock] = frequency_column[i]
            i+= 1

        if str(stock_dict['Date']) == str(get_current_date()):
            return;
        else:
            data_dict['Date'] = get_current_date()
        
        for i in stocks:
            if i != 'Date':
                stock_dict[i] = int(stock_dict[i]) +int(1)
        
        df = pd.DataFrame({'Stocks': stock_dict.keys(), 'Frequency' :stock_dict.values()})
        df.to_csv(output_file, index=False, header=True)

def generate_New_csv(in_stocks,output_file):
    stocks = in_stocks.copy()
    stocks_dictionary = {}
    
    for stock in stocks:
        stocks_dictionary[stock] = 1
    stocks_dictionary['Date'] = get_current_date()
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(list(stocks_dictionary.items()), columns=['Stocks', 'Frequency'])
    df.to_csv(output_file, index=False, header=True)


