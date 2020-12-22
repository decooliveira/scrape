class ElementFactory:

    def reviews(self, data):
        return data.find_all("div", {
            "class": "review-entry"})

    def content(self, data):
        return data.find("p", {"class": "font-16 review-content margin-bottom-none line-height-25"})

    def five_stars(self, data):
        return data.find(
            "div", {"class": "rating-static hidden-xs rating-50 margin-center"})

    def date(self, data):
        return data.find("div", {"class": "italic col-xs-6 col-sm-12 pad-none margin-none font-20"})

    def title(self, data):
        return data.find("h3", {"class": "no-format inline italic-bolder font-20 dark-grey"})

    def author(self, data):
        return data.find("span", {"class": "italic font-18 black notranslate"})
