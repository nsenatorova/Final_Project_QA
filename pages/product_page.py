from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        self.browser.implicitly_wait(10)

    def should_be_correct_message(self):
        actual_name = self.browser.find_element(*ProductPageLocators.NAME).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART_MESSAGE).text
        assert actual_name in message, 'Actual name is different from one in message'

    def should_be_accurate_total_cost(self):
        actual_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_IS_NOW).text
        print(actual_price, price_in_message)
        assert actual_price == price_in_message, 'price in message does not match the actual price'
