*** Settings ***
Documentation     Resourse file with common keywords for epam project testing.
Library           SeleniumLibrary

*** Keywords ***
Open Browser To Home Page
    Open Browser    ${HOME_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Home Page Should Be Open

Home Page Should Be Open
    Title Should Be    EPAM | Enterprise Software Development, Design & Consulting

Make Sure Version Is English
    Log to Console      Verifying site version...
    Element Text Should Be  //button[@class='location-selector__button']    Global (EN)
    Log to Console      Done

Check Links Translation
    Log to Console      Verifying links translation...
    Element Text Should Be  css:.top-navigation__item-link[href="/services"]    SERVICES
    Element Text Should Be  css:.top-navigation__item-link[href="/how-we-do-it"]    HOW WE DO IT
    Element Text Should Be  css:.top-navigation__item-link[href="/our-work"]    OUR WORK
    Element Text Should Be  css:.top-navigation__item-link[href="/insights"]    INSIGHTS
    Element Text Should Be  css:.top-navigation__item-link[href="/about"]    ABOUT
    Element Text Should Be  css:.top-navigation__item-link[href="/careers"]    CAREERS
    Log to Console      Done

Click About Link In Header
    Log to Console      Opening About page...
    Click Link      css:.top-navigation__item-link[href="/about"]
    Log to Console      Done

Check Link About Is Opened
    Log to Console      Verifying site location...
    Location Should Be      https://www.epam.com/about
    Log to Console      Done

Click Search Button
    Log to Console      Going to search page...
    Click Element    //button[@class='header-search__button header__icon']
    Log to Console      Done

Enter The Python word and Click Find
    Input Text    id:new_form_search    Python
    Log to Console      Searching for "Python" word...
    Click Button    //button[normalize-space()='Find']


Check If Search Results Equal to 10
    Log to Console      Waiting for search results...
    Wait Until Element Is Visible   css:.search-results__counter    10
    Log to Console      Search results were displayed
    Log to Console      Test will fail as expected...
    Element Text Should Be      css:.search-results__counter       10 RESULTS FOR "PYTHON"
