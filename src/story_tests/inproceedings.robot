*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Succesfully Add An Inproceeding Reference With Required Info
    Go To Add Inproceeding
    Write Title  Vakava konferenssi
    Write Author  Jesse
    Write Booktitle  Konferenssi 1
    Write Year  2005
    Press Submit
    Submit Should Succeed With Message  Reference added succesfully

Unsuccesfully Adding An Article Reference
    Go To Add Inproceeding
    Press Submit
    Submit Should Fail With Message  You must put valid Author, Title, Booktitle And Year

*** Keywords ***
Go To Add Inproceeding
    Go To  ${INPROCEEDING_URL}

Write Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Write Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Write Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Write Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Add Inproceeding Page Should Be Open
    Title Should Be  Create a reference

Submit Should Fail With Message
    [Arguments]  ${message}
    Add Inproceeding Page Should Be Open
    Page Should Contain  ${message}