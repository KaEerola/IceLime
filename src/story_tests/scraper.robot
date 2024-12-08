*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser


*** Test Cases ***
Successfully Import A Book Reference By DOI
    Go To Add Book
    Write Doi  10.1145/3603288
    Press Import
    ${firstname}  Get Value  name=author_firstname_0
    Should Be Equal As Strings  ${firstname}  Chuchu
    ${lastname}  Get Value  name=author_lastname_0
    Should Be Equal As Strings  ${lastname}  Fan
    ${title}  Get Value  name=title
    Should Be Equal As Strings  ${title}  Formal Methods for Safe Autonomy: Data-driven Verification, Synthesis, and Applications
    ${publisher}  Get Value  name=publisher
    Should Be Equal As Strings  ${publisher}  ACM
    ${year}  Get Value  name=year
    Should Be Equal  ${year}  2024
    ${month}  Get Value  name=month
    Should Be Equal As Strings  ${month}  October

Successfully Import An Article Reference By DOI
    Go To Add Article
    Write Doi  10.1145/3695770
    Press Import
    ${firstname}  Get Value  name=author_firstname_0
    Should Be Equal As Strings  ${firstname}  Sergei
    ${lastname}  Get Value  name=author_lastname_0
    Should Be Equal As Strings  ${lastname}  Chuprov
    ${title}  Get Value  name=title
    Should Be Equal As Strings  ${title}  Data Quality Based Intelligent Instrument Selection with Security Integration
    ${journal}  Get Value  name=journal
    Should Be Equal As Strings  ${journal}  Journal of Data and Information Quality
    ${year}  Get Value  name=year
    Should Be Equal  ${year}  2024
    ${volume}  Get Value  name=volume
    Should Be Equal  ${volume}  16
    ${month}  Get Value  name=month
    Should Be Equal As Strings  ${month}  January

Successfully Import An Inproceeding Reference By DOI
    Go To Add Inproceeding
    Write Doi  10.1145/3372923.3404836
    Press Import
    ${firstname}  Get Value  name=author_firstname
    Should Be Equal As Strings  ${firstname}  Michael
    ${lastname}  Get Value  name=author_lastname
    Should Be Equal As Strings  ${lastname}  Paris
    ${title}  Get Value  name=title
    Should Be Equal As Strings  ${title}  How to Assess the Exhaustiveness of Longitudinal Web Archives: A Case Study of the German Academic Web
    ${booktitle}  Get Value  name=booktitle
    Should Be Equal As Strings  ${booktitle}  Proceedings of the 31st ACM Conference on Hypertext and Social Media
    ${year}  Get Value  name=year
    Should Be Equal  ${year}  2020
    ${month}  Get Value  name=month
    Should Be Equal As Strings  ${month}  January
    ${publisher}  Get Value  name=publisher
    Should Be Equal As Strings  ${publisher}  ACM

Unsuccessfully Import A Book Reference From DOI
    Go To Add Book
    Write Doi  0
    Press Import
    Page Should Contain  Failed to fetch the data, please check the DOI.

Unsuccessfully Import An Article Reference From DOI
    Go To Add Article
    Write Doi  0
    Press Import
    Page Should Contain  Failed to fetch the data, please check the DOI.

Unsuccessfully Import An Inproceeding Reference From DOI
    Go To Add Inproceeding
    Write Doi  0
    Press Import
    Page Should Contain  Failed to fetch the data, please check the DOI.

*** Keywords ***
Go To Add Book
    Go To  ${BOOK_URL}

Go To Add Article
    Go To  ${ARTICLE_URL}

Go To Add Inproceeding
    Go To  ${INPROCEEDING_URL}

Write Doi
    [Arguments]  ${doi}
    Input Text  doi  ${doi}
