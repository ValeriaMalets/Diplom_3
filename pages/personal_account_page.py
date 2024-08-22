from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.personal_account_locators import LoginLocators, PersonalAccountLocators
from tests.test_data import EMAIL, PASSWORD
from config import WEB_LINK, LOGIN_SCREEN_URL
from pages.home_page import HomePage


class PersonalAccountPage:
    def __init__(self, browser):
        self.browser = browser
        self.home_page = HomePage(browser)

    def login(self):
        self.browser.get(WEB_LINK)
        self.home_page.go_to_personal_account()
        self.browser.find_element(By.XPATH, LoginLocators.input_email).send_keys(EMAIL)
        self.browser.find_element(By.XPATH, LoginLocators.input_password).send_keys(PASSWORD)
        self.browser.find_element(By.XPATH, LoginLocators.button_login).click()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator))
        )

    def assert_element_displayed(self, locator):
        assert self.browser.find_element(By.XPATH, locator).is_displayed()

    def assert_current_url(self, expected_url):
        assert self.browser.current_url == expected_url, f"URL doesn't change to expected. Current URL: {self.browser.current_url}"

    def click_element(self, locator):
        self.browser.find_element(By.XPATH, locator).click()

    def logout(self):
        logout_button = self.wait_for_element_to_be_clickable(PersonalAccountLocators.button_exit, timeout=15)
        logout_button.click()
        self.wait_for_element(LoginLocators.button_login)
        self.assert_current_url(LOGIN_SCREEN_URL)

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locator))
        )

    def go_to_order_history(self):
        self.wait_for_element(PersonalAccountLocators.button_order_history)
        self.click_element(PersonalAccountLocators.button_order_history)
        self.wait_for_element(PersonalAccountLocators.button_order_history_selected)
        self.assert_element_displayed(PersonalAccountLocators.button_order_history_selected)

    def go_to_constructor_after_login(self):
        self.login()
        self.home_page.go_to_personal_account()
        self.home_page.go_to_constructor()
