from config import db
from sqlalchemy import text

from entities.book import Book




def get_books():
    result = db.session.execute(
        text("SELECT * FROM books"))
    
    result = result.fetchall()

    return [Book(book[0],book[1],book[2],book[3],book[4]) for book in result]

def add_user_book(book):

    author = book[0]
    title = book[1]
    publisher = book[2]
    year = book[3]
    editor = book[4]
    volume = book[5]
    number = book[6]
    pages = book[7]
    month = book[8]
    note = book[9]


    #db.session.execute("INSERT INTO books (author, title, year, publisher) VALUES ('cha','cha','cha',12)")

    sql = text(f'''INSERT INTO books (author, title, year, publisher, editor, volume, number, pages, month, note) VALUES (:author, 
               :title, :year, :publisher, :editor, :volume, :number, :pages, :month, :note)''')
    

    db.session.execute(sql ,{"author":author, "title":title,"year": year, "publisher": publisher, "editor": editor, "volume": volume, "number": number, "pages": pages, "month": month, "note": note })

    db.session.commit()