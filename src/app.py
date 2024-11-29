from flask import redirect, render_template, request, jsonify, flash, send_file
from db_helper import reset_db
from repositories.book_repository import add_user_book, get_books
from repositories.article_repository import add_user_article, get_articles
from repositories.inproceeding_repository import add_user_inproceeding, get_inproceedings
from config import app, test_env
from util import validate_book
from scraper import get_book_data_by_doi
from export import Bibtex

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/add_reference", methods=["GET"])
def add_reference():

    return render_template("add_reference.html")

@app.route("/add_book", methods=["GET"])
def add_book():
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return render_template("add_book.html", months = months)

@app.route("/add_book", methods=["POST"])
def add_POST_book():

    if request.form["action"] == "reset":
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return render_template("add_book.html",
                               author_firstname="",
                               author_lastname="",
                               title="",
                               publisher="",
                               year="",
                               editor="",
                               volume="",
                               number="",
                               pages="",
                               month="",
                               note="",
                               months=months)

    aut_firstname = request.form["author_firstname"]
    aut_lastname = request.form["author_lastname"]
    tit = request.form["title"]
    pub = request.form["publisher"]
    year = request.form["year"]
    edt = request.form.get("editor") or None
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None

    reference = [aut_firstname, aut_lastname, tit, pub, year, edt, vol, num, pages, month, note]

    try:
        validate_book(reference)
        add_user_book(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
    except:
        flash('You must put valid Author, Title, Publisher And Year',"")
        return redirect("/add_book")

@app.route("/view_references")
def view_references():

    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    return render_template("view_references.html", books=books, articles=articles, inproceedings=inproceedings)

@app.route("/add_article", methods = ["GET"])
def add_article():

    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return render_template("add_article.html", months = months)

@app.route("/add_article", methods = ["POST"])
def add_POST_article():

    if request.form["action"] == "reset":
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return render_template("add_article.html",
                               author_firstname="",
                               author_lastname="",
                               title="",
                               journal="",
                               year="",
                               volume="",
                               number="",
                               pages="",
                               month="",
                               note="",
                               months=months)

    aut_firstname = request.form["author_firstname"]
    aut_lastname = request.form["author_lastname"]
    tit = request.form["title"]
    jou = request.form["journal"]
    year = request.form["year"]
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None

    reference = [aut_firstname, aut_lastname, tit, jou, year, vol, num, pages, month, note]

    try:
        validate_book(reference)
        add_user_article(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
    except:
        flash('You must put valid Author, Title, Journal And Year',"")
        return redirect("/add_article")


@app.route("/add_inproceeding", methods = ["GET"])
def add_inproceeding():

    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return render_template("add_inproceeding.html", months = months)

@app.route("/add_inproceeding", methods=["POST"])
def add_POST_inproceeding():

    if request.form["action"] == "reset":
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return render_template("add_inproceeding.html",
                               author_firstname="",
                               author_lastname="",
                               title="",
                               booktitle="",
                               year="",
                               editor="",
                               volume="",
                               number="",
                               series="",
                               pages="",
                               address="",
                               month="",
                               organization="",
                               publisher="",
                               months=months)

    aut_firstname = request.form["author_firstname"]
    aut_lastname = request.form["author_lastname"]
    tit = request.form["title"]
    bti = request.form["booktitle"]
    year = request.form["year"]
    edt = request.form.get("editor") or None
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    series = request.form.get("series") or None
    pages = request.form.get("pages") or None
    address = request.form.get("address") or None
    month = request.form.get("month") or None
    org = request.form.get("organization") or None
    publisher = request.form.get("publisher") or None

    reference = [aut_firstname, aut_lastname, tit, bti, year, edt, vol, num, series, pages, address, month, org, publisher]

    try:
        validate_book(reference)
        add_user_inproceeding(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
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
        editor_fullname = f"{data[6]} {data[7]}"

        return render_template("add_book.html",
                               author_firstname = data[0],
                               author_lastname = data[1],
                               editor = editor_fullname,
                               title = data[2],
                               publisher = data[3],
                               year = data[4],
                               months = months,
                               imported_month = data[5])

    except:
        flash("Failed to fetch the data, please check the DOI.", "")
        return redirect("/add_book")

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

    return render_template("remove_reference.html", books=books, articles=articles, inproceedings=inproceedings)

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
