class Bibtex():
    def __init__(self):
        pass

    def create_book_bibtex(self, books_list):


        with open("bibtex.bib", "w") as file:

            for book in books_list:
            
                file.write(f'''@book{{book{book.id}''')
                file.write(f''',\n    author = "{book.author}"''')
                file.write(f''',\n    title = "{book.title}"''')
                file.write(f''',\n    year = "{book.year}"''')
                file.write(f''',\n    publisher = "{book.publisher}"''')

                if book.editor != "":
                    file.write(f''',\n    editor = "{book.editor}"''')

                if book.volume != "":
                    file.write(f''',\n    volume = "{book.volume}"''')

                if book.number != "":
                    file.write(f''',\n    number = "{book.number}"''')

                if book.pages != "":
                    file.write(f''',\n    pages = "{book.pages}"''')

                if book.month != "":
                    file.write(f''',\n    month = "{book.month}"''')

                if book.note != "":
                    file.write(f''',\n    note = "{book.note}"''')

                file.write('''\n}\n\n\n''')