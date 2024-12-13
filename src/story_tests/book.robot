*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser


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
    Leave Author Empty
    Press Update Book
    Submit Should Succeed With Message  You must provide at least one author or editor  

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

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Write Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Write Key
    [Arguments]  ${key}
    Input Text  key  ${key}

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

Leave Author Empty
    Clear Element Text  name:author_firstname_0
    
