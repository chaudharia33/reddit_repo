import unittest
from ..utils.sentiment import analyze_sentiment_vader

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment_vader_positive(self):
        self.assertEqual(analyze_sentiment_vader("I love this product!"), "positive")

    def test_analyze_sentiment_vader_negative(self):
        self.assertEqual(analyze_sentiment_vader("I hate this product!"), "negative")

    def test_analyze_sentiment_vader_neutral(self):
        self.assertEqual(analyze_sentiment_vader("This product is okay."), "neutral")

if __name__ == "__main__":
    unittest.main()