from pages.event_creation import Cards
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from tests.test_base import BaseTestCase


class TestUserDashboard(BaseTestCase):
    login_page: LoginPage
    profile_page: ProfilePage
    cards: Cards

    def test_check_doodle_info(self):
        """User can see general info about survey created on participants page

        Summary
            Given that user is registered and logged in
            When user creates new `survey`
                and fills in Title and fills in location `location`
                and fills in `note`
                and adds `at least 2` options
            When user click on Finish
            Then general info inputed by user is correct

        Steps
            Require: Registered user, Logged in user
            1. Click to create new Survey by clicking on +Create button
            2. Input the survey title
            3. Choose TBD location
            4. Input the note data
            5. Click Continiue
            6. Input one option data
            7. Click Continiue
            8. Click Finish
            9. Assert that general data is saved and correct
            on participants page
                (title, location, description)
        """
        # Provide test-related data
        test_data__general_card = dict(
            title='Title',
            location='Test Location',
            description='Test note'
        )
        test_data__survey_options = ['TESTOPT1', 'TESTOPT2']

        # Init pages to access objects and actions
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.cards = Cards(self.driver)

        # execute login step
        self.login_page.login__email_pass()

        # Init survey creation
        self.profile_page.open_menu__create()
        self.profile_page.menu_option_click__survey()

        # Fill in the data
        self.cards.general_card.wait_for_wizard_subtitle()
        self.cards.general_card.fill_information_card(**test_data__general_card)

        self.cards.survey_card.wait_for_wizard_subtitle()
        self.cards.survey_card.fill_in_survey_options(*test_data__survey_options)

        self.cards.settings_card.wait_for_wizard_subtitle()
        self.cards.settings_card.finilize_poll()

        # Perform assertions
        assert (
                self.cards.init_card.init_poll_title
                == test_data__general_card.get('title')
        )

        assert (
            self.cards.init_card.init_poll_location
            == test_data__general_card.get('location')
        )

        assert (
            self.cards.init_card.init_poll_note
            == test_data__general_card.get('description')
        )
