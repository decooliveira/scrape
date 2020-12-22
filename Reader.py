import requests


class Reader:

    def read(self, url):
        return requests.get(url)
