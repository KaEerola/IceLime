*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser


*** Test Cases ***
Succesfully Add An Article Reference With Required Info
    Go To Add Article
    Write Author Firstname  Kalle
    Write Author Lastname  Eerola
    Write Title  Vakava tutkimus
    Write Journal  Tiede-lehti
    Write Year  2024
    Write Key  Tutkimus
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Unsuccesfully Adding An Article Reference
    Go To Add Article
    Press Submit
    Submit Should Fail With Message  You cannot have empty required fields

Successfully Edit Article Reference
    Go To Edit Reference
    Press Edit Article
    Update Reference Page Should Be Open
    Write Page  75
    Press Update Article
    Submit Should Succeed With Message  Reference updated successfully

Unsuccessfully Edit Article Reference
    Go To Edit Reference
    Press Edit Article
    Update Reference Page Should Be Open
    Leave Journal Empty
    Press Update Article
    Submit Should Succeed With Message  You cannot have empty required fields

Removing Of Article
    Go To Remove Reference
    Press Remove
    Removal Shold Succeed With Message  Reference removed succesfully

*** Keywords ***
Go To Add Article
    Go To  ${ARTICLE_URL}

Write Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Write Author Firstname
    [Arguments]  ${author_firstname}
    Input Text  author_firstname_0  ${author_firstname}

Write Author Lastname
    [Arguments]  ${author_lastname}
    Input Text  author_lastname_0  ${author_lastname}
    
Write Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Write Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Add Article Page Should Be Open
    Title Should Be  Create a reference

Submit Should Fail With Message
    [Arguments]  ${message}
    Add Article Page Should Be Open
    Page Should Contain  ${message}

Press Remove
    Click Button    Remove Article

Press Edit Article
    Click Button  Edit Article

Write Page
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Press Update Article
    Click Button  Update reference

Leave Journal Empty
    Clear Element Text  name:journal
