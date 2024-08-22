class HomePageLocators:
    button_account = '//p[contains(text(), "Личный Кабинет")]'
    button_constructor = '//p[contains(text(), "Конструктор")]'
    tab_buns = '//span[contains(text(), "Булки")]'
    tab_sauces = '//span[contains(text(), "Соусы")]'
    sauce_spicy_x_image = '//img[@alt="Соус Spicy-X"]'
    sauce_spicy_x_details = '//h2[contains(text(), "Детали ингредиента")]'
    close_details_window_button = '//button[contains(@class, "Modal_modal__close")]'
    make_order_button = '//button[contains(text(), "Оформить")]'
    complete_burger_title = '//h1[text()="Соберите бургер"]'
    ingredient_counter = '//div[contains(@class, "counter_counter__ZNLkj")]'
    ingredient_counter_increased = '//p[@class="counter_counter__num__3nue1" and text()="1"]'
    order_basket = '//ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]'
    success_order_modal_window = '//section[contains(@class, "Modal_modal_opened__3ISw4")]'
    success_order_tick_image = '//img[@alt="tick animation"]'
    success_order_cook_text = '//p[contains(text(), "Ваш заказ начали готовить")]'
    success_order_modal_x_button = ('//button[contains(@class, "Modal_modal__close_modified__3V5XS") and contains('
                                    '@class, "Modal_modal__close__TnseK")]')

