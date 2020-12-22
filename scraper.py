from Loader import Loader
from Review import Review
from Logger import Logger

class Scraper:

    def __init__(self):
        self.logger = Logger()

    def run(self, pages):
        if(pages < 1):
            raise ValueError("The number of pages cannot be zero or negative")

        self.logger.log("Start running Scraper")
        try:
            loader = Loader()
            reviews = loader.load(pages)
            reviews.sort(key=lambda x: x.length, reverse=True)

            for i in range(0, 3):
                review = reviews[i]
                review.print()
                self.logger.log(str(i+1)+100*"-")
                self.logger.log(review.title+" - "+review.date+" "+review.author)
                self.logger.log(100*"-"+"\n")
        
        except:
            print("Unable to fetch review at this moment. Please try again later")
scraper = Scraper()
scraper.run(5)
