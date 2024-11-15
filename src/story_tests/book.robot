*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Succesfully Add A Book Reference
    Go To Main Page
    Press Add Reference
    Press Add Book
    Write Author  Aleksis Kivi
    Write Title  Seitsemän Veljestä
    Write Year  1870
    Write Publisher  Otava
    Press Submit
    Main Page Should Be Open

Viewing After Succesfully Adding A Book
    Press View Reference

*** Keywords ***
Press Add Book Reference
    Click Button  Add book

Write Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Write Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Write Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}