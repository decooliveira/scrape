from bs4 import BeautifulSoup


class Parser:

    def parse(self, data):
        return BeautifulSoup(data.text, 'html.parser')
