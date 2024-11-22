from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.book_repository import add_user_book, get_books
from repositories.inproceeding_repository import add_user_inproceeding, get_inproceedings
from config import app, test_env
from util import validate_book

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/add_reference", methods=["GET"])
def add_reference():

    return render_template("add_reference.html")

@app.route("/add_book", methods=["GET"])
def add_book():

    return render_template("add_book.html")


@app.route("/add_book", methods=["POST"])
def add_POST_book():

    aut = request.form["author"]
    tit = request.form["title"]
    pub = request.form["publisher"]
    year = request.form["year"]
    edt = request.form.get("editor") or None
    vol = request.form.get("volume") or None
    num = request.form.get("number") or None
    pages = request.form.get("pages") or None
    month = request.form.get("month") or None
    note = request.form.get("note") or None

    reference = [aut, tit, pub, year, edt, vol, num, pages, month, note]

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
    return render_template("view_references.html", books=books)

 
@app.route("/add_article", methods = ["GET"])
def add_article():

    return render_template("add_article.html")

@app.route("/add_inproceeding", methods = ["GET"])
def add_inproceeding():

    return render_template("add_inproceeding.html")


@app.route("/add_inproceeding", methods=["POST"])
def add_POST_inproceeding():

    aut = request.form["author"]
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

    reference = [aut, tit, bti, year, edt, vol, num, series, pages, address, month, org, publisher]

    try:
        add_user_inproceeding(reference)
        flash('Reference added succesfully', "")
        return redirect("/")
    except:
        flash('You must put valid Author, Title, Publisher And Year',"")
        return redirect("/add_inproceeding")




# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })