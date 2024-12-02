from sqlalchemy import text
from config import db
from entities.inproceeding import Inproceeding # pylint: disable=unused-import,import-error

def remove_inproceeding(id):

    sql = text("DELETE FROM inproceedings WHERE id = :id")

    db.session.execute(sql, {"id": id})


    db.session.commit()

def get_inproceedings():
    result = db.session.execute(
        text("SELECT * FROM inproceedings")
    )

    result = result.fetchall()

    return [Inproceeding(inproceeding[0], inproceeding[1], inproceeding[2],
                         inproceeding[3], inproceeding[4], inproceeding[5], inproceeding[6], 
                         inproceeding[7], inproceeding[8], inproceeding[9],
                         inproceeding[10], inproceeding[11], inproceeding[12],
                         inproceeding[13]) for inproceeding in result]

def add_user_inproceeding(inproceeding):
    author = f"{inproceeding[0]} {inproceeding[1]}"
    title = inproceeding[2]
    booktitle = inproceeding[3]
    year = inproceeding[4]
    editor = inproceeding[5]
    volume = inproceeding[6]
    number = inproceeding[7]
    series = inproceeding[8]
    pages = inproceeding[9]
    address = inproceeding[10]
    month = inproceeding[11]
    organization = inproceeding[12]
    publisher = inproceeding[13]

    #print(inproceeding)

    sql = text('''INSERT INTO inproceedings (author, title, booktitle, year, editor,
                volume, number, series, pages, address, month, organization, publisher)
               VALUES (:author, :title, :booktitle, :year, :editor,
                :volume, :number, :series, :pages, :address, :month, :organization, :publisher)''')

    db.session.execute(sql, {"author":author, "title":title, "booktitle":booktitle,
                            "year":year, "editor":editor, "volume":volume, "number":number,
                            "series":series, "pages":pages, "address":address,
                            "month":month, "organization":organization,
                            "publisher":publisher})

    db.session.commit()
