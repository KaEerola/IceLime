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

def update_article(article_id, article_updated):

    id = int(article_id)
    author = article_updated[0]
    title = article_updated[1]
    journal = article_updated[2]
    year = article_updated[3]
    volume = article_updated[4]
    number = article_updated[5]
    pages = article_updated[6]
    month = article_updated[7]
    note = article_updated[8]

    sql = text("""UPDATE articles SET author = :author, title = :title, journal = :journal,
               year = :year, volume = :volume, number = :number, pages = :pages, 
               month = :month, note = :note
                WHERE id = :id""")

    db.session.execute(sql ,{"id" :id, "author":author, "title":title, "journal":journal, 
                             "year": year, "volume": volume, "number": number, 
                             "pages": pages, "month": month, "note": note})
    db.session.commit()

def get_article_by_id(ref_id):
    result = db.session.execute(
        text("""SELECT id, author, title, journal, year, volume, number,
            pages, month, note FROM articles WHERE id = :ref_id"), {"ref_id": ref_id} """))

    article = result.fetchone()

    if article:
        return Article(*article)
