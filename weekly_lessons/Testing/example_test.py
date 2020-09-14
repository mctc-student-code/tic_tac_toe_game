import unittest
from unittest import TestCase
import quote
class QuoteTest(TestCase):

    def test_quote_for_small_lawn_same_day(self):
            actual_quote = quote.lawn_quote('small', True)
            expected = 15
            self.assertEquals(expected,actual_quote)

if __name__ == '__main__':
    unittest.main()