import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None,
    #                  help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: ru, en...(etc)')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print('\n\nStart chrome browser for test...')
    # browser_name = request.config.getoption('browser_name')
    # browser = None
    # user_language = request.config.getoption('language')
    # if browser_name == 'chrome':
    #     options = Options()
    #     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #     browser = webdriver.Chrome(options=options)
    #     print('\n\nStart chrome browser for test...')
    # elif browser_name == 'firefox':
    #     fp = webdriver.FirefoxProfile()
    #     fp.set_preference("intl.accept_languages", user_language)
    #     browser = webdriver.Firefox(firefox_profile=fp)
    #     print('\n\nStart firefox browser for test...')
    # else:
    #     print('Browser <browser_name> still not implemented')

    yield browser
    print('\nQuit browser...')
    browser.quit()