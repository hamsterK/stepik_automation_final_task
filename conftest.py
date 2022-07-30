import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose your language')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = webdriver.ChromeOptions()  # added to remove chrome logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # added to remove chrome logs
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser...')
    time.sleep(3)
    browser.quit()
