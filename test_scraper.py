import unittest
from scraper import Scraper


class TestScraper(unittest.TestCase):

    def test_run_pages_should_be_higher_than_zero(self):
        scraper = Scraper()
        self.assertRaises(ValueError, scraper.run, 0)
