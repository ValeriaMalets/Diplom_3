from config import WEB_LINK
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.orders_feed_section_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestStellarBurgersMainFunctionality:

    def test_go_to_constructor_from_my_account(self, browser):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.login()
        home_page = HomePage(browser)
        home_page.go_to_constructor()
        home_page.assert_constructor_page_is_open()

    def test_go_to_order_feed_section(self, browser):
        browser.get(WEB_LINK)
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.go_to_order_feed_section()
        order_feed_page.assert_order_feed_url()

    def test_ingredient_details_window_open(self, browser):
        browser.get(WEB_LINK)
        home_page = HomePage(browser)
        home_page.go_to_constructor()
        home_page.wait_for_element(HomePageLocators.tab_sauces).click()
        home_page.open_ingredient_details(HomePageLocators.sauce_spicy_x_image)
        home_page.assert_ingredient_details_window_is_open()

    def test_ingredient_details_close_by_x_button(self, browser):
        browser.get(WEB_LINK)
        home_page = HomePage(browser)
        home_page.go_to_constructor()
        home_page.wait_for_element(HomePageLocators.tab_sauces).click()
        home_page.open_ingredient_details(HomePageLocators.sauce_spicy_x_image)
        home_page.wait_for_element(HomePageLocators.sauce_spicy_x_details)
        home_page.close_ingredient_details()
        home_page.assert_complete_burger_title_is_visible()

    def test_ingredient_counter_increase(self, browser):
        browser.get(WEB_LINK)
        home_page = HomePage(browser)
        home_page.go_to_constructor()
        home_page.wait_for_element(HomePageLocators.tab_sauces).click()
        home_page.drag_and_drop_ingredient(HomePageLocators.sauce_spicy_x_image, HomePageLocators.order_basket)
        home_page.assert_ingredient_counter("1")

    def test_authorised_user_makes_order(self, browser):
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.login()
        home_page = HomePage(browser)
        home_page.go_to_personal_account()
        home_page.make_order()



