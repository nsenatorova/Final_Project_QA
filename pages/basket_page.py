from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Isn't empty as it should be"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Isn't empty as it should be"

    def should_be_empty(self):
        self.should_be_no_items()
        self.should_be_empty_text()

    def should_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Is empty but it shouldn't be"
