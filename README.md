# News2Voice: News Summarization, Sentiment Analysis, and Text-to-Speech Application

![Alt Text](https://github.com/HazbiZubaii/news2voice3/blob/main/Screenshot%202025-03-23%20111412.png)

## Project Overview
News2Voice is a web-based application that performs news extraction, sentiment analysis, comparative sentiment analysis, and generates a Text-to-Speech (TTS) output in Hindi for a given company's news articles. The application enables users to input a company name, fetch news articles, analyze sentiment, summarize the content, and play a Hindi speech output for the summarization. This project leverages modern NLP techniques, sentiment analysis, and machine learning to offer a structured and accessible news experience.

## Objective
The application achieves the following:

Extracts the title, summary, and other relevant metadata from at least 10 unique news articles related to a given company.

Performs sentiment analysis on each article (positive, negative, neutral).

Conducts comparative sentiment analysis to derive insights into how the company's news coverage varies.

Converts the summarized news content into Hindi speech using an open-source TTS engine.

Provides a simple web interface using Streamlit where users can input a company name and receive a sentiment report and audio output.

## Key Features
News Extraction: Automatically scrapes news articles for any given company name, extracting the title, summary, and relevant metadata.

Sentiment Analysis: Classifies each article’s sentiment into positive, negative, or neutral categories.

Comparative Sentiment Analysis: Compares sentiment scores across multiple articles to give insights into how a company's news coverage is perceived.

Summarization: Generates concise summaries of each news article.

Text-to-Speech (TTS): Converts summarized content into Hindi speech for an interactive experience.

User-Friendly Interface: Built using Streamlit, allowing users to input the company name and receive both a sentiment report and audio output.

## Technologies Used
Streamlit: For the interactive web interface.

BeautifulSoup (bs4): For web scraping news articles from non-JavaScript websites.

NLTK: For text preprocessing and tokenization.

VADER Sentiment Analyzer: A lexicon and rule-based sentiment analysis tool.

Google Translate API: For translating the article titles to Hindi.

gTTS (Google Text-to-Speech): To convert text into speech.

API (Flask): For backend API development to communicate between frontend and backend.

## Project Setup and Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/News2Voice.git
cd News2Voice
2. Set up a Python Virtual Environment
Create a virtual environment to manage dependencies:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3. Install Required Dependencies
Install the necessary Python libraries using:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the Streamlit App
To start the application, run:

bash
Copy
Edit
streamlit run app.py
This will open the app in your browser, where you can input a company name and get the output.

## API Development
Overview of API Endpoints
The application has backend APIs to handle the extraction of news, sentiment analysis, comparative analysis, and text-to-speech conversion.

POST /api/get_news: Accepts a company name, fetches relevant news articles using the News Scraper script.

POST /api/sentiment_analysis: Analyzes the sentiment of the extracted news articles.

POST /api/comparative_analysis: Performs comparative sentiment analysis between the fetched news articles.

POST /api/tts: Converts the summarized content into speech using gTTS and returns a playable audio file.

## Assumptions & Limitations
The scraper only fetches news from non-JS web pages that can be parsed using BeautifulSoup.

The sentiment analysis is performed on the content and title only; multimedia content such as images and videos are not considered.

Hindi translation is limited to the title of the article.

The number of fetched articles might vary depending on the availability of news.

## Deployment
The application is deployed on Hugging Face Spaces for testing. You can access it via the following link: Hugging Face Deployment Link
## Conclusion
This project provides an interactive tool to fetch, summarize, analyze, and voice company news articles. By using NLP techniques, sentiment analysis, and TTS in Hindi, the app makes news consumption more accessible and engaging.

## License
This project is open-source and available under the MIT License. 
