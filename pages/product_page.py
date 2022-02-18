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
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        assert actual_name == name_in_message, 'Actual name is different from one in message'

    def should_be_accurate_total_cost(self):
        actual_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.SUM_IN_BASKET_NOW).text
        assert actual_price == price_in_message, 'Price in message does not match the actual price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, though it should be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message hasn't disappeared"
