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

def update_frequencies(stocks, sectors, output_file, dump_stock_to_file, date_val):
    if dump_stock_to_file == False:
        return

    # Check if the file does not exist
    if not os.path.exists(output_file):
        generate_New_csv(stocks, sectors, output_file, date_val)
    else:
        stock_column = read_csv_column(output_file,'Stocks')
        frequency_column = read_csv_column(output_file,'Frequency')
        sector_column = read_csv_column(output_file,'Sector')

        new_entrant_stocks = []
        new_entrant_sector = []
        current_date = ""

        stock_dict = {}
        i = 0

        #Create a dictionary containing all stocks and frequencies form the csv
        for stock in stock_column:
            stock_dict[stock] = frequency_column[i]
            i+= 1
        

        #Delete the Date field. Will add after stocks are added to maintain
        #correct postion
        del stock_dict['Date']
        #Remove the corresponding field from sector column
        sector_column.pop()
            
        
        i = 0
        #Iterate through the calculated stocks
        for stock in stocks:
            i += 1
            # If the stock exists in csv increment frequency counter
            if stock in stock_column :
                stock_dict[stock] = int(stock_dict[stock]) + int(1)
            #If the stock is a new entry add to new entr
            else:
                new_entrant_stocks.append(stock)
                new_entrant_sector.append(sectors[i-1])

        #Dump the new stocks which were not in csv to the dictionary
        for stock in new_entrant_stocks:
            stock_dict[stock] = 1
        
        #Insert the new entrant sectors at the second last postion of sector column  just
        # before the Date field
        sector_column = sector_column + new_entrant_sector
        sector_column.append('NULL') # For Date field

        #Add the date since it was deleted from dictionary and population of stocks is completed
        stock_dict['Date'] = date_val
        df = pd.DataFrame({'Stocks': stock_dict.keys(), 'Sector': sector_column, 'Frequency' :stock_dict.values()})
        df.to_csv(output_file, index=False, header=True)

def generate_New_csv(in_stocks, sectors, output_file, date_val):
    stocks = in_stocks.copy()
    stocks_dictionary = {}
    
    for stock in stocks:
        stocks_dictionary[stock] = 1
    stocks_dictionary['Date'] = date_val
    sectors.append('NULL') # To make lists of same length
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame({'Stocks': stocks_dictionary.keys(), 'Sector': sectors, 'Frequency' :stocks_dictionary.values()})
    df.to_csv(output_file, index=False, header=True)

def dump_mutual_fund_data(column_list, data_list, mutual_fund_output_file, dump_mutual_funds_to_file, date):
    existing_date_list = []

    if dump_mutual_funds_to_file == False:
        return 

    header_flag = False
    mode_flag = 'a' #Append
 
    
    # Check if the file does not exist, add header to the csv file
    if not os.path.exists(mutual_fund_output_file):
        header_flag = True
        mode_flag = 'w'

    #File exists

    #Check if latest data is present. If yes skip
    if os.path.exists(mutual_fund_output_file):
        existing_date_list = read_csv_column(mutual_fund_output_file, 'Date')
        if date in  existing_date_list:
            return

    df = pd.DataFrame(data_list, columns=column_list)
    df.to_csv(mutual_fund_output_file, index=False, header=header_flag, mode=mode_flag)


def frequncy_distribution_top_funds(enable_frequncy_distribution_top_funds, mutual_fund_output_file ,top_funds_ctr):

    if enable_frequncy_distribution_top_funds == False:
        return

    if not os.path.exists(mutual_fund_output_file):
        print("Can not calculate Frequency distribuiton of top funds as file does not exist")
        return

    for i in range(top_funds_ctr):
        print(i)
        column_name = "Rank_" + str(i+1)

        # Load the CSV file into a DataFrame
        df = pd.read_csv(mutual_fund_output_file)

        # Assuming the column you want to analyze is named 'column_name'
        frequency_distribution = df[column_name].value_counts()

        print("\n\n")
        print(frequency_distribution)