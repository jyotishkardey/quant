import pandas as pd

output_file = "../output.csv"

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


def dump_csv(stocks):
    # Create a DataFrame from the list
    df = pd.DataFrame(stocks, columns=["Stocks"])

    # Write the DataFrame to a file
    df.to_csv(output_file, index=False, header=True)


