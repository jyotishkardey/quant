import feedparser
from datetime import datetime, timedelta
import os
import pandas as pd

from settings import *

def read_csv_column(file_path, column_name):
    df = pd.read_csv(file_path)
    return df[column_name].tolist()

def article_file_exists():
    # Get the current date and time
    current_date = datetime.now().date()

    appended_file_name = file_name + str(current_date)

    if os.path.exists(appended_file_name):
        print(f"\n\n\nThe file{file_name} exits. Skipping")
        return True
    return False


def dump_to_file(article):
    if enable_file_dump == False:
        return

    # Get the current date and time and populate file name
    current_date = datetime.now().date()
    appended_file_name = file_name + str(current_date)

    # Write the recent articles to a file
    with open(appended_file_name, "a", encoding="utf-8") as file:
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




