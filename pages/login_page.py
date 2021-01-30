from selenium.webdriver.common.by import By

from .base import BasePage
from configtemplate.configbase import TestConfig


class LoginPage(BasePage):

    LOGIN_PAGE_TITLE = 'Doodle'

    AUTH_PAGE = (By.CSS_SELECTOR, '.AuthenticationPage')

    HEADER_LOGO = (By.CSS_SELECTOR, 'header .DoodleLogo')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.Button--green')

    def __init__(self, driver):
        super().__init__(driver)

    def visit(self):
        self.driver.get(TestConfig.LOGIN_PAGE_URL)

    def wait_for_auth_page(self):
        self.wait_for_element_to_be_visible(
            self.AUTH_PAGE,
            message='Auth page not visible'
        )

    def wait_for_email_input(self):
        self.wait_for_element_to_be_visible(
            self.EMAIL_INPUT,
            message='Email input not visible'
        )

    def wait_for_password_input(self):
        self.wait_for_element_to_be_visible(
            self.PASSWD_INPUT,
            message='Password input not visible'
        )

    def get_login_page_title(self):
        return self._get_title(
            self.LOGIN_PAGE_TITLE,
            message='Could not match page title'
        )

    def fill_in_email(self, value=TestConfig.USER_EMAIL):
        self.type(self.EMAIL_INPUT, value)

    def fill_in_password(self, value=TestConfig.USER_PASSWD):
        self.type(self.PASSWD_INPUT, value)

    def confirm_login(self):
        self.execute_click(
            self.LOGIN_BUTTON, message='Could not confirm login'
        )
