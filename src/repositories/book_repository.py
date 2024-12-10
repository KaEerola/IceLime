from sqlalchemy import text
from config import db
from entities.book import Book # pylint: disable=unused-import,import-error



def remove_book(id):

    sql = text("DELETE FROM books WHERE id = :id")

    db.session.execute(sql, {"id": id})

    db.session.commit()


def get_books():
    result = db.session.execute(
        text("SELECT * FROM books")) 
    result = result.fetchall()
    return [Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6],
                book[7], book[8], book[9], book[10], book[11]) for book in result]

def add_user_book(book):

    authors = book[0]
    title = book[1]
    publisher = book[2]
    year = book[3]
    editors = book[4]
    volume = book[5]
    number = book[6]
    pages = book[7]
    month = book[8]
    note = book[9]
    key = book[10]

    sql = text('''INSERT INTO books (author, title, year, publisher,
                editor, volume, number, pages, month, note, key) VALUES (:author,
                :title, :year, :publisher, :editor,
                :volume, :number, :pages, :month, :note, :key)''')

    db.session.execute(sql ,{"author": authors, "title": title,"year": year,
                            "publisher": publisher, "editor": editors, "volume": volume,
                            "number": number, "pages": pages,
                            "month": month, "note": note, "key": key })

    db.session.commit()

def update_book(book_id, book_updated):

    id = int(book_id)
    author = book_updated[0]
    title = book_updated[1]
    publisher = book_updated[2]
    year = book_updated[3]
    editor = book_updated[4]
    volume = book_updated[5]
    number = book_updated[6]
    pages = book_updated[7]
    month = book_updated[8]
    note = book_updated[9]

    sql = text("""UPDATE books SET author = :author, title = :title, year = :year,
                publisher = :publisher, editor = :editor, volume = :volume,
                number = :number, pages = :pages, month = :month, note = :note
                WHERE id = :id""")

    db.session.execute(sql ,{"id" :id, "author":author, "title":title,"year": year,
                            "publisher": publisher, "editor": editor,"volume": volume,
                            "number": number, "pages": pages, "month": month, "note": note})
    db.session.commit()

def get_book_by_id(ref_id):
    result = db.session.execute(
        text('''SELECT id, author, title, year, publisher, editor,
             volume, number, pages, month, note FROM books WHERE id = :ref_id'''),
            {"ref_id": ref_id}
    )
    book = result.fetchone()

    if book:
        return Book(*book)
    return None

def get_book_keys():
    sql = text("""SELECT key FROM books""")

    result = db.session.execute(sql)

    keys = result.fetchall()

    return keys