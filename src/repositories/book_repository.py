from config import db
from sqlalchemy import text

from entities.book import Book




def get_book():
    result = db.session.execute(
        text("SELECT * FROM books"))
    
    result = result.fetchall()

    return [Book(book[0],book[1],book[2],book[3],book[4]) for book in result]

def add_book(book):

    author = book[1]
    title = book[2]
    year = book[3]
    publisher = book[4]

    sql = text(f'''INSERT INTO books VALUES (:author), 
               (:title),(:year), (:publisher)''')

    db.session.execute(sql ,{"author":author, "title":title,"year": year, "publisher": publisher})