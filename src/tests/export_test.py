from entities.book import Book
from entities.article import Article
from entities.inproceeding import Inproceeding
from export import Bibtex
import unittest

# Tests check that reference types are printed correctly into files. Ih they are printed like txt variabalse then they pass.

txt = '''@book{book1,
    author = {last, first},
    title = {123},
    year = {123},
    publisher = {123},
    editor = {last3, first3},
    volume = {123},
    number = {123},
    pages = {123},
    month = {123},
    note = {123}
}


@book{book2,
    author = {last2, first2},
    title = {123},
    year = {123},
    publisher = {123},
    editor = {last4, first4},
    volume = {123},
    number = {123},
    pages = {123},
    month = {123},
    note = {123}
}


'''


txt2 = '''@article{article3,
    author = {Back, Jack},
    title = {Chocko Iland},
    year = {2017},
    journal = {New Journal},
    volume = {2},
    number = {23},
    pages = {14}
}


'''

txt3 = '''@inproceedings{inproceedings4,
    author = {Jack Back},
    title = {Chocko Iland},
    year = {2017},
    booktitle = {New Journal},
    editor = {2},
    volume = {23},
    number = {14}
}


'''

class TestStatisticsService(unittest.TestCase):
    def test_exports_bibtex_book(self):

        kirja = Book("1",["first last"],"123","123","123",["first3 last3"],
                     "123","123","123","123","123","book1")

        kirja2 = Book("2",["first2 last2"],"123","123","123",["first4 last4"],
                      "123","123","123","123","123","book2")

        bibtex = Bibtex()
        bibtex.create_book_bibtex([kirja])

        bibtex.create_book_bibtex([kirja2])

        with open("src/bibtex.bib","r",encoding= 'utf-8') as file:

            text = file.read()

        self.assertEqual(txt == text,True)

    def test_exports_bibtex_article(self):

        article = Article("3",["Jack Back"],"Chocko Iland","New Journal",
                          "2017", "2", "23","14","","","article3")

        bibtex = Bibtex()
        bibtex.create_article_bibtex([article])

        with open("src/bibtex.bib","r",encoding= 'utf-8') as file:

            text = file.read()

        self.assertEqual(txt2 == text,True)

    def test_exports_bibtex_inproceedings(self):
        inpro = Inproceeding("4","Jack Back","Chocko Iland","New Journal","2017", "2", "23","14")

        bibtex = Bibtex()
        bibtex.create_inproceedings_bibtex([inpro])

        with open("src/bibtex.bib","r",encoding= 'utf-8') as file:

            text = file.read()

        self.assertEqual(txt3 == text,True)
