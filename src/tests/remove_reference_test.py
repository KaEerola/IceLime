import unittest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import db
from app import remove_book, add_user_book, get_books  

class TestRemoveBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite:///:memory:")
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

        db.session = cls.session

        db.session.execute(text('''
            CREATE TABLE books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT,
                title TEXT,
                year INTEGER,
                publisher TEXT,
                editor TEXT,
                volume TEXT,
                number TEXT,
                pages INTEGER,
                month TEXT,
                note TEXT
            )
        '''))
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.engine.dispose()

    def setUp(self):
        db.session.execute(text("DELETE FROM books"))
        db.session.commit()

    def test_remove_book(self):
        book_data = [
            "John", "Doe", "Test Book", "Test Publisher", 2024, "Test Editor",
            "1st", "1", 100, "January", "Test Note"
        ]
        add_user_book(book_data)

        books = get_books()
        self.assertEqual(len(books), 1)
        book_id = books[0].id

        remove_book(book_id)

        books_after_removal = get_books()
        self.assertEqual(len(books_after_removal), 0)

if __name__ == "__main__":
    unittest.main()