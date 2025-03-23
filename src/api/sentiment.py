from textblob import TextBlob


def analyze_sentiment(text):
    """
    Performs sentiment analysis on the given text.

    :param text: News article content
    :return: Sentiment category (Positive, Negative, Neutral)
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":
    sample_text = "Tesla's latest innovation is groundbreaking!"
    print(analyze_sentiment(sample_text))  # Expected Output: Positive
