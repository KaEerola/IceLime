class Book:
    def __init__(self, id, author, title, year, publisher, editor="", volume="", number="", pages="", month="", note=""): # pylint: disable=redefined-builtin
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
        return f"""Book(id={self.id}, title={self.title}, author={self.author},
                year={self.year}, publisher={self.publisher})"""

