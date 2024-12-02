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

def update_book(book_id, book_updated):

    sql = text("""UPDATE books SET author = :author, title = :title, year = :year, publisher = :publisher, editor = :editor, 
                volume = :volume, number = :number, pages = :pages, month = :month, note = :note
                WHERE id = :id""")
    
    db.session.execute(sql, {
        "id": book_id,
        "author": book_updated["author"],
        "title": book_updated["title"],
        "year": book_updated["year"],
        "publisher": book_updated["publisher"],
        "editor": book_updated.get("editor"),
        "volume": book_updated.get("volume"),
        "number": book_updated.get("number"),
        "pages": book_updated.get("pages"),
        "month": book_updated.get("month"),
        "note": book_updated.get("note")
        })
    db.session.commit()

def get_book_by_id(ref_id):
    result = db.session.execute(
        text("SELECT * FROM books WHERE id = :ref_id"), {"ref_id": ref_id}
    )
    book = result.fetchone()  # Fetch a single result (the specific book)
    
    if book:
        # Assuming the Book class takes parameters in the same order as the DB columns
        return Book(*book)
    return None

