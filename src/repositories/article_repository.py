from config import db
from sqlalchemy import text

from entities.article import Article


def get_articles():
    result = db.session.execute(
        text("SELECT * FROM articles")
    )

    result = result.fetchall()

    return [Article(article[0], article[1], article[2], article[3], article[4]) for article in result]

def add_user_article(article):
    author = article[0]
    title = article[1]
    journal = article[2]
    year = article[3]
    volume = article[4]
    number = article[5]
    pages = article[6]
    month = article[7]
    note = article[8]


    sql = text('''INSERT INTO articles (author, title, journal, year, volume, number, pages, month, note)
               VALUES (:author, :title, :journal, :year, :volume, :number, :pages, :month, :note)''')
    
    db.session.execute(sql, {"author":author, "title":title, "journal":journal, "year":year, "volume":volume, "number":number, "pages":pages, "month":month, "note":note})


    db.session.commit()