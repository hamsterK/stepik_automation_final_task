from .base_page import BasePage
from .locators import LoginPageLocators
import time
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"Login" should be present in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form should be present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form should be present'

    def register_new_user(self, email, user):
        email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        email.send_keys(str(time.time()) + '@fakemail.org')
        new_password = random.randint(100000000, 999999999)
        password.send_keys(new_password)
        confirm_password.send_keys(new_password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


