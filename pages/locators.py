from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, '.btn-group > a.btn')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > strong')
    PRICE = (By.CSS_SELECTOR, 'div.product_main .price_color')
    SUM_IN_BASKET_NOW = (By.CSS_SELECTOR, 'div.alertinner > p > strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    ITEMS = (By.CSS_SELECTOR, '.basket-items')
