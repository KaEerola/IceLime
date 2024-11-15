from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_todos, create_todo, set_done
from repositories.book_repository import add_user_book, get_books
from config import app, test_env
from util import validate_todo

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

    print(aut , tit , pub ,year)

    add_user_book([aut, tit, pub, year])

    return render_template("index.html")

@app.route("/view_references")
def view_references():
    books = get_books()
    return render_template("view_references.html")
    


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
