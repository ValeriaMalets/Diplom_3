from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_constructor(self):
        self.browser.find_element(By.XPATH, HomePageLocators.button_constructor).click()

    def assert_constructor_page_is_open(self):
        assert self.browser.find_element(By.XPATH,
                                         HomePageLocators.tab_buns).is_displayed(), "Constructor page did not open"

    def go_to_personal_account(self):
        self.browser.find_element(By.XPATH, HomePageLocators.button_account).click()

    def wait_for_element(self, xpath, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    def open_ingredient_details(self, ingredient_xpath):
        self.browser.find_element(By.XPATH, ingredient_xpath).click()

    def assert_ingredient_details_window_is_open(self):
        assert self.wait_for_element(
            HomePageLocators.sauce_spicy_x_details).is_displayed(), "Details window didn't open"

    def close_ingredient_details(self):
        self.browser.find_element(By.XPATH, HomePageLocators.close_details_window_button).click()

    def assert_complete_burger_title_is_visible(self):
        assert self.wait_for_element(
            HomePageLocators.complete_burger_title).is_displayed(), "Complete burger title is not visible"

    def assert_ingredient_counter(self, expected_count):
        counter_text = self.wait_for_element(HomePageLocators.ingredient_counter_increased).text
        assert counter_text == expected_count, f"Expected counter value to be '{expected_count}', but got '{counter_text}'"

    def drag_and_drop_ingredient(self, ingredient_xpath, basket_xpath):
        ingredient = self.browser.find_element(By.XPATH, ingredient_xpath)
        basket = self.browser.find_element(By.XPATH, basket_xpath)
        actions = ActionChains(self.browser)
        actions.drag_and_drop(ingredient, basket).perform()

    def click_order_button(self):
        self.browser.find_element(By.XPATH, HomePageLocators.make_order_button).click()

    def make_order(self):
        self.go_to_constructor()
        self.wait_for_element(HomePageLocators.tab_sauces).click()
        self.wait_for_element(HomePageLocators.tab_buns).click()
        sleep(5)
        self.drag_and_drop_ingredient(HomePageLocators.cr_bun, HomePageLocators.order_basket)
        self.click_order_button()
        return self.wait_for_order_number_change()

    def wait_for_order_number_change(self, initial_number="9999", timeout=60):
        order_number_locator = (By.XPATH, '//h2[contains(@class, "text_type_digits-large")]')
        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.find_element(*order_number_locator).text != initial_number
        )
        new_number = self.browser.find_element(*order_number_locator).text
        return new_number
