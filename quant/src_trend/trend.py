import feedparser
import re

# Define the RSS feed URL for Google News search
rss_url = "https://news.google.com/rss/search?q=trending+stocks+Indian+stock+market&hl=en-IN&gl=IN&ceid=IN:en"

# Parse the RSS feed
news_feed = feedparser.parse(rss_url)

# Function to extract stock names from article titles
def extract_stock_names(title):
    # Regular expression pattern to find stock names (assuming they are in uppercase letters)
#    pattern = r'\b[A-Z]{2,}\b'
    pattern1 = r'\b([A-Z]+(?:, [A-Z]+)*)\b'
    pattern2 = r'([\w\s,&]+)\b'

    matches1= re.findall(pattern1, title)
    matches2 = re.findall(pattern2, title)
    # Combine and return unique stock names
    stock_names = list(set(matches1 + matches2))
    return stock_names

# Extract and display the news articles and their related stock names
print("Trending Stocks in Indian Stock Market:")
for entry in news_feed.entries:
    title = entry.title
    stock_names = extract_stock_names(title)
    print(f"Title: {title}")
    print(f"Stock Names: {', '.join(stock_names) if stock_names else 'None found'}")
#    print(f"Link: {entry.link}")
    print()

