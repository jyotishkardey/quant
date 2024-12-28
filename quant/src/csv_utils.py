import pandas as pd

def read_csv(file, column):
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Get the list of column names
    columns = df.columns.tolist()
    
    # Print the list of columns
    print(columns)

