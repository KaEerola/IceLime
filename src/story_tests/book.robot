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
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Unsuccesfully Adding A Book Reference
    Go To Add Book
    Press Submit
    Submit Should Fail With Message  You must put valid Author, Title, Publisher And Year

Removing Of Book
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
    Input Text  author_firstname  ${author_firstname}

Write Author Lastname
    [Arguments]  ${author_lastname}
    Input Text  author_lastname  ${author_lastname}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Write Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Submit Should Fail With Message
    [Arguments]  ${message}
    Add Book Page Should Be Open
    Page Should Contain  ${message}

Press Remove
    Click Button    Remove Book
    