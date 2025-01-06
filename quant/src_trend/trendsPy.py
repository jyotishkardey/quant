import trendspy as ts

# Initialize the TrendsPy client
client = ts.Trends()

# Define the search term
search_term = 'Python programming'

# Fetch related keywords
related_keywords = client.related_queries(search_term, headers={'referer': 'https://www.google.com/'})

# Display related keywords
for query in related_keywords:
    print(query)

