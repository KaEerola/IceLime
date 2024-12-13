from flask import redirect, render_template, request, jsonify, flash, send_file
from db_helper import reset_db
from repositories.book_repository import add_user_book, get_books, get_book_by_id
from repositories.book_repository import update_book, remove_book
from repositories.article_repository import add_user_article, get_articles
from repositories.article_repository import remove_article, update_article, get_article_by_id
from repositories.inproceeding_repository import add_user_inproceeding, get_inproceedings
from repositories.inproceeding_repository import remove_inproceeding, update_inproceeding
from repositories.inproceeding_repository import  get_inproceeding_by_id
from config import app, test_env
from util import validate_book, validate_article, validate_inproceeding, validate_update
from util import validate_key, validate_update_key
from scraper import get_book_data_by_doi, get_article_data_by_doi, get_inproceeding_data_by_doi
from export import Bibtex


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/add_reference", methods=["GET"])
def add_reference():

    return render_template("add_reference.html")

@app.route("/add_book", methods=["GET"])
def add_book():
    authors = []
    author_count = 1
    editors = []
    editor_count = 1

    months = ["", "January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    return render_template("add_book.html", authors=authors, author_count=author_count, editors=editors, editor_count=editor_count, months=months)

@app.route("/add_book", methods=["POST"])
def add_post_book():
    months = ["", "January", "February", "March", "April",
                  "May", "June", "July", "August", "September",
                  "October", "November", "December"]
    authors = []
    author_count = int(request.form.get("author_count", 1))
    editors = []
    editor_count = int(request.form.get("editor_count", 1))

    if request.form["action"] == "reset":
        return render_template("add_book.html",
                               months=months,
                               author_count=1,
                               editor_count=1)

    elif request.form["action"] in ["add_author", "add_editor", "remove_author", "remove_editor"]:

        if request.form["action"] == "add_author":
            author_count += 1

        elif request.form["action"] == "add_editor":
            editor_count += 1

        elif request.form["action"] == "remove_author":
            author_count -= 1

        elif request.form["action"] == "remove_editor":
            editor_count -= 1

        idx = 0
        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1

        idx = 0
        while idx < editor_count:
            firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
            lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
            if firstname or lastname:
                editors.append(f"{firstname} {lastname}")
            idx += 1

        return render_template("add_book.html",
                               authors=authors,
                               title=request.form["title"],
                               publisher=request.form["publisher"],
                               year=request.form["year"],
                               editors=editors,
                               volume=request.form.get("volume", ""),
                               number=request.form.get("number", ""),
                               pages=request.form.get("pages", ""),
                               imported_month=request.form.get("month", ""),
                               note=request.form.get("note", ""),
                               key=request.form["key"],
                               months=months,
                               author_count=author_count,
                               editor_count=editor_count)

    idx = 0
    while f"author_firstname_{idx}" in request.form:
        firstname = request.form.get(f"author_firstname_{idx}").strip()
        lastname = request.form.get(f"author_lastname_{idx}").strip()
        if firstname and lastname:
            authors.append(f"{firstname} {lastname}")
        idx += 1
    idx = 0
    while f"editor_firstname_{idx}" in request.form:
        firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
        lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
        if firstname and lastname:
            editors.append(f"{firstname} {lastname}")
        idx += 1

    tit = request.form["title"]
    pub = request.form["publisher"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None
    key = request.form["key"]

    reference = [authors, tit, pub, year, editors, vol, num, pages, month, note, key]

    try:
        validate_book(reference)
        validate_key(key)
        add_user_book(reference)
        flash('Reference added succesfully', "")
        return redirect("/add_book")
    except:
        flash('You must put valid Author, Title, Publisher And Year',"")
        return redirect("/add_book")

@app.route("/view_references")
def view_references():

    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    return render_template("view_references.html",
                           books=books,
                           articles=articles,
                           inproceedings=inproceedings)

@app.route("/add_article", methods = ["GET"])
def add_article():
    authors = []
    author_count = 1
    months = ["", "January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    return render_template("add_article.html", authors=authors, author_count=author_count, months=months)

@app.route("/add_article", methods = ["POST"])
def add_post_article():

    months = ["", "January", "February", "March", "April",
                  "May", "June", "July", "August", "September",
                  "October", "November", "December"]
        
    authors = []
    author_count = int(request.form.get("author_count", 1))

    if request.form["action"] == "reset":
        return render_template("add_article.html",
                               months=months,
                               author_count=1)

    elif request.form["action"] == "add_author":
        author_count += 1
        authors = []

        idx = 0

        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1

        return render_template("add_article.html",
                               authors=authors,
                               title=request.form["title"],
                               journal=request.form["journal"],
                               year=request.form["year"],
                               volume=request.form.get("volume", ""),
                               number=request.form.get("number", ""),
                               pages=request.form.get("pages", ""),
                               imported_month=request.form.get("month", ""),
                               note=request.form.get("note", ""),
                               key=request.form["key"],
                               months=months,
                               author_count=author_count)

    elif request.form["action"] == "remove_author":
        author_count -= 1
        authors = []

        idx = 0

        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1
        
        return render_template("add_article.html",
                               authors=authors,
                               title=request.form["title"],
                               journal=request.form["journal"],
                               year=request.form["year"],
                               volume=request.form.get("volume", ""),
                               number=request.form.get("number", ""),
                               pages=request.form.get("pages", ""),
                               imported_month=request.form.get("month", ""),
                               note=request.form.get("note", ""),
                               key=request.form["key"],
                               months=months,
                               author_count=author_count)

    idx = 0
    while f"author_firstname_{idx}" in request.form:
        firstname = request.form.get(f"author_firstname_{idx}").strip()
        lastname = request.form.get(f"author_lastname_{idx}").strip()
        if firstname and lastname:
            authors.append(f"{firstname} {lastname}")
        idx += 1


    tit = request.form["title"]
    jou = request.form["journal"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None
    key = request.form["key"]

    reference = [authors, tit, jou, year, vol,
                 num, pages, month, note, key]
    print(reference)

    try:
        validate_article(reference)
        validate_key(key)
        add_user_article(reference)
        flash('Reference added succesfully', "")
        return redirect("/add_article")
    except:
        flash('You must put valid Author, Title, Journal And Year',"")
        return redirect("/add_article")


@app.route("/add_inproceeding", methods = ["GET"])
def add_inproceeding():
    authors = []
    author_count = 1
    editors = []
    editor_count = 1

    months = ["", "January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    return render_template("add_inproceeding.html", authors=authors, author_count=author_count, editors=editors, editor_count=editor_count, months=months)

@app.route("/add_inproceeding", methods=["POST"])
def add_post_inproceeding():
    months = ["", "January", "February", "March", "April",
                  "May", "June", "July", "August", "September",
                  "October", "November", "December"]
    authors = []
    author_count = int(request.form.get("author_count", 1))
    editors = []
    editor_count = int(request.form.get("editor_count", 1))

    if request.form["action"] == "reset":
        return render_template("add_inproceeding.html",
                               months=months,
                               author_count=1,
                               editor_count=1)

    elif request.form["action"] in ["add_author", "add_editor", "remove_author", "remove_editor"]:

        if request.form["action"] == "add_author":
            author_count += 1

        elif request.form["action"] == "add_editor":
            editor_count += 1

        elif request.form["action"] == "remove_author":
            author_count -= 1

        elif request.form["action"] == "remove_editor":
            editor_count -= 1

        idx = 0
        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1

        idx = 0
        while idx < editor_count:
            firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
            lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
            if firstname or lastname:
                editors.append(f"{firstname} {lastname}")
            idx += 1

        return render_template("add_inproceeding.html",
                               authors=authors,
                               title=request.form["title"],
                               booktitle=request.form["booktitle"],
                               year=request.form["year"],
                               editors=editors,
                               volume=request.form.get("volume", ""),
                               number=request.form.get("number", ""),
                               series=request.form.get("series", ""),
                               pages=request.form.get("pages", ""),
                               address=request.form.get("address", ""),
                               imported_month=request.form.get("month", ""),
                               organization=request.form.get("organization", ""),
                               publisher=request.form.get("publisher", ""),
                               note=request.form.get("note", ""),
                               key=request.form["key"],
                               months=months,
                               author_count=author_count,
                               editor_count=editor_count)

    idx = 0
    while f"author_firstname_{idx}" in request.form:
        firstname = request.form.get(f"author_firstname_{idx}").strip()
        lastname = request.form.get(f"author_lastname_{idx}").strip()
        if firstname and lastname:
            authors.append(f"{firstname} {lastname}")
        idx += 1
    idx = 0
    while f"editor_firstname_{idx}" in request.form:
        firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
        lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
        if firstname and lastname:
            editors.append(f"{firstname} {lastname}")
        idx += 1

    tit = request.form["title"]
    btit = request.form["booktitle"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    ser = request.form.get("series") or None
    pages = request.form.get("pages") or None
    addr = request.form.get("address") or None
    month = request.form.get("month") or None
    org = request.form.get("organization") or None
    note = request.form.get("note") or None
    pub = request.form.get("publisher") or None
    key = request.form["key"]

    reference = [authors, tit, btit, year, editors, vol, num, ser, pages, addr, month, org, note, pub, key]

    try:
        validate_inproceeding(reference)
        validate_key(key)
        add_user_inproceeding(reference)
        flash('Reference added succesfully', "")
        return redirect("/add_inproceeding")
    except:
        flash('You must put valid Author, Title, Booktitle And Year',"")
        return redirect("/add_inproceeding")

@app.route("/fetch_book_doi", methods=["POST"])
def fetch_book_doi():
    doi = request.form.get("doi")

    if not doi:
        flash("You must put in a valid DOI", "")
        return redirect("/add_book")

    months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    try:
        data = get_book_data_by_doi(doi)

        authors = data[0]
        author_count = len(authors) if authors else 1
        editors = data[5]
        editor_count = len(editors) if editors else 1
        return render_template("add_book.html",
                               authors = authors,
                               title = data[1],
                               publisher = data[2],
                               year = data[3],
                               months = months,
                               imported_month = data[4],
                               editors = editors,
                               author_count = author_count,
                               editor_count = editor_count)

    except:
        flash("Failed to fetch the data, please check the DOI.", "")
        return redirect("/add_book")

@app.route("/fetch_article_doi", methods=["POST"])
def fetch_article_doi():
    doi = request.form.get("doi")

    if not doi:
        flash("You must put in a valid DOI", "")
        return redirect("/add_article")

    months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    try:
        data = get_article_data_by_doi(doi)

        authors = data[0]
        author_count = len(authors) if authors else 1

        return render_template("add_article.html",
                               authors = authors,
                               title = data[1],
                               publisher = data[2],
                               year = data[3],
                               months = months,
                               imported_month = data[4],
                               journal = data[5],
                               volume = data[6], 
                               author_count = author_count)

    except:
        flash("Failed to fetch the data, please check the DOI.", "")
        return redirect("/add_article")

@app.route("/fetch_inproceeding_doi", methods=["POST"])
def fetch_inproceeding_doi():
    doi = request.form.get("doi")

    if not doi:
        flash("You must put in a valid DOI", "")
        return redirect("/add_inproceeding")

    months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    try:
        print("test")
        data = get_inproceeding_data_by_doi(doi)
        print(data)
        authors = data[0]
        author_count = len(authors) if authors else 1
        editors = data[5]
        editor_count = len(editors) if editors else 1

        return render_template("add_inproceeding.html",
                               authors = authors,
                               title = data[1],
                               publisher = data[2],
                               year = data[3],
                               months = months,
                               imported_month = data[4],
                               editors = editors,
                               booktitle = data[6],
                               volume = data[7],
                               author_count = author_count,
                               editor_count = editor_count)

    except:
        flash("Failed to fetch the data, please check the DOI.", "")
        return redirect("/add_inproceeding")

@app.route("/export", methods=["GET"])
def export():

    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()


    bibtex = Bibtex()
    bibtex.create_book_bibtex(books)
    bibtex.create_article_bibtex(articles)
    bibtex.create_inproceedings_bibtex(inproceedings)

    return send_file(
        "bibtex.bib",
        as_attachment = True,
        download_name = "references.bib",
        mimetype = "text/plain")

@app.route("/remove_reference", methods=["GET"])
def remove_reference():
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()

    return render_template("remove_reference.html",
                           books=books,
                           articles=articles,
                           inproceedings=inproceedings)

@app.route("/remove_reference", methods=["POST"])
def remove_reference2():
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()

    book_id = request.form.get('book_id')
    article_id = request.form.get("article_id")
    inproceedings_id = request.form.get("inproceeding_id")

    if book_id:
        try:
            remove_book(book_id)
            flash('Reference removed succesfully', "")
            return redirect("/view_references")
        except Exception as e:
            return f"An error occurred: {e}", 500

    if article_id:
        try:
            remove_article(article_id)
            flash('Reference removed succesfully', "")
            return redirect("/view_references")
        except Exception as e:
            return f"An error occurred: {e}", 500

    if inproceedings_id:
        try:
            remove_inproceeding(inproceedings_id)
            flash('Reference removed succesfully', "")
            return redirect("/view_references")
        except Exception as e:
            return f"An error occurred: {e}", 500
    return render_template("remove_reference.html",
                           books=books,
                           articles=articles,
                           inproceedings=inproceedings)

@app.route("/edit_reference", methods=["GET"])
def edit_reference():
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()

    return render_template("edit_reference.html",
                           books=books,
                           articles=articles,
                           inproceedings=inproceedings)

@app.route("/edit_reference", methods=["POST"])
def edit_post_reference():

    book_id = request.form.get("book_id")
    article_id = request.form.get("article_id")
    inproceeding_id = request.form.get("inproceeding_id")

    if book_id:
        return redirect("/update_book/"+str(book_id))

    if article_id:
        return redirect("/update_article/"+str(article_id))

    if inproceeding_id:
        return redirect("/update_inproceeding/"+str(inproceeding_id))

    flash("No reference selected", "")

@app.route("/update_book/<int:book_id>", methods=["GET"])
def update_book_reference(book_id):

    reference = get_book_by_id(book_id)
    authors = reference.author
    author_count = len(authors) if authors else 1
    editors = reference.editor
    editor_count = len(editors) if editors else 1

    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return render_template("update_book.html",
                           book_id=reference.id,
                           authors=authors,
                           title=reference.title,
                           publisher=reference.publisher,
                           year=reference.year,
                           editors=editors if editors else "",
                           volume=reference.volume if reference.volume else "",
                           number=reference.number,
                           pages=reference.pages if reference.pages else "",
                           imported_month=reference.month,
                           note=reference.note if reference.note else "",
                           months=months,
                           key=reference.key,
                           author_count=author_count,
                           editor_count=editor_count,
                           reference=reference)

@app.route("/update_book/<int:book_id>", methods=["POST"])
def update_post_book_reference(book_id):
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    authors = []
    author_count = int(request.form.get("author_count", 1))
    editors = []
    editor_count = int(request.form.get("editor_count", 1))

    tit = request.form["title"]
    pub = request.form["publisher"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None
    key = request.form["key"]


    if request.form["action"] in ["add_author", "add_editor", "remove_author", "remove_editor"]:


        if request.form["action"] == "add_author":
            author_count += 1

        elif request.form["action"] == "add_editor":
            editor_count += 1

        elif request.form["action"] == "remove_author":
            author_count -= 1

        elif request.form["action"] == "remove_editor":
            editor_count -= 1

        idx = 0
        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1

        idx = 0
        while idx < editor_count:
            firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
            lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
            if firstname or lastname:
                editors.append(f"{firstname} {lastname}")
            idx += 1

        reference = [authors, tit, pub, year, editors, vol, num, pages, month, note, key]

        return render_template("update_book.html",
                               book_id=book_id,
                               authors=authors,
                               title=tit,
                               publisher=pub,
                               year=year,
                               editors=editors if editors else "",
                               volume=vol if vol else "",
                               number=num if num else "",
                               pages=pages if pages else "",
                               imported_month=month if month else "",
                               note=note if note else "",
                               months=months,
                               key = key,
                               author_count=author_count,
                               editor_count=editor_count)

    idx = 0
    while f"author_firstname_{idx}" in request.form:
        firstname = request.form.get(f"author_firstname_{idx}", "").strip()
        lastname = request.form.get(f"author_lastname_{idx}", "").strip()
        if firstname and lastname:
            authors.append(f"{firstname} {lastname}")
        idx += 1

    idx = 0
    while f"editor_firstname_{idx}" in request.form:
        firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
        lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
        if firstname and lastname:
            editors.append(f"{firstname} {lastname}")
        idx += 1

    reference = [authors, tit, pub, year, editors, vol, num, pages, month, note, key]

    try:
        validate_update(reference)
        validate_update_key(get_book_by_id(book_id).key, key)
        update_book(book_id, reference)
        flash('Reference updated successfully', "")
        return redirect("/view_references")
    except:
        flash("Something went wrong, please check that you have filled the required fields", "")
        return redirect("/update_book/"+str(book_id))

@app.route("/update_article/<int:article_id>", methods=["GET"])
def update_article_reference(article_id):
    reference = get_article_by_id(article_id)
    authors = reference.author
    author_count = len(authors) if authors else 1

    months = ["", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    return render_template("update_article.html",
                           article_id=reference.id,
                           authors=authors,
                           title=reference.title,
                           journal=reference.journal,
                           year=reference.year,
                           volume=reference.volume if reference.volume else "",
                           number=reference.number if reference.number else "",
                           pages=reference.pages if reference.pages else "",
                           imported_month=reference.month,
                           note=reference.note if reference.note else "",
                           months=months,
                           key=reference.key,
                           author_count=author_count,
                           reference=reference)

@app.route("/update_article/<int:article_id>", methods=["POST"])
def update_post_article_reference(article_id):
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    authors = []
    author_count = int(request.form.get("author_count", 1))

    tit = request.form["title"]
    jou = request.form["journal"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None
    key=request.form["key"]

    if request.form["action"] in ["add_author", "remove_author"]:


        if request.form["action"] == "add_author":
            author_count += 1

        elif request.form["action"] == "remove_author":
            author_count -= 1

        idx = 0
        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1

        reference = [authors, tit, jou, year, vol, num, pages, month, note, key]

        return render_template("update_article.html",
                               article_id=article_id,
                               authors=authors,
                               title=tit,
                               journal=jou,
                               year=year,
                               volume=vol if vol else "",
                               number=num if num else "",
                               pages=pages if pages else "",
                               imported_month=month if month else "",
                               note=note if note else "",
                               months=months,
                               key=key,
                               author_count=author_count)

    idx = 0
    while f"author_firstname_{idx}" in request.form:
        firstname = request.form.get(f"author_firstname_{idx}", "").strip()
        lastname = request.form.get(f"author_lastname_{idx}", "").strip()
        if firstname and lastname:
            authors.append(f"{firstname} {lastname}")
        idx += 1

    reference = [authors, tit, jou, year, vol, num, pages, month, note, key]

    try:
        validate_update(reference)
        validate_update_key(get_article_by_id(article_id).key, key)
        update_article(article_id, reference)
        flash('Reference updated successfully', "")
        return redirect("/view_references")
    except:
        flash("Something went wrong, please check that you have filled the required fields", "")
        return redirect("/update_article/"+str(article_id))

@app.route("/update_inproceeding/<int:inproceeding_id>", methods=["GET"])
def update_inproceeding_reference(inproceeding_id):

    reference = get_inproceeding_by_id(inproceeding_id)
    authors = reference.author
    author_count = len(authors) if authors else 1
    editors = reference.editor
    editor_count = len(editors) if editors else 1
    months = ["", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    return render_template("update_inproceeding.html",
                           inproceeding_id=reference.id,
                           authors=authors,
                           title=reference.title,
                           booktitle=reference.booktitle,
                           year=reference.year,
                           editors=editors if editors else "",
                           volume=reference.volume if reference.volume else "",
                           number=reference.number if reference.number else "",
                           series=reference.series if reference.series else "",
                           pages=reference.pages if reference.pages else "",
                           address=reference.address if reference.address else "",
                           imported_month=reference.month,
                           organization=reference.organization if reference.organization else "",
                           note=reference.note if reference.note else "",
                           publisher=reference.publisher if reference.publisher else "",
                           months=months,
                           key=reference.key,
                           author_count=author_count,
                           editor_count=editor_count,
                           reference=reference)

@app.route("/update_inproceeding/<int:inproceeding_id>", methods=["POST"])
def update_post_inproceeding_reference(inproceeding_id):

    authors = []
    author_count = int(request.form.get("author_count", 1))
    editors = []
    editor_count = int(request.form.get("editor_count", 1))

    months = ["", "January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    tit = request.form["title"]
    btit = request.form["booktitle"]
    jou = request.form["booktitle"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    ser = request.form.get("series") or None
    pages = request.form.get("pages") or None
    adr = request.form.get("address") or None
    month = request.form.get("month") or None
    org = request.form.get("organization") or None
    note = request.form.get("note") or None
    pub = request.form.get("publisher") or None
    key = request.form["key"]

    if request.form["action"] in ["add_author", "add_editor", "remove_author", "remove_editor"]:


        if request.form["action"] == "add_author":
            author_count += 1

        elif request.form["action"] == "add_editor":
            editor_count += 1

        elif request.form["action"] == "remove_author":
            author_count -= 1

        elif request.form["action"] == "remove_editor":
            editor_count -= 1

        idx = 0
        while idx < author_count:
            firstname = request.form.get(f"author_firstname_{idx}", "").strip()
            lastname = request.form.get(f"author_lastname_{idx}", "").strip()
            if firstname or lastname:
                authors.append(f"{firstname} {lastname}")
            idx += 1

        idx = 0
        while idx < editor_count:
            firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
            lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
            if firstname or lastname:
                editors.append(f"{firstname} {lastname}")
            idx += 1

        reference = [authors, tit, btit, year, editors, vol, num, ser, pages, adr, month, org, note, pub, key]

        return render_template("update_inproceeding.html",
                               inproceeding_id=inproceeding_id,
                               authors=authors,
                               title=tit,
                               booktitle=btit,
                               year=year,
                               editors=editors if editors else "",
                               volume=vol if vol else "",
                               number=num if num else "",
                               series=ser if ser else "",
                               pages=pages if pages else "",
                               address=adr if adr else "",
                               imported_month=month if month else "",
                               organization=org if org else "",
                               note=note if note else "",
                               publisher=pub if pub else "",
                               months=months,
                               key = key,
                               author_count=author_count,
                               editor_count=editor_count)

    idx = 0
    while f"author_firstname_{idx}" in request.form:
        firstname = request.form.get(f"author_firstname_{idx}", "").strip()
        lastname = request.form.get(f"author_lastname_{idx}", "").strip()
        if firstname and lastname:
            authors.append(f"{firstname} {lastname}")
        idx += 1

    idx = 0
    while f"editor_firstname_{idx}" in request.form:
        firstname = request.form.get(f"editor_firstname_{idx}", "").strip()
        lastname = request.form.get(f"editor_lastname_{idx}", "").strip()
        if firstname and lastname:
            editors.append(f"{firstname} {lastname}")
        idx += 1

    reference = [authors, tit, btit, year, editors, vol, num, ser, pages, adr, month, org, note, pub, key]

    try:
        validate_update(reference)
        validate_update_key(get_inproceeding_by_id(inproceeding_id).key, key)
        update_inproceeding(inproceeding_id, reference)
        flash("Reference updated successfully", "")
        return redirect("/view_references")
    except:
        flash("Something went wrong, please check that you have filled the required fields", "")
        return redirect("/update_inproceeding/"+str(inproceeding_id))


# testausta varten oleva reitti

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
