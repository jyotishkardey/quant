import pandas as pd
import os
from datetime import date

output_file = "../output.csv"

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

def update_frequencies(stocks):
    data_dict = {}
    # Check if the file does not exist
    if not os.path.exists(output_file):
        generate_New_csv(stocks)
    else:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(output_file)
        # Convert the DataFrame to a dictionary
        data_dict = df.to_dict(orient='records')
        print("--------")
        print(data_dict)
        '''
        if str(data_dict['Date']) == str(get_current_date()):
            return;
        else:
            data_dict['Date'] = get_current_date()
        '''
        for i in stocks:
            if i in data_dict and i != 'Date':
                data_dict[i] += 1
        df.to_csv(output_file, index=False, header=True)
        


def generate_New_csv(in_stocks):
    stocks = in_stocks.copy()
    stocks_dictionary = {}
    
    for stock in stocks:
        stocks_dictionary[stock] = 1
    stocks_dictionary['Date'] = get_current_date()
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(list(stocks_dictionary.items()), columns=['Stocks', 'Frequency'])
    df.to_csv(output_file, index=False, header=True)


