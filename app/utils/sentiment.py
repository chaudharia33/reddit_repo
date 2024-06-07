from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_vader(sentence: str):
    """
    Analyzes the sentiment of a given sentence using Vader sentiment analysis.

    Args:
        sentence (str): The sentence to analyze.

    Returns:
        str: The sentiment label ('positive', 'negative', or 'neutral').
    """
    # Initialize Vader sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Analyze sentiment of the sentence
    sentiment_scores = analyzer.polarity_scores(sentence)

    # Determine sentiment based on compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment_scores, sentiment

def analyze_sentiment_textblob(sentence: str):
    """
    Analyzes the sentiment of a given sentence using TextBlob sentiment analysis.

    Args:
        sentence (str): The sentence to analyze.

    Returns:
        str: The sentiment label ('positive', 'negative', or 'neutral').
    """
    # Create a TextBlob object
    blob = TextBlob(sentence)
    
    # Get the sentiment polarity
    sentiment_scores = blob.sentiment.polarity

    # Determine sentiment based on polarity
    if sentiment_scores > 0:
        sentiment = "positive"
    elif sentiment_scores < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment_scores, sentiment