from selenium.webdriver.common.by import By


class OrderFeedLocators:
    order_feed_section_button = '//p[text()="Лента Заказов"]'
    order_feed_title = '//div[contains(@class, "OrderFeed_orderFeed")]/h1'
    order_card_in_feed = '//div/ul/li[1]'
    order_window_details = '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]'
    order_window_title = ('//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                          '"Modal_orderBox")]//h2')
    order_counter_all_time = '//div[contains(@class, "mb-15")]//p[contains(@class, "OrderFeed_number__2MbrQ")]'

    order_counter_today = '//p[text()="Выполнено за сегодня:"]/following-sibling::p'
    order_in_progress = '//ul[contains(@class, "OrderFeed_orderListReady")]/li'
    order_number_in_progress = ('//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, '
                                '"text_type_digits-default")]')
    order_list_items = '//li[contains(@class, "OrderHistory_listItem__2x95r")]'
    first_order_in_users_history = ('//li[contains(@class, "OrderHistory_listItem__2x95r mb-6")][1]//p[@class="text '
                                    'text_type_digits-default"]')
    order_number = './/div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[@class="text text_type_digits-default"]'
    order_number_success_mw = 'Modal_modal__title__2L34m'
