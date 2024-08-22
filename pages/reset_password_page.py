from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import WEB_LINK, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from locators.home_page_locators import HomePageLocators
from locators.personal_account_locators import PersonalAccountLocators
from locators.reset_password_locators import ResetPasswordLocators, ForgotPasswordLocators


class ResetPasswordPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_reset_password_from_login_page(self):
        self.browser.get(WEB_LINK)
        self.browser.find_element(By.XPATH, HomePageLocators.button_account).click()
        self.browser.find_element(By.XPATH, PersonalAccountLocators.link_reset_password).click()

    def go_to_reset_password_from_login_page(self):
        self.browser.get(WEB_LINK)

        # Wait for any overlay or modal to disappear
        WebDriverWait(self.browser, 10).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )

        # Scroll the element into view
        account_button = self.browser.find_element(By.XPATH, HomePageLocators.button_account)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", account_button)
        account_button.click()

        reset_password_link = self.browser.find_element(By.XPATH, PersonalAccountLocators.link_reset_password)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", reset_password_link)
        reset_password_link.click()

    def assert_reset_password_opened(self):
        assert self.browser.current_url == FORGOT_PASSWORD_URL, f"URL doesn't change to expected. Current URL: {self.browser.current_url}"

    def input_email(self, email):
        self.browser.find_element(By.XPATH, ForgotPasswordLocators.input_email).send_keys(email)

    def submit_reset_password(self):
        self.browser.find_element(By.XPATH, ForgotPasswordLocators.button_reset_password).click()

    def assert_input_new_password_page_opened(self, timeout=10):
        WebDriverWait(self.browser, timeout).until(expected_conditions.url_to_be(RESET_PASSWORD_URL))
        assert self.browser.current_url == RESET_PASSWORD_URL, f"URL doesn't change to expected. Current URL: {self.browser.current_url}"

    def toggle_password_visibility(self):
        self.browser.find_element(By.XPATH, ResetPasswordLocators.eye_button).click()

    def wait_for_new_password_input(self, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ResetPasswordLocators.input_new_password))
        )
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ResetPasswordLocators.eye_button))
        )
        return self.browser.find_element(By.XPATH, ResetPasswordLocators.input_new_password)

    def assert_password_field_active_after_toggle(self, timeout=10):
        self.browser.find_element(By.XPATH, ResetPasswordLocators.eye_button).click()
        active_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located(ResetPasswordLocators.new_password_active)
        )
        active_class = active_element.get_attribute("class")
        assert "input_status_active" in active_class, \
            "Password field should be active after clicking the visibility toggle button"
