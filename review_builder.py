from Review import Review
from element_factory import ElementFactory


class ReviewBuilder:

    def collection(self, reviews):
        all_reviews = []
        factory = ElementFactory()

        for r in reviews:

            content = factory.content(r)
            five_stars = factory.five_stars(r)
            date = factory.date(r).text
            author = factory.author(r).text
            title = factory.title(r).text
            rating = 5 if five_stars != None else 0

            if(rating == 5):
                review = Review(title, content, rating, date, author)
                all_reviews.append(review)
        return all_reviews
