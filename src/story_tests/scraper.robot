*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser


*** Test Cases ***
Successfully Import A Book Reference By DOI
    Go To Add Book
    Write Doi  10.1145/3603288
    Press Import
    Page Should Contain  Chuchu
    Page Should Contain  Fan
    Page Should Contain
        ...  Formal Methods for Safe Autonomy:
        ...  Data-driven Verification, Synthesis, and Applications
    Page Should Contain  ACM
    Page Should Contain  2024
    Page Should Contain  October

Successfully Import An Article Reference By DOI
    Go To Add Article
    Write Doi  10.1145/3695770
    Press Import
    Page Should Contain  Sergei
    Page Should Contain  Chuprov
    Page Should Contain
        ...  Data Quality Based Intelligent Instrument Selection
        ...  with Security Integration
    Page Should Contain  Journal of Data and Information Quality
    Page Should Contain  2024
    Page Should Contain  16
    Page Should Contain  January

Successfully Import An Inproceeding Reference By DOI
    Go To Add Inproceeding
    Write Doi  10.1145/3372923.3404836
    Press Import
    Page Should Contain  Michael
    Page Should Contain  Paris
    Page Should Contain
        ...  How to Assess the Exhaustiveness of Longitudinal Web Archives:
        ...  A Case Study of the German Academic Web
    Page Should Contain
        ...  Proceedings of the 31st ACM Conference
        ...  on Hypertext and Social Media
    Page Should Contain  2020
    Page Should Contain  January
    Page Should Contain ACM

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
