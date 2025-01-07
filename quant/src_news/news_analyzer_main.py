import feedparser
from datetime import datetime, timedelta
from settings import *
from utils     import *
import pandas as pd

def generateTrendingStocks():
    stock_column = read_csv_column(input_data,'Company Name')
    trending_stocks = {}
    count = 0

    current_date = datetime.now().date()
    appended_file_name = file_name + str(current_date)
    '''
    if os.path.exists(appended_file_name):
        print(f"\n\n\nThe file{file_name} exits. Skipping")
        return True
    '''
    i = 0
    for stock in stock_column:
        i += 1
        print(f"Counting word occurences for Stock #{i}.  {stock}")
        first_word = stock.split()[0]
        count = count_word_occurrences(appended_file_name, first_word)

        if count != 0:
            trending_stocks[stock] = count

    trending_stocks_df = pd.DataFrame({'Stocks': trending_stocks.keys(), 'Frequncy':trending_stocks.values()})
    print("============================")
    print(trending_stocks_df)
    trending_stocks_df.to_csv(trending_stocks_output_file, index=False, header=True)

def main():
    global enable_file_dump
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Get the current date and time
    current_date = datetime.now()

    # Calculate the date 5 days ago
    five_days_ago = current_date - timedelta(days=5)

    # Filter articles that are less than 5 days old
    recent_articles = []
    for entry in feed.entries:
        article_date = datetime(*entry.published_parsed[:6])
        if article_date > five_days_ago:
            recent_articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": article_date
            })

    if article_file_exists():
        enable_file_dump = False

    # Print the recent articles
    for article in recent_articles:
        print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
        dump_to_file(article)
       
    generateTrendingStocks()
    
    # Example output when articles are not found
    if not recent_articles:
        print("No recent articles found that are less than 5 days old.")

    if enable_file_dump == False:
        print("\n\n\n SKIPPING FILE DUMP AS FILE ALREADY EXISTS")


main()