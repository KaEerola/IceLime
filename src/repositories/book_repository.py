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
    year = int(book[3])
    publisher = book[2]

    #db.session.execute("INSERT INTO books (author, title, year, publisher) VALUES ('cha','cha','cha',12)")

    sql = text(f'''INSERT INTO books (author, title, year, publisher) VALUES (:author, 
               :title,:year, :publisher)''')
    

    db.session.execute(sql ,{"author":author, "title":title,"year": year, "publisher": publisher})

    db.session.commit()