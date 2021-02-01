from selenium.webdriver.common.by import By

from .base import BasePage
from configtemplate.configbase import TestConfig


class ProfilePage(BasePage):

    PROFILE_PAGE_TITLE = 'Doodle – Dashboard'

    USER_MENU = (By.CSS_SELECTOR, '.UserMenu')
    CREATE_POLL = (By.CSS_SELECTOR, '.CreatePollMenu')

    CREATE_POLL_MENU = (By.CSS_SELECTOR, 'ul.Menu-list[role="menu"]')
    MENU_ITEM_SURVEY = (
        By.CSS_SELECTOR, '[data-testid="navigation-menu-create-text-poll"]'
    )

    def __init__(self, driver):
        super().__init__(driver)

    def visit(self):
        self.driver.get(TestConfig.USER_DASHBOARD)

    def get_profile_page_title(self):
        return self._get_title(
            self.PROFILE_PAGE_TITLE,
            message='Could not match page title'
        )

    def open_menu__create(self):
        """Method waits for a Create menu and clicks to open the menu"""
        self.wait_for_create_menu().click()

    def menu_option_click__survey(self):
        """Method executes click on an open menu on user page"""
        return self.execute_click(
            self.MENU_ITEM_SURVEY,
            message='Could not click on menu item Survey'
        )

    def wait_for_user_menu(self):
        """Method waits for user menu triger-button to become clickable"""
        return self.wait_for_element_to_be_clickable(
            self.USER_MENU,
            message='User menu is not clickable'
        )

    def wait_for_create_menu(self):
        """Method waits for `create` menu triger-button to become clickable"""
        return self.wait_for_element_to_be_clickable(
            self.CREATE_POLL,
            message='+Create menu is not clickable'
        )