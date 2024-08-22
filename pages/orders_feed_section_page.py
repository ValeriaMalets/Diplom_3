from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators
from locators.orders_feed_section_locators import OrderFeedLocators
from config import ORDER_FEED_URL


class OrderFeedPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_order_feed_section(self):
        self.browser.find_element(By.XPATH, OrderFeedLocators.order_feed_section_button).click()

    def assert_order_feed_url(self):
        assert self.browser.current_url == ORDER_FEED_URL, f"URL doesn't change to expected. Current URL: {self.browser.current_url}"

    def wait_element_visibility(self, xpath, timeout=5):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    def find_element(self, xpath):
        return self.browser.find_element(By.XPATH, xpath)

    def click_on_order(self):
        self.wait_element_visibility(OrderFeedLocators.order_card_in_feed)
        self.find_element(OrderFeedLocators.order_card_in_feed).click()
        self.wait_element_visibility(OrderFeedLocators.order_window_details)
        return self.find_element(OrderFeedLocators.order_window_title)

    def close_success_order_modal_window(self):
        # Wait until the close button is visible and clickable
        close_button = WebDriverWait(self.browser, 15).until(
            expected_conditions.element_to_be_clickable((By.XPATH, HomePageLocators.success_order_modal_x_button))
        )
        close_button.click()

        # Wait until the success order modal window is no longer visible
        WebDriverWait(self.browser, 15).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, HomePageLocators.success_order_modal_window))
        )

    def get_first_order_number(self):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, OrderFeedLocators.first_order_in_users_history))
        )
        order_number_element = self.browser.find_element(By.XPATH, OrderFeedLocators.first_order_in_users_history)
        return order_number_element.text

    def get_last_order_number(self):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, OrderFeedLocators.order_list_items))
        )
        order_elements = self.browser.find_elements(By.XPATH, OrderFeedLocators.order_list_items)
        last_order_element = order_elements[-1]
        order_number_element = last_order_element.find_element(By.XPATH, OrderFeedLocators.order_number)
        return order_number_element.text

    def scroll_and_click(self, xpath):
        element = self.browser.find_element(By.XPATH, HomePageLocators.button_account)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def close_modal_and_go_to_order_history(self, personal_account_page):
        self.close_success_order_modal_window()
        self.scroll_and_click(HomePageLocators.button_account)
        personal_account_page.go_to_order_history()

    def is_order_number_in_feed(self, order_number):
        try:
            order_xpath = f"//p[contains(text(), '{order_number}')]"
            self.wait_element_visibility(order_xpath)
            return True
        except:
            return False

    def assert_order_in_feed(self, order_number):
        order_present = self.is_order_number_in_feed(order_number)
        assert order_present, f"Order number {order_number} is not found in the order feed."

    def get_all_time_orders_count(self):
        count_element = WebDriverWait(self.browser, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, OrderFeedLocators.order_counter_all_time)
            )
        )
        return int(count_element.text)

    def verify_all_time_order_count_increased(self, initial_count):
        updated_count = self.get_all_time_orders_count()
        if updated_count != initial_count + 1:
            print(f"Expected order count to increase by 1. Initial: {initial_count}, Updated: {updated_count}")
        assert updated_count == initial_count + 1, (
            f"Expected order count to increase by 1. Initial: {initial_count}, Updated: {updated_count}"
        )

    def get_today_orders_count(self):
        count_element = WebDriverWait(self.browser, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, OrderFeedLocators.order_counter_today)
            )
        )
        return int(count_element.text)

    def verify_today_order_count_increased(self, initial_count):
        updated_count = self.get_today_orders_count()
        if updated_count != initial_count + 1:
            print(f"Expected order count to increase by 1. Initial: {initial_count}, Updated: {updated_count}")
        assert updated_count == initial_count + 1, (
            f"Expected order count to increase by 1. Initial: {initial_count}, Updated: {updated_count}")

    def verify_order_number_in_progress(self, order_number, timeout=15):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, OrderFeedLocators.order_in_progress))
        )
        orders_in_progress = self.browser.find_elements(By.XPATH, OrderFeedLocators.order_in_progress)
        for order in orders_in_progress:
            if order_number in order.text:
                print(f"Order number {order_number} is in progress.")
                return True
        print(f"Order number {order_number} is not found in the orders in progress.")
        return False
