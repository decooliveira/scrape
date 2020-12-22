class Review:
    def __init__(self, title, content, rating, date, author):
        self.content = content
        self.length = len(content)
        self.rating = rating
        self.date = date
        self.author = author
        self.title = title

    def print(self):
        print(self.title, '\n', self.content.text,
              '\n', self.date, '\n', self.author, '\n')
