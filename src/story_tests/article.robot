*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser


*** Test Cases ***
Succesfully Add An Article Reference With Required Info
    Go To Add Article
    Write Author  Kalle Eerola
    Write Title  Vakava tutkimus
    Write Journal  Tiede-lehti
    Write Year  2024
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Unsuccesfully Adding An Article Reference
    Go To Add Article
    Press Submit
    Submit Should Fail With Message  You must put valid Author, Title, Journal And Year

*** Keywords ***
Go To Add Article
    Go To  ${ARTICLE_URL}

Write Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Write Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Write Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Add Article Page Should Be Open
    Title Should Be  Create a reference

Submit Should Fail With Message
    [Arguments]  ${message}
    Add Article Page Should Be Open
    Page Should Contain  ${message}