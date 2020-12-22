import unittest
from Loader import Loader

class TestLoader(unittest.TestCase):
    
    

    def test_load_reviews(self):
        loader = Loader()
        reviews = loader.load(5)
        self.assertGreater(len(reviews),0)