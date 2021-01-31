import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    web_driver = None

    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()
