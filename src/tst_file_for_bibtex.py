from entities.book import Book

from export import Bibtex


kirja = Book("13","1324","123","123","123","123","123","123","123","123","123")


bibtex = Bibtex([kirja])

bibtex.create_book_bibtex()