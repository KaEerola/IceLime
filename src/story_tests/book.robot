*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

Library    ../../.venv/lib/python3.11/site-packages/robot/libraries/Telnet.py

*** Test Cases ***
Succesfully Add A Book Reference
    Go To Add Book
    Write Author Firstname  Aleksis
    Write Author Lastname  Kivi
    Write Title  Seitsemän Veljestä
    Write Year  1870
    Write Publisher  Otava
    Write Key  Kivi
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Succesfully Add A Book Reference With Multiple Authors
    Go To Add Book
    Write Author Firstname  Kirke
    Write Author Lastname   Ruusalo
    Press Add Author
    Write Second Author Firstname  Kalle   
    Write Second Author Lastname   Eerola
    Write Title    SeriousBook
    Write Publisher    IceLime
    Write Year    2009
    Write Key    Book
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Succesfully Add A Book Without Authors Only Editors
    Go To Add Book
    Write Title    Kirja
    Write Publisher    IceLime
    Write Year    2012
    Write Editor Firstname  Miikka
    Write Editor Lastname    Meikäläinen
    Write Key    Kirja
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully
Unsuccesfully Adding A Book Reference
    Go To Add Book
    Press Submit
    Submit Should Fail With Message  You cannot have empty required fields

Successfully Edit Book Reference
    Go To Add Book
    Write Author Firstname  Aleksis
    Write Author Lastname  Kivi
    Write Title  Seitsemän Veljestä
    Write Year  1870
    Write Publisher  Otava
    Press Submit
    Go To Edit Reference
    Press Edit Book
    Update Reference Page Should Be Open
    Write Page  75
    Press Update Book
    Submit Should Succeed With Message  Reference updated successfully

Unsuccessfully Edit Book Reference
    Go To Add Book
    Write Author Firstname  Aleksis
    Write Author Lastname  Kivi
    Write Title  Seitsemän Veljestä
    Write Year  1870
    Write Publisher  Otava
    Press Submit
    Go To Edit Reference
    Press Edit Book
    Update Reference Page Should Be Open
    Leave Title Empty
    Press Update Book
    Submit Should Succeed With Message  You cannot have empty required fields

Removing Of Book
    Go To Add Book
    Write Author Firstname  Aleksis
    Write Author Lastname  Kivi
    Write Title  Seitsemän Veljestä
    Write Year  1870
    Write Publisher  Otava
    Write Key  Kivi
    Press Submit
    Go To Remove Reference
    Press Remove
    Removal Shold Succeed With Message  Reference removed succesfully

Using A Key That Is Already In Use
    Go To Add Book
    Write Author Firstname  Aleksis
    Write Author Lastname  Kivi
    Write Title  Seitsemän Veljestä
    Write Year  1870
    Write Publisher  Otava
    Write Key  Kivi
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully
    Write Author Firstname  Maija
    Write Author Lastname  Meikäläinen
    Write Title  Meikäläisen muistelmat
    Write Year  2020
    Write Publisher  Kustantaja
    Write Key  Kivi
    Press Submit
    Submit Should Fail With Message  You have already used this key

*** Keywords ***
Go To Add Book
    Go To  ${BOOK_URL}

Press Add Book Reference
    Click Button  add_book

Write Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Write Author Firstname
    [Arguments]  ${author_firstname}
    Input Text  author_firstname_0  ${author_firstname}

Write Author Lastname
    [Arguments]  ${author_lastname}
    Input Text  author_lastname_0  ${author_lastname}

Write Second Author Firstname
    [Arguments]  ${author_firstname}
    Input Text  author_firstname_1  ${author_firstname}

Write Second Author Lastname
    [Arguments]  ${author_lastname}
    Input Text  author_lastname_1  ${author_lastname}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Write Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Write Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Write Editor Firstname
    [Arguments]  ${editor_firstname}
    Input Text  editor_firstname_0  ${editor_firstname}

Write Editor Lastname
    [Arguments]  ${editor_lastname}
    Input Text  editor_lastname_0  ${editor_lastname}

Submit Should Fail With Message
    [Arguments]  ${message}
    Add Book Page Should Be Open
    Page Should Contain  ${message}

Press Remove
    Click Button  Remove Book

Press Edit Book
    Click Button  Edit Book

Write Page
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Press Update Book
    Click Button  Update Book

Leave Title Empty
    Clear Element Text  title
    
