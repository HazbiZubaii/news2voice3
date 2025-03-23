import sys
import os

# Ensure 'src' is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from scraping.news_scraper import get_news_articles

company_name = "Tesla"
articles = get_news_articles(company_name)

for article in articles:
    print(f"Title: {article.get('title', 'No Title')}")
    print(f"Content: {article.get('content', 'No Content')}")
    print(f"Link: {article.get('link', 'No Link')}")
    print("-" * 50)
