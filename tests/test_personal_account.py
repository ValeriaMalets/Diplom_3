from locators.personal_account_locators import PersonalAccountLocators
from pages.personal_account_page import PersonalAccountPage


class TestStellarBurgersMyAccount:

    def test_go_to_my_account_from_main_page(self, browser):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.login()
        personal_account_page.home_page.go_to_personal_account()
        personal_account_page.wait_for_element(PersonalAccountLocators.button_exit, timeout=2)
        personal_account_page.assert_element_displayed(PersonalAccountLocators.link_profile)

    def test_go_to_order_history_from_my_account(self, browser):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.login()
        personal_account_page.home_page.go_to_personal_account()
        personal_account_page.go_to_order_history()

    def test_logout_from_my_account(self, browser):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.login()
        personal_account_page.home_page.go_to_personal_account()
        personal_account_page.logout()

