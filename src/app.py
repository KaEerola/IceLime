from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_todos, create_todo, set_done
from repositories.book_repository import add_book, get_books
from config import app, test_env
from util import validate_todo

@app.route("/")
def index():

    return render_template("index.html") 

@app.route("/add_reference", methods=["GET"])
def add_reference():

    return render_template("add_reference.html")

@app.route("/view_references")
def view_references():
    books = get_books
    return render_template("view_references.html")
    


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
