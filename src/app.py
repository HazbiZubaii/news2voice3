import nltk
import os
import streamlit as st
from googletrans import Translator  # Importing Google Translator
from api.sentiment import analyze_sentiment
from api.summarization import summarize_text
from api.tts import text_to_speech
from scraping.news_scraper import get_news_articles  # Import the scraper

# Explicitly define NLTK data directory
nltk_data_path = os.path.join(os.path.expanduser("~"), "nltk_data")
nltk.data.path.append(nltk_data_path)

# Ensure 'punkt' is downloaded
nltk.download('punkt', download_dir=nltk_data_path)

# Streamlit App Title
st.title("📰 News Summarization & Hindi TTS")
st.subheader("Made by Hasbi Fathima VP")

# User Input
company_name = st.text_input("Enter company name:", "Tesla")

if st.button("Fetch News"):
    # Fetching news articles using the get_news_articles function from news_scraper.py
    articles = get_news_articles(company_name)

    if not articles:
        st.warning("⚠️ No news found. Try another company name.")
    else:
        report = []
        for article in articles:
            title = article.get("title", "No Title Available")
            summary = article.get("summary", "No summary available.")
            link = article.get("link", "#")

            # Analyzing sentiment using the title
            sentiment = analyze_sentiment(title)

            report.append({
                "Title": title,
                "Summary": summary,
                "Sentiment": sentiment,
                "Link": link
            })

        for item in report:
            st.subheader(item["Title"])
            st.write(item["Summary"])
            st.write(f"Sentiment: **{item['Sentiment']}**")
            st.write(f"[Read More]({item['Link']})")

        # Generate Hindi Speech based on Titles
        combined_text = " ".join([item["Title"] for item in report])

        # Check if combined_text is not empty or None
        if combined_text and isinstance(combined_text, str) and combined_text.strip():
            # Translate the combined text to Hindi using Google Translate
            translator = Translator()
            translated_text = translator.translate(combined_text, src='en', dest='hi').text

            # Generate Hindi Speech using translated text
            audio_file = text_to_speech(translated_text, lang="hi")
            st.audio(audio_file, format="audio/mp3")
        else:
            st.warning("⚠️ No valid titles available for text-to-speech.")







