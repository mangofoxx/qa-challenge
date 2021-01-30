from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def execute_click(self, locator, timeout=10, message=''):

        WebDriverWait(
            self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=message
        ).click()

    def type(self, locator, text, timeout=10, message=''):

        WebDriverWait(
            self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=message
        ).send_keys(text)


