*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Succesfully Add An Inproceeding Reference With Required Info
    Go To Add Inproceeding
    Write Title  Vakava konferenssi
    Write Author Firstname  Jesse
    Write Author Lastname  Meikäläinen
    Write Booktitle  Konferenssi 1
    Write Year  2005
    Write Key  konferenssi
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Unsuccesfully Adding An Article Reference
    Go To Add Inproceeding
    Press Submit
    Submit Should Fail With Message  You must put valid Author, Title, Booktitle And Year

Successfully Edit Inproceeding Reference
    Go To Edit Reference
    Press Edit Inproceeding
    Update Reference Page Should Be Open
    Write Page  75
    Press Update Inproceeding
    Submit Should Succeed With Message  Reference updated successfully

Unsuccessfully Edit Inproceeding Reference
    Go To Edit Reference
    Press Edit Inproceeding
    Update Reference Page Should Be Open
    Leave Title Empty
    Press Update Inproceeding
    Submit Should Succeed With Message  Something went wrong, please check that you have filled the required fields 

Removing Of Inproceeding
    Go To Remove Reference
    Press Remove
    Removal Shold Succeed With Message  Reference removed succesfully

*** Keywords ***
Go To Add Inproceeding
    Go To  ${INPROCEEDING_URL}

Press Remove
    Click Button    Remove Inproceeding

Write Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Write Author Firstname
    [Arguments]  ${author_firstname}
    Input Text  author_firstname_0  ${author_firstname}

Write Author Lastname
    [Arguments]  ${author_lastname}
    Input Text  author_lastname_0  ${author_lastname}

Write Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Write Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Add Inproceeding Page Should Be Open
    Title Should Be  Create a reference

Submit Should Fail With Message
    [Arguments]  ${message}
    Add Inproceeding Page Should Be Open
    Page Should Contain  ${message}

Press Edit Inproceeding
    Click Button  Edit Inproceeding

Write Page
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Press Update Inproceeding
    Click Button  Update reference

Leave Title Empty
    Clear Element Text  name:title
