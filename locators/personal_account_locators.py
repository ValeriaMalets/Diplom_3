

class PersonalAccountLocators:
    button_login_to_account = '//button[contains(text(), "Войти в аккаунт")]'
    link_reset_password = '//a[contains(text(), "Восстановить пароль")]'
    link_registration = '//a[contains(text(), "Зарегистрироваться")]'
    link_profile = '//a[contains(text(), "Профиль")]'
    button_exit = '//button[contains(text(), "Выход")]'
    button_order_history = "//a[text()='История заказов']"
    button_order_history_selected = '//a[contains(@class, "Account_link_active__2opc9") and text()="История заказов"]'





class LoginLocators:
    input_email = '//label[contains(text(), "Email")]/following-sibling::input'
    input_password = '//label[contains(text(), "Пароль")]/following-sibling::input'
    button_login = '//button[contains(text(), "Войти")]'

