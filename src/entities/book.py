class Book:
    def __init__(self, id, author, title, year, publisher, editor="", volume="", number="", pages="", month="", note=""):
        self.id = id
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher
        self.editor = editor
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month
        self.note = note

    def __str__(self):
        return None
