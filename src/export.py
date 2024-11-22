

class Bibtex():
    def __init__(self, books_list):
        self.books = books_list

    def create_book_bibtex(self):


        with open("bibtex.bib", "w") as file:

            for book in self.books:
            
                file.write(f'''@book{{book{book.id}''')
                file.write(f''',\n    author = "{book.author}"''')
                file.write(f''',\n    title = "{book.title}"''')
                file.write(f''',\n    year = "{book.year}"''')
                file.write(f''',\n    publisher = "{book.publisher}"''')

                if book.editor != None:
                    file.write(f''',\n    editor = "{book.editor}"''')

                if book.volume != None:
                    file.write(f''',\n    volume = "{book.volume}"''')

                if book.number != None:
                    file.write(f''',\n    number = "{book.number}"''')

                if book.pages != None:
                    file.write(f''',\n    pages = "{book.pages}"''')

                if book.month != None:
                    file.write(f''',\n    month = "{book.month}"''')

                if book.note != None:
                    file.write(f''',\n    note = "{book.note}"''')

                file.write('''\n}\n\n\n''')