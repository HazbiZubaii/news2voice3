import nltk
import os

# Explicitly define NLTK data directory
nltk_data_path = os.path.join(os.path.expanduser("~"), "nltk_data")
nltk.data.path.append(nltk_data_path)

# Ensure 'punkt' is downloaded
nltk.download('punkt', download_dir=nltk_data_path)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def summarize_text(text, num_sentences=3):
    """
    Summarizes the given text using LSA summarization.

    :param text: The article content.
    :param num_sentences: Number of sentences in the summary (default 3).
    :return: Summary text.
    """
    # Debug: Check if the function is receiving the text properly
    print(f"\n🔍 DEBUG: Received text for summarization (first 200 chars):\n{text[:200]}\n")

    if not text.strip():
        print("⚠️ Empty article content received! Skipping summarization.")  # Debugging
        return "No summary available."

    try:
        print(f"📌 Processing text (first 100 chars): {text[:100]}...")  # Debugging

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, num_sentences)

        summary_text = " ".join(str(sentence) for sentence in summary)

        # Debug: Show generated summary
        print(f"✅ Generated Summary (first 200 chars):\n{summary_text[:200]}\n")

        return summary_text if summary_text else "Summary could not be generated."

    except Exception as e:
        print(f"❌ Summarization failed: {str(e)}")  # Debugging
        return f"Summarization failed: {str(e)}"


if __name__ == "__main__":
    sample_article = """Tesla has launched a new electric car. It has great features and improved battery life. 
    This new model is expected to dominate the EV market. Experts believe this will revolutionize the industry."""

    print("Generated Summary:", summarize_text(sample_article))




