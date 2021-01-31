from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .base import BasePage


class Card(BasePage):

    NEXT_BUTTON = None
    WIZARD_SUBTITLE = None

    def __init__(self, driver):
        super().__init__(driver)

    def confirm_button__continue(self):
        ActionChains(self.driver).move_to_element(
            self.wait_for_element_to_be_clickable(
                (By.CSS_SELECTOR, self.NEXT_BUTTON),
            )
        ).click().perform()

    def wait_for_wizard_subtitle(self):
        self.wait_for_element_to_be_visible(
            self.WIZARD_SUBTITLE,
            timeout=30,
            message='Wizard subtitle not visible'
        )


class GeneralInformationCard(Card):
    NEXT_BUTTON = '#d-wizardGeneralInformationPage button.d-nextButton'
    WIZARD_SUBTITLE = (
        By.CSS_SELECTOR, '#d-wizardGeneralInformationPage .d-wizardStepSubtitle'
    )

    D_TITLE = (By.CSS_SELECTOR, 'input#d-pollTitle')
    D_LOCATION = (By.CSS_SELECTOR, 'input#d-pollLocation')
    D_NOTE = (By.CSS_SELECTOR, 'textarea#d-pollDescription')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_title_input(self, text=''):
        self.type(
            self.D_TITLE, text=text, message='Could not type into title'
        )

    def fill_location_input(self, text=''):
        self.type(
            self.D_LOCATION, text=text, message='Could not type into location'
        )

    def fill_in_description(self, text=''):
        self.type(
            self.D_NOTE, text=text, message='Could not type into note text'
        )

    def fill_information_card(self, title='', location='', description=''):
        """Fill information with given data
        :return:
        """
        self.fill_title_input(title)
        self.fill_location_input(location)
        self.fill_in_description(description)

        self.confirm_button__continue()


class SurveyOptionsCard(Card):

    D_TEXT_OPTIONS = (By.TAG_NAME, 'ol')
    NEXT_BUTTON = '#d-wizardOptionsNavigationView button.d-nextButton'
    WIZARD_SUBTITLE = (
        By.CSS_SELECTOR, '#d-wizardOptionsPage .d-wizardStepSubtitle'
    )

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def survey_options__container(self) -> WebElement:
        return self.wait_for_element_to_be_visible(
            self.D_TEXT_OPTIONS,
            message='Text option list not visible'
        )

    @property
    def survey_options__list(self):
        return self.survey_options__container.find_elements_by_tag_name('li')

    def fill_in_survey_options(self, *data):

        for index, data_item in enumerate(data):
            (self.survey_options__list[index]
             .find_element_by_tag_name('textarea')
             .send_keys(data_item))

        self.confirm_button__continue()


class SettingsCard(Card):

    NEXT_BUTTON = '#d-wizardSettingsPage button.d-nextButton'

    WIZARD_SUBTITLE = (
        By.CSS_SELECTOR, '#d-wizardSettingsPage .d-wizardStepSubtitle'
    )

    def finilize_poll(self):
        self.confirm_button__continue()


class InitiatorCard(Card):

    INIT_POLL_TITLE = (By.CSS_SELECTOR, '#d-participationPage h1.d-pollTitle')
    INIT_POLL_LOC = (By.CSS_SELECTOR, '#d-participationPage .d-locationName')
    INIT_POLL_NOTE = (By.CSS_SELECTOR, '#d-participationPage .d-content')

    @property
    def init_poll_title(self):
        return self.get_element_text(self.INIT_POLL_TITLE)

    @property
    def init_poll_location(self):
        return self.get_element_text(self.INIT_POLL_LOC)

    @property
    def init_poll_note(self):
        return self.get_element_text(self.INIT_POLL_NOTE)


class Cards:

    def __init__(self, driver):
        self.driver = driver

    @property
    def survey_card(self):
        return SurveyOptionsCard(self.driver)

    @property
    def general_card(self):
        return GeneralInformationCard(self.driver)

    @property
    def settings_card(self):
        return SettingsCard(self.driver)

    @property
    def init_card(self):
        return InitiatorCard(self.driver)
