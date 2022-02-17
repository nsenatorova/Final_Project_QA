from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRICE = (By.CSS_SELECTOR, 'div.product_main .price_color')
    BASKET_IS_NOW = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
