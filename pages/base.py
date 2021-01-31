from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        pass

    def execute_click(self, locator, timeout=10, message=''):
        self.wait_for_element_to_be_clickable(
            locator, timeout=timeout, message='not clickabe'
        ).click()

    def type(self, locator, text, timeout=10, message=''):
        self.wait_for_element_to_be_visible(
            locator, timeout=timeout, message=message
        ).send_keys(text)

    def wait_for_element_to_be_clickable(self, locator, timeout=30, message=''):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=message
        )

    def wait_for_element_to_be_visible(self, locator, timeout=10, message=''):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=message
        )

    def wait_for_elements_to_be_visible(self, locator, timeout=10, message=''):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator),
            message=message
        )

    def is_visible(self, locator, timeout=10, message=''):
        return bool(self.wait_for_element_to_be_visible(
            locator, timeout=timeout, message=message
        ))

    def _get_title(self, title, timeout=10, message=''):
        WebDriverWait(self.driver, timeout).until(
            EC.title_is(title),
            message=message
        )
        return self.driver.title

    def get_element_text(self, locator, timeout=10, message=''):
        return self.wait_for_element_to_be_visible(
            locator, timeout=timeout, message=message
        ).text
