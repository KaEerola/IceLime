from sqlalchemy import text
from config import db
from entities.book import Book # pylint: disable=unused-import,import-error




def get_books():
    result = db.session.execute(
        text("SELECT * FROM books"))

    result = result.fetchall()

    return [Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8], book[9], book[10]) for book in result]

def add_user_book(book):

    author = f"{book[0]} {book[1]}"
    title = book[2]
    publisher = book[3]
    year = book[4]
    editor = book[5]
    volume = book[6]
    number = book[7]
    pages = book[8]
    month = book[9]
    note = book[10]


    #db.session.execute("INSERT INTO books (author, title, year, publisher) VALUES ('cha','cha','cha',12)")

    sql = text('''INSERT INTO books (author, title, year, publisher, editor, volume, number, pages, month, note) VALUES (:author,
               :title, :year, :publisher, :editor, :volume, :number, :pages, :month, :note)''')

    db.session.execute(sql ,{"author":author, "title":title,"year": year, "publisher": publisher, "editor": editor, "volume": volume,
                              "number": number, "pages": pages, "month": month, "note": note })

    db.session.commit()
