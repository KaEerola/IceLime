class Inproceeding:
    def __init__(self, id, author, title, booktitle, year, 
                editor="", volume="", number="", # pylint: disable=redefined-builtin
                series="", pages="", address="", 
                month="", organization="", publisher=""):
        self.id = id
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.pages = pages
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher

    def __str__(self): # pylint: disable=invalid-str-returned
        return None
