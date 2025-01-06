import feedparser
from datetime import datetime, timedelta
from settings import *

def dump_to_file(article):
    if dump_to_file == False:
        return

    # Write the recent articles to a file
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"Title: {article['title']}\n")
        file.write(f"Link: {article['link']}\n")
        file.write(f"Published: {article['published']}\n\n")


def count_word_occurrences(file_path, word):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert text to lowercase for case-insensitive matching

    # Tokenize the text into words
    words = text.split()

    # Count the occurrences of the given word
    word_count = words.count(word.lower())

    return word_count




