import allure
from time import sleep


from config import WEB_LINK
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.orders_feed_section_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedSection:

    @allure.title("View Order Details")
    def test_open_order_details(self, browser):
        browser.get(WEB_LINK)
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.go_to_order_feed_section()
        order_feed_page.click_on_order()

    @allure.title("Check User's Order exists in Feed Section")
    def test_user_orders_in_the_order_feed_section(self, browser):
        browser.get(WEB_LINK)
        order_feed_page = OrderFeedPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.go_to_constructor_after_login()
        home_page = HomePage(browser)
        home_page.make_order()
        order_feed_page.close_success_order_modal_window()
        order_feed_page.scroll_and_click(HomePageLocators.button_account)
        personal_account_page.go_to_order_history()
        last_order_number = order_feed_page.get_last_order_number()
        order_feed_page.go_to_order_feed_section()
        order_feed_page.assert_order_in_feed(last_order_number)

    @allure.title("Check All-Time Order Counter is increased")
    def test_counter_orders_all_the_time(self, browser):
        browser.get(WEB_LINK)
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.go_to_order_feed_section()
        initial_count = order_feed_page.get_all_time_orders_count()
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.go_to_constructor_after_login()
        home_page = HomePage(browser)
        home_page.make_order()
        order_feed_page.close_success_order_modal_window()
        sleep(3)
        order_feed_page.go_to_order_feed_section()
        order_feed_page.verify_all_time_order_count_increased(initial_count)

    @allure.title("Check Today's Order Counter is increased")
    def test_counter_orders_today(self, browser):
        browser.get(WEB_LINK)
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.go_to_order_feed_section()
        initial_count = order_feed_page.get_today_orders_count()
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.go_to_constructor_after_login()
        home_page = HomePage(browser)
        home_page.make_order()
        order_feed_page.close_success_order_modal_window()
        sleep(5)
        order_feed_page.go_to_order_feed_section()
        order_feed_page.verify_today_order_count_increased(initial_count)

    @allure.title("Check Order Number is In Progress")
    def test_order_number_in_progress(self, browser):
        browser.get(WEB_LINK)
        order_feed_page = OrderFeedPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        personal_account_page.go_to_constructor_after_login()
        home_page = HomePage(browser)
        home_page.make_order()
        order_number = order_feed_page.get_order_number_from_modal()
        order_feed_page.close_success_order_modal_window()
        order_feed_page.go_to_order_feed_section()
        order_feed_page.assert_order_number_in_progress(order_number)
