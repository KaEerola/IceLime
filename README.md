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

# Coverage

Coverage report can be found in htmlcov directory. There is a index.html file which has coverage report for files which are tested by unitest. https://github.com/KaEerola/IceLime/blob/main/htmlcov/index.html 

# Definition of Done

## Sprint 1

### User can add a reference to a book with the required fields: author, title, publisher, year

There is a button on the main page that takes the user to the page for adding a new reference. From there, the user can click a link to add a new book reference. This takes the user to a page with the appropriate number of text fields (author, title, publisher, year). When the user has put in the proper values, they can add the reference to the database by clicking the add-button. If the user tries to add a year that hasn't come yet, or leaves fields empty, there is an error message.

### User can view the references that they have already added

There is a button on the main page that takes the user to the page for viewing the references that are currently in the database. This takes the user to a page titled "view your references", where each reference (currently just the book references) are gathered from the database and shown in a list. 


## Sprint 2

### User can add article and inproceeding references

There are two new types of references that can be added, articles and inproceedings. Adding work like in adding book reference.

### User can export a .bib file

There is a button on the view_reference page that creates a bibtex file. A .bib file yet can create only references for books.

### User can add optional fields to the references

There are optional input fields in the different types of references. User can choose which optional fields they want to fill out. If the fields are filled out correctly the user will get a message that the reference was added successfully. If the required fields are empty or year isn't correct the user will get an error message.

## Sprint 3

### The bibtex file prints Article and Inproceedings references

Application has now ability export inproceedings and article reference types into bibtex file. It can be done through a button in view_reference page.

### User can edit book reference

In view_reference window is button "Edit" clicking wich user can choose reference he or she want to edit. It shows all fields of the reference and user can add or erase information. Yet it only works for book reference types.

# Contributors


[//]: contributor-faces

<a href="https://github.com/lahgit"><img src="https://avatars.githubusercontent.com/u/149614775?s=400&v=4" title="lahgit" width="50" height="50"></a>
<a href="https://github.com/KaEerola"><img src="https://avatars.githubusercontent.com/u/157395194?v=4" title="KaEerola" width="50" height="50"></a>
<a href="https://github.com/acpeltol"><img src="https://avatars.githubusercontent.com/u/152793290?v=4" title="acpeltol" width="50" height="50"></a>
<a href="https://github.com/neononoen"><img src="https://avatars.githubusercontent.com/u/153290803?v=4" title="neononoen" width="50" height="50"></a>
<a href="https://github.com/kirkeruusalu"><img src="https://avatars.githubusercontent.com/u/128533486?v=4" title="kirkeruusalu" width="50" height="50"></a>
<a href="https://github.com/ratilmii"><img src="https://avatars.githubusercontent.com/u/32961917?v=4" title="ratilmii" width="50" height="50"></a>

[//]: contributor-faces







