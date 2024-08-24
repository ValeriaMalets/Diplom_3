class OrderFeedLocators:
    order_feed_section_button = '//p[text()="Лента Заказов"]'
    order_card_in_feed = '//div/ul/li[1]'
    order_window_details = '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]'
    order_window_details_title = ('//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                  '"Modal_orderBox")]//h2')
    order_counter_all_time = '//div[contains(@class, "mb-15")]//p[contains(@class, "OrderFeed_number__2MbrQ")]'
    order_counter_today = '//p[text()="Выполнено за сегодня:"]/following-sibling::p'
    order_user_history_list_item = '//li[contains(@class, "OrderHistory_listItem__2x95r")]'
    order_number_from_user_history = ('.//div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[@class="text '
                                      'text_type_digits-default"]')
    order_number_from_success_modal = '//h2[contains(@class, "text_type_digits-large")]'
    order_list_in_progress = '//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]'
    order_number_in_progress = '//li[contains(@class, "text_type_digits-default") and contains(@class, "mb-2")]'
