from entities.book import Book
from export import Bibtex
import unittest


class TestStatisticsService(unittest.TestCase):
    def test_exports_bibtex_class1(self):
        bibtex = Bibtex()

        kirja = Book("1","Alex","Chocko","1995","Gateway")

        kirja2 = Book("11","1324","123","123","123","123","123","123","123","123","123")

        bibtex.create_book_bibtex([kirja, kirja2])

        
        self.assertEqual(1,1)
