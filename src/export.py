class Bibtex():
    def __init__(self):

        with open("src/bibtex.bib", "w") as file:
            pass

    def create_book_bibtex(self, books_list):

        with open("src/bibtex.bib", "a") as file:

            for book in books_list:

                file.write(f'''@book{{book{book.id}''')
                file.write(f''',\n    author = {{{book.author}}}''')
                file.write(f''',\n    title = {{{book.title}}}''')
                file.write(f''',\n    year = {{{book.year}}}''')
                file.write(f''',\n    publisher = {{{book.publisher}}}''')

                if book.editor:
                    file.write(f''',\n    editor = {{{book.editor}}}''')

                if book.volume:
                    file.write(f''',\n    volume = {{{book.volume}}}''')

                if book.number:
                    file.write(f''',\n    number = {{{book.number}}}''')

                if book.pages:
                    file.write(f''',\n    pages = {{{book.pages}}}''')

                if book.month:
                    file.write(f''',\n    month = {{{book.month}}}''')

                if book.note:
                    file.write(f''',\n    note = {{{book.note}}}''')

                file.write('''\n}\n\n\n''')

            file.close()

    def create_article_bibtex(self, article_list):

        with open("src/bibtex.bib", "a") as file:

            for article in article_list:

                file.write(f'''@article{{article{article.id}''')
                file.write(f''',\n    author = {{{article.author}}}''')
                file.write(f''',\n    title = {{{article.title}}}''')
                file.write(f''',\n    year = {{{article.year}}}''')
                file.write(f''',\n    journal = {{{article.journal}}}''')

                if article.volume:
                    file.write(f''',\n    volume = {{{article.volume}}}''')

                if article.number:
                    file.write(f''',\n    number = {{{article.number}}}''')

                if article.pages:
                    file.write(f''',\n    pages = {{{article.pages}}}''')

                if article.month:
                    file.write(f''',\n    month = {{{article.month}}}''')

                if article.note:
                    file.write(f''',\n    note = {{{article.note}}}''')

                file.write('''\n}\n\n\n''')

            file.close()

    def create_inproceedings_bibtex(self, inproceeding_list):

        with open("src/bibtex.bib", "a") as file:

            for inpro in inproceeding_list:

                file.write(f'''@inproceedings{{inproceedings{inpro.id}''')
                file.write(f''',\n    author = {{{inpro.author}}}''')
                file.write(f''',\n    title = {{{inpro.title}}}''')
                file.write(f''',\n    year = {{{inpro.year}}}''')
                file.write(f''',\n    booktitle = {{{inpro.booktitle}}}''')

                if inpro.editor:
                    file.write(f''',\n    editor = {{{inpro.editor}}}''')
                
                if inpro.volume:
                    file.write(f''',\n    volume = {{{inpro.volume}}}''')

                if inpro.number:
                    file.write(f''',\n    number = {{{inpro.number}}}''')

                if inpro.series:
                    file.write(f''',\n    series = {{{inpro.series}}}''')

                if inpro.pages:
                    file.write(f''',\n    pages = {{{inpro.pages}}}''')

                if inpro.address:
                    file.write(f''',\n    address = {{{inpro.address}}}''')
                
                if inpro.month:
                    file.write(f''',\n    month = {{{inpro.month}}}''')

                if inpro.organization:
                    file.write(f''',\n    organization = {{{inpro.organization}}}''')

                if inpro.publisher:
                    file.write(f''',\n    publisher = {{{inpro.publisher}}}''')

                file.write('''\n}\n\n\n''')

            file.close()

