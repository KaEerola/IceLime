from entities.book import Book
import unittest


class TestStatisticsService(unittest.TestCase):
    def test_book_values_are_put_correct_way(self):
        id = 2
        name = "Alex"
        tit = "kdjf"
        publis = "otava"
        yer = 1998

        book = Book(id,name,tit,publis, yer)

        self.assertEqual(book.title, tit)

    def test_book_values_are_put_correct_way2(self):
        id = 2
        name = "Alex"
        tit = "kdjf"
        yer = 1998
        publis = "otava"


        book = Book(id,name,tit,yer,publis)

        self.assertEqual(book.publisher, publis)

    def test_book_values_is_not_empty_when_value_put(self):
        id = 2
        name = "Alex"
        tit = "kdjf"
        yer = 1998
        publis = "otava"
        editor = "edit"


        book = Book(id,name,tit,publis, yer, editor)

        self.assertEqual(book.editor, editor)

    def test_book_optional_is_empty_when_no_value(self):
        id = 2
        name = "Alex"
        tit = "kdjf"
        publis = "otava"
        yer = 1998

        book = Book(id,name,tit,publis, yer)

        self.assertEqual(book.volume, "")

        



