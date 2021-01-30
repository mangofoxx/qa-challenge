from selenium.webdriver.common.by import By

from .base import BasePage
from configtemplate.configbase import TestConfig


class DoodleMainPage(BasePage):

    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.HeaderWidget-loginButton')

    def __init__(self, driver):
        super().__init__(driver)

    def visit(self):
        self.driver.get(TestConfig.BASE_URL)

    def login_button__click(self):
        self.execute_click(
            self.LOGIN_BUTTON, message='Could not click on Log in button'
        )
