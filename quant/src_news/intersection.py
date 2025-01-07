import pandas as pd 

analysed_stocks_file_path = "../stoks_analysis.csv"
trending_stocks_file_path = "out/recent_articles.txt2025-01-06"

def find_intersection():
    stocks_df = pd.read_csv(analysed_stocks_file_path)
    trending_df = pd.read_csv(trending_stocks_file_path)
    # Find intersection
    intersection = stocks_df[df['Stocks'].isin(df['Stocks'])]

    print("==================INTERSECTION===========")
    print(intersection)




find_intersection()