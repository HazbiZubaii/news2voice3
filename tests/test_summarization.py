import sys
import os

# Add the `src` directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from api.summarization import summarize_text

def test_summarization():
    """
    Test case for the summarization function.
    """
    article_content = """Tesla, the electric vehicle company led by Elon Musk, has been making headlines again. 
    Recent reports suggest that Tesla is expanding its operations in Asia while also dealing 
    with challenges in the U.S. market. Analysts predict that Tesla’s stock might see fluctuations 
    based on the upcoming quarterly earnings report."""

    summary = summarize_text(article_content, num_sentences=2)

    assert isinstance(summary, str), "Summary should be a string"
    assert len(summary) > 0, "Summary should not be empty"

    print("\n✅ Summarization test passed!")
    print("Generated Summary:", summary)

if __name__ == "__main__":
    test_summarization()


