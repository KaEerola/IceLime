# IceLime
Repository for the miniproject

![GHA workflow badge](https://github.com/KaEerola/IceLime/workflows/CI/badge.svg)

# Backlog link

https://docs.google.com/spreadsheets/d/17_ErdDH1jxFkODuv1_hyGJekEFNDRP_3ufEJWUNcTP8/edit?gid=0#gid=0

# Install guide:

Create a new folder and clone the repository:

`$ git clone git@github.com:KaEerola/IceLime.git`

Create a .env file inside the repository directory with the database url.

* `DATABASE_URL=postgresql:///{user}`
* `TEST_ENV = true`
* `SECRET_KEY={secret_key}`

Set up the environment inside the repository:

* `$ poetry install`

* `$ poetry shell`

Start PostgreSQL and run the database setup:

`$ python3 src/db_helper.py`

Now start the server:

`$ python3 src/index.py`

Server should start in the address:

http://127.0.0.1:5001/










