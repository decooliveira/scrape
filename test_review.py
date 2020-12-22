import unittest
from Review import Review

class TestReview(unittest.TestCase):

    def test_review(self):
        review = Review("Review title","This is the review content","5","December 20, 2020","Deco Oliveira")
        self.assertEquals(review.title,"Review title")
        self.assertEquals(review.content,"This is the review content")
        self.assertEquals(review.rating,"5")
        self.assertEquals(review.date,"December 20, 2020")
        self.assertEquals(review.author,"Deco Oliveira")