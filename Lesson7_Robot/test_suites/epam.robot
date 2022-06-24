*** Settings ***
Documentation     EPAM website test using SeleniumLibrary.
...               Header localisation.
...               Working About Function.
...               Python Word Search.
Resource          ../keywords/keywords.robot
Variables         ../data/variables.py

*** Test Cases ***
Header Localisation
    [Setup]     Log to Console      ${TEST NAME} is started
    Open Browser To Home Page
    Make Sure Version Is English
    Check Links Translation
    [Teardown]    Close Browser

Working About Function
    [Setup]     Log to Console      ${TEST NAME} is started
    Open Browser To Home Page
    Click About Link In Header
    Check Link About Is Opened
    [Teardown]    Close Browser

Python Word Search
    [Setup]     Log to Console      ${TEST NAME} is started
    Open Browser To Home Page
    Click Search Button
    Enter The Python word and Click Find
    Check If Search Results Equal to 10
    [Teardown]    Close Browser

