class Article:
    def __init__(self, id, author, title, journal, year, volume="", number="", pages="", month="", note=""):
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month 
        self.note = note

    def __str__(self):
        return None