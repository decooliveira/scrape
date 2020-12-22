import unittest
from Reader import Reader


class TestReader(unittest.TestCase):

    def test_read(self):

        url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page1"
        reader = Reader()
        response = reader.read(url)
        self.assertIsNotNone(response)
