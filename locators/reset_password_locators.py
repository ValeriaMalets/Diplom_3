from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    input_email = '//label[contains(text(), "Email")]/following-sibling::input'
    button_reset_password = '//button[contains(text(), "Восстановить")]'
    link_login = '//a[contains(text(), "Войти")]'
    remember_password_text_label = '//p[contains(text(), "Вспомнили пароль?")]'
    reset_password_screen_title = '//h2[contains(text(), "Восстановление пароля")]'


class ResetPasswordLocators:
    input_new_password = '//label[contains(text(), "Пароль")]/following-sibling::input[@type="password"]'
    input_email_code = '//label[contains(text(), "Введите код из письма")]/following-sibling::input'
    eye_button = '//div[contains(@class, "input__icon") and contains(@class, "input__icon-action")]'
    new_password_active = (By.XPATH, "//div[contains(@class, 'input_status_active')]")

