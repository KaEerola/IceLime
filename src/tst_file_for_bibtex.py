from entities.book import Book

from export import Bibtex


kirja = Book("13","1324","123","123","123","123","123","123","123","123","123")

kirja2 = Book("11","1324","123","123","123","123","123","123","123","123","123")

bibtex = Bibtex()
bibtex.create_book_bibtex([kirja])

bibtex.create_book_bibtex([kirja2])
