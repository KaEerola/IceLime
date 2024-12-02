from sqlalchemy import text
from config import db
from entities.article import Article # pylint: disable=unused-import,import-error

def remove_article(id):

    sql = text("DELETE FROM articles WHERE id = :id")

    db.session.execute(sql, {"id": id})

    db.session.commit()


def get_articles():
    result = db.session.execute(
        text("SELECT * FROM articles")
    )

    result = result.fetchall()

    return [Article(article[0], article[1], article[2], article[3],
    article[4], article[5], article[6], article[7],
    article[8]) for article in result]

def add_user_article(article):
    author = f"{article[0]} {article[1]}"
    title = article[2]
    journal = article[3]
    year = article[4]
    volume = article[5]
    number = article[6]
    pages = article[7]
    month = article[8]
    note = article[9]


    sql = text('''INSERT INTO articles (author, title, journal, year,
               volume, number, pages, month, note)
               VALUES (:author, :title, :journal, :year, :volume,
               :number, :pages, :month, :note)''')

    db.session.execute(sql, {"author":author, "title":title, "journal":journal,
                              "year":year, "volume":volume, "number":number,
                              "pages":pages, "month":month, "note":note})


    db.session.commit()
