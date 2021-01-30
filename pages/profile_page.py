from selenium.webdriver.common.by import By

from configtemplate.configbase import TestConfig
from .base import BasePage


class ProfilePage(BasePage):

    PROFILE_PAGE_TITLE = 'Doodle – Dashboard'

    USER_MENU = (By.CSS_SELECTOR, '.UserMenu')

    def __init__(self, driver):
        super().__init__(driver)

    def visit(self):
        self.driver.get(TestConfig.USER_DASHBOARD)

    def get_profile_page_title(self):
        return self._get_title(
            self.PROFILE_PAGE_TITLE,
            message='Could not match page title'
        )

    def wait_for_user_menu(self):
        self.wait_for_element_to_be_clickable(
            self.USER_MENU,
            message='User menu is not clickable'
        )