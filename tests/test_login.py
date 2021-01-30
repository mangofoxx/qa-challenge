from pages.doodle_main_dash import DoodleMainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from tests.test_base import BaseTestCase


class TestLogInDoodle(BaseTestCase):
    login_page: LoginPage
    doodle_main_page: DoodleMainPage

    def test_login_from_root_page(self):
        """Test login email/password form

        Summary
            Given that user is registered on doodle.com website and user has
            valid credentials
            When user clicks on Log in button on doodle.com
            and enters valid email address
            and enters valid passwod
            and user clicks Log in button
            Then user is logged in to account

        Steps:
            1. Using browser navigate to https://doodle.com/en/
            2. Wait for Login button to be clickable
            3. Click on Log in button
            4. Verify that form has loaded into the view
            5. Verify that email input is visible
            6. Verify that password input is visible
            7. Type in valid email && valid password
            8. Click on Login button
            9. Verify that user login is success
        """
        self.login_page = LoginPage(self.driver)
        self.doodle_main_page = DoodleMainPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

        # Using browser navigate to https://doodle.com/en/
        self.doodle_main_page.visit()
        # 2. Wait for Login button to be clickable > Click on Log in button
        self.doodle_main_page.login_button__click()

        self.login_page.wait_for_auth_page()
        self.login_page.wait_for_email_input()
        self.login_page.wait_for_password_input()

        page_title = self.login_page.get_login_page_title()

        assert page_title == LoginPage.LOGIN_PAGE_TITLE,\
            f'Expected page title { LoginPage.LOGIN_PAGE_TITLE} ' \
            f',got {page_title}'

        self.login_page.fill_in_email()
        self.login_page.fill_in_password()
        self.login_page.confirm_login()

        self.profile_page.wait_for_user_menu()

        page_title = self.profile_page.get_profile_page_title()

        assert page_title == ProfilePage.PROFILE_PAGE_TITLE, \
            f'Expected page title {ProfilePage.PROFILE_PAGE_TITLE} ' \
            f',got {page_title}'
