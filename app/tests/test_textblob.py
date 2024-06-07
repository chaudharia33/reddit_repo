import unittest
from ..utils.sentiment import analyze_sentiment_textblob

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment_textblob_positive(self):
        self.assertEqual(analyze_sentiment_textblob("I love this product!"), "positive")

    def test_analyze_sentiment_textblob_negative(self):
        self.assertEqual(analyze_sentiment_textblob("I hate this product!"), "negative")

    def test_analyze_sentiment_textblob_neutral(self):
        self.assertEqual(analyze_sentiment_textblob("This product is okay."), "neutral")

if __name__ == "__main__":
    unittest.main()