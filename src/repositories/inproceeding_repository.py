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
                         inproceeding[13], inproceeding[14], inproceeding[15]) for inproceeding in result]

def add_user_inproceeding(inproceeding):

    author = inproceeding[0]
    title = inproceeding[1]
    booktitle = inproceeding[2]
    year = inproceeding[3]
    editor = inproceeding[4]
    volume = inproceeding[5]
    number = inproceeding[6]
    series = inproceeding[7]
    pages = inproceeding[8]
    address = inproceeding[9]
    month = inproceeding[10]
    organization = inproceeding[11]
    note = inproceeding[12]
    publisher = inproceeding[13]
    key = inproceeding[14]
    print(inproceeding)
    sql = text('''INSERT INTO inproceedings (author, title, booktitle, year, editor,
                volume, number, series, pages, address, month, organization, note, publisher, key)
                VALUES (:author, :title, :booktitle, :year, :editor,
                :volume, :number, :series, :pages, :address, :month, :organization, :note,
                :publisher, :key)''')

    db.session.execute(sql, {"author":author, "title":title, "booktitle":booktitle,
                            "year":year, "editor":editor, "volume":volume, "number":number,
                            "series":series, "pages":pages, "address":address,
                            "month":month, "organization":organization, "note":note,
                            "publisher":publisher, "key":key})

    db.session.commit()

def update_inproceeding(inproceeding_id, inproceeding_updated):

    id = int(inproceeding_id)
    author = inproceeding_updated[0]
    title = inproceeding_updated[1]
    booktitle = inproceeding_updated[2]
    year = inproceeding_updated[3]
    editor = inproceeding_updated[4]
    volume = inproceeding_updated[5]
    number = inproceeding_updated[6]
    series = inproceeding_updated[7]
    pages = inproceeding_updated[8]
    address = inproceeding_updated[9]
    month = inproceeding_updated[10]
    organization = inproceeding_updated[11]
    note = inproceeding_updated[12]
    publisher = inproceeding_updated[13]
    key = inproceeding_updated[14]

    sql = text("""UPDATE inproceedings SET author = :author, title = :title, booktitle = :booktitle,
                year = :year, editor = :editor, volume = :volume, number = :number, series = :series,
                pages = :pages, address = :address, month = :month, organization = :organization, note = :note, publisher = :publisher, key = :key
                WHERE id = :id""")

    db.session.execute(sql ,{"id" :id, "author":author, "title": title, "booktitle": booktitle,
                             "year": year, "editor": editor, "volume": volume,  
                             "number": number, "series": series, "pages": pages, "address": address,
                             "month": month, "organization": organization, "note": note, "publisher": publisher,
                             "key": key})

    db.session.commit()

def get_inproceeding_by_id(ref_id):
    result = db.session.execute(
        text('''SELECT id, author, title, booktitle, year, editor, volume, number, series,
            pages, address, month, organization, note, publisher, key FROM inproceedings WHERE id = :ref_id
             '''),
            {"ref_id": ref_id}
    )
    inproceeding = result.fetchone()

    if inproceeding:
        return Inproceeding(*inproceeding)
    return None

def get_inproceeding_keys():
    sql = text("""SELECT key FROM inproceedings""")

    result = db.session.execute(sql)

    keys = result.fetchall()

    return keys
