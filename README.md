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

Coverage report can be found in htmlcov directory. There is a index.html file which has coverage report for files which are tested by unitest. https://app.codecov.io/gh/KaEerola/IceLime

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

### User can edit a reference

In view_reference window is button "Edit a reference" clicking which user can choose reference he or she want to edit. It shows all fields of the reference and user can add or erase information.

### User can remove reference

In view_reference window is button "Remove a reference" clicking which user can choose certain reference from articles, inroceedings and books. By clicking submit button, user removes reference from references.

### User can fulfill reference fields using DOI

In every page where you are adding references. There is add DOI field where you can paste links of page of reference you want to add. It will automaticly fulfill input fields with reference information. 

## Sprint 4 

### User can use navigation bar at the top of application

The application now has a navigation bar at the top, where the user can move to the different windows.

### User can choose a key for a reference

When adding a new reference, the user is required to choose a unique key for the reference. This key is used to identify the reference in several other places (when actually using the references to cite in text).

### User can have references with multiple authors

When the user adds a reference, they can input multiple authors into the fields. They can also do this when editing a reference. User can dynamically increase or decrease the amount of authors in the input form using + and - buttons.

### User can have references with multiple editors

When the user adds a reference, they can input multiple editors into the fields. They can also do this when editing a reference. User can dynamically increase or decrease the amount of editors in the input form using + and - buttons. In the case of adding a book, there is a possibility for the user to only have editors instead of authors.

### User has a more pleasant experience with CSS and styling

The user has a great time when navigating through the application.

# Contributors


[//]: contributor-faces

<a href="https://github.com/lahgit"><img src="https://avatars.githubusercontent.com/u/149614775?s=400&v=4" title="lahgit" width="50" height="50"></a>
<a href="https://github.com/KaEerola"><img src="https://avatars.githubusercontent.com/u/157395194?v=4" title="KaEerola" width="50" height="50"></a>
<a href="https://github.com/acpeltol"><img src="https://avatars.githubusercontent.com/u/152793290?v=4" title="acpeltol" width="50" height="50"></a>
<a href="https://github.com/neononoen"><img src="https://avatars.githubusercontent.com/u/153290803?v=4" title="neononoen" width="50" height="50"></a>
<a href="https://github.com/kirkeruusalu"><img src="https://avatars.githubusercontent.com/u/128533486?v=4" title="kirkeruusalu" width="50" height="50"></a>
<a href="https://github.com/ratilmii"><img src="https://avatars.githubusercontent.com/u/32961917?v=4" title="ratilmii" width="50" height="50"></a>

[//]: contributor-faces







