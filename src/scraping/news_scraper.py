import feedparser
import urllib.parse
import logging
from newspaper import Article  # Import newspaper3k

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

def get_news_articles(topic):
    """Scrape Google News RSS for a given topic and extract article content."""
    encoded_topic = urllib.parse.quote(topic)  # Encode spaces and special characters
    url = f"https://news.google.com/rss/search?q={encoded_topic}&hl=en-US&gl=US&ceid=US:en"

    logging.info(f"Fetching news from: {url}")
    feed = feedparser.parse(url)

    if feed.entries:
        articles = []
        for entry in feed.entries[:5]:  # Limit to top 5 articles
            title = entry.title
            link = entry.link

            # Extract content from the article URL
            article = Article(link)
            article.download()
            article.parse()
            content = article.text.strip()  # Extract article text content

            # Generate a simple summary (you can improve this with advanced summarization techniques)
            summary = content[:300]  # Take the first 300 characters as a basic summary

            articles.append({
                "title": title,
                "summary": summary,
                "link": link
            })

        return articles
    else:
        logging.warning("⚠️ No articles found.")
        return []














