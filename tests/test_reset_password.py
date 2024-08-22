from config import WEB_LINK
from pages.reset_password_page import ResetPasswordPage
from tests.test_data import EMAIL


class TestStellarBurgersResetPassword:

    def test_go_to_reset_password_screen(self, browser):
        browser.get(WEB_LINK)
        reset_password_page = ResetPasswordPage(browser)
        reset_password_page.go_to_reset_password_from_login_page()
        reset_password_page.assert_reset_password_opened()

    def test_reset_password_input_email(self, browser):
        browser.get(WEB_LINK)
        reset_password_page = ResetPasswordPage(browser)
        reset_password_page.go_to_reset_password_from_login_page()
        reset_password_page.input_email(EMAIL)
        reset_password_page.submit_reset_password()
        reset_password_page.assert_input_new_password_page_opened()

    def test_toggle_password_visibility_activation(self, browser):
        browser.get(WEB_LINK)
        reset_password_page = ResetPasswordPage(browser)
        reset_password_page.go_to_reset_password_from_login_page()
        reset_password_page.input_email(EMAIL)
        reset_password_page.submit_reset_password()
        reset_password_page.wait_for_new_password_input()
        reset_password_page.toggle_password_visibility()
        reset_password_page.assert_password_field_active_after_toggle()
