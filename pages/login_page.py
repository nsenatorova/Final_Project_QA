from .base_page import BasePage
from .locators import LoginPageLocators
import random
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not here"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not here"

    def generate_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(random.randint(111111111, 999999999))
        return email, password

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        confirmation_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirmation_input.send_keys(password)

        submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        submit.click()
