*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BOOK_URL}   http://${SERVER}/add_book
${ARTICLE_URL}  http://${SERVER}/add_article
${INPROCEEDING_URL}  http://${SERVER}/add_inproceeding
${VIEW_URL}  http://${SERVER}/view_references
${REMOVE_URL}  http://${SERVER}/remove_reference
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Todos
    Go To  ${RESET_URL}

Go To Remove Reference
    Go To  ${REMOVE_URL}

Go To Main Page
    Go to  ${HOME_URL}

Press Add Reference
    Click Button  add_reference

Submit Should Succeed With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Press View Reference
    Click Button  View references

Press Submit
    Click Button  Add Reference

Add Book Page Should Be Open
    Title Should Be  Create a reference

View References Page Should Be Open
    Title Should Be    View references

Removal Shold Succeed With Message
    [Arguments]  ${message}
    View References Page Should Be Open
    Page Should Contain  ${message}