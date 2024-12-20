import unittest
from unittest.mock import Mock, patch
from repositories.book_repository import get_books
from config import db

class TestAddingBook(unittest.TestCase):
    @patch("config.db.session.execute")
    def test_get_books(self, mock_execute):
        mock_result = [(1, "Author 1", "Title 1", 2023, "Publisher 1", "Editor 1", "Volume 1", "Number 1", "Pages 1", "January", "Note 1", "book1" ),
            (2, "Author 2", "Title 2", 2022, "Publisher 2", "", "", "", "", "", "", "book2"),
        ]

        mock_execute.return_value.fetchall.return_value = mock_result

        books = get_books()

        self.assertEqual(len(books),2)
        self.assertEqual(books[1].title, "Title 2")

        mock_execute.assert_called_once()
        actual_query = mock_execute.call_args[0][0]
        self.assertEqual(str(actual_query), "SELECT * FROM books")

if __name__ == "__main__":
    unittest.main()
