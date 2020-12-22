from Review import Review
from Reader import Reader
from Parser import Parser
from element_factory import ElementFactory
from review_builder import ReviewBuilder


class Loader:

    def load(self, pages):
    
        reviews = []
        step = 1

        for page in range(1, pages+step):

            url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page" + \
                str(page)

            reader = Reader()
            response = reader.read(url)

            parser = Parser()
            data = parser.parse(response)

            factory = ElementFactory()
            reviewElements = factory.reviews(data)

            review_builder = ReviewBuilder()
            reviews.extend(review_builder.collection(reviewElements))

        return reviews
