from sqlalchemy import text
from config import db, app


table_name = "todos" # pylint: disable=invalid-name

def table_exists(name):
    sql_table_existence = text(
      "SELECT EXISTS ("
      "  SELECT 1"
      "  FROM information_schema.tables"
      f" WHERE table_name = '{name}'"
      ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()

def setup_db():
    if table_exists(table_name):
        print(f"Table {table_name} exists, dropping")
        sql = text(f"DROP TABLE {table_name}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name}")
    sql = text(
      f"CREATE TABLE {table_name} ("
      "  id SERIAL PRIMARY KEY, "
      "  content TEXT NOT NULL,"
      "  done BOOLEAN DEFAULT FALSE"
      ")"
    )

    db.session.execute(sql)
    db.session.commit()

  #inproceedings

    if table_exists("inproceedings"):
        print("Table inproceedings exists, dropping")
        sql = text("DROP TABLE inproceedings")
        db.session.execute(sql)
        db.session.commit()


    sql2 = text(
      """
      CREATE TABLE inproceedings (
          id SERIAL PRIMARY KEY,
          "author" TEXT,
          "title" TEXT,
          "booktitle" TEXT,
          "year" integer,
          "editor" TEXT,
          "volume" integer,
          "number" integer,
          "series" TEXT,
          "pages" TEXT,
          "address" TEXT,
          "month" TEXT,
          "organization" TEXT,
          "publisher" TEXT
      )
      """
    )

    db.session.execute(sql2)
    db.session.commit()

  #books

    if table_exists("books"):
        print("Table books exists, dropping")
        sql = text("DROP TABLE books")
        db.session.execute(sql)
        db.session.commit()

    sql3 = text(
    """
    CREATE TABLE "books" (
    "id" SERIAL PRIMARY KEY,
    "author" TEXT[],
    "title" TEXT,
    "year" integer,
    "publisher" TEXT,
    "editor" TEXT[] DEFAULT NULL,
    "volume" integer DEFAULT NULL,
    "number" integer DEFAULT NULL,
    "pages" TEXT DEFAULT NULL,
    "month" TEXT DEFAULT NULL,
    "note" TEXT DEFAULT NULL,
    "key" TEXT
      )
    """
  )

    db.session.execute(sql3)
    db.session.commit()

  #articles

    if table_exists("articles"):
        print("Table articles exists, dropping")
        sql = text("DROP TABLE articles")
        db.session.execute(sql)
        db.session.commit()


    sql4 = text(
      """
      CREATE TABLE "articles" (
      "id" SERIAL PRIMARY KEY,
      "author" TEXT[],
      "title" TEXT,
      "journal" TEXT,
      "year" integer,
      "volume" integer,
      "number" integer,
      "pages" TEXT,
      "month" TEXT,
      "note" TEXT,
      "key" TEXT
      )
      """
    )


    db.session.execute(sql4)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
