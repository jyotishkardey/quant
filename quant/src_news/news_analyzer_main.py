import feedparser
from datetime import datetime, timedelta
from settings import *
from utils     import *

def main():
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

    # Print the recent articles
    for article in recent_articles:
        print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
        dump_to_file(article)
    
    # Example output when articles are not found
    if not recent_articles:
        print("No recent articles found that are less than 5 days old.")



main()