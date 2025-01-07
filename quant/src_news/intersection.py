import pandas as pd 

analysed_stocks_file_path = "../stoks_analysis.csv"
trending_stocks_file_path = "out/trending_stocks_output_file.csv"

def find_intersection():
    import pandas as pd

    # Load the CSV files
    file1 = analysed_stocks_file_path
    file2 = trending_stocks_file_path

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Specify the columns you want to compare
    column1 = 'Stocks'
    column2 = 'Stocks'

    # Find common values using intersection
    common_values = pd.Series(list(set(df1[column1]).intersection(set(df2[column2]))))

    # Print the common values
    print(common_values)


find_intersection()