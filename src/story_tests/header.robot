*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
You Can Use The Top Bar For Navigation
    Go To View References
    Press Edit References
    Page Should Be Edit References

*** Keywords ***
Go To View References
    Go To  ${VIEW_URL}

Press Edit References
    Click Button  Edit References

Page Should Be Edit References
    Title Should Be    View references
    