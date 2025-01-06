import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Define the URL for Google News search
url = "https://news.google.com/search?q=Indian+stock+market&hl=en-IN&gl=IN&ceid=IN:en"

# Add headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a request to the URL
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Print the HTML content for debugging
#print(soup.prettify())

# Get the current date and time
current_date = datetime.now()

# Calculate the date 5 days ago
five_days_ago = current_date - timedelta(days=5)

# Find news articles
articles = soup.select("article")

# Check if articles are found
if not articles:
    print("No articles found. Check if the class name has changed.")

# Filter articles that are less than 5 days old
recent_articles = []
for article in articles:
    date_tag = article.find("time")
    if date_tag:
        date_str = date_tag.get("datetime")
        if date_str:
            article_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
            if article_date > five_days_ago:
                title_tag = article.find("h3")
                if title_tag:
                    title = title_tag.get_text(strip=True)
                    link_tag = article.find("a", href=True)
                    if link_tag:
                        link = link_tag["href"]
                        if link.startswith("/"):
                            link = "https://news.google.com" + link
                        recent_articles.append((title, link))

# Print the recent articles
for title, link in recent_articles:
    print(f"Title: {title}\nLink: {link}\n")

# Example output when articles are not found
if not recent_articles:
    print("No recent articles found that are less than 5 days old.")
