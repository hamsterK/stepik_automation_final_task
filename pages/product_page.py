from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET)
        add_to_basket_button.click()

    def should_be_correct_name_of_product_added(self):
        product_on_page = self.return_text(*ProductPageLocators.PRODUCT_NAME)
        product_in_basket = self.return_text(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_SUCCESSFULLY_MESSAGE)
        assert product_in_basket == product_on_page, 'Name of added product is not correct'

    def should_be_correct_price_in_basket(self):
        price_of_product_on_page = self.return_price(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        price_of_product_in_basket = self.return_price(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert price_of_product_in_basket == price_of_product_on_page, 'Price on page and in basket is not the same'

    def should_be_displayed_message_about_added_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESSFULLY_MESSAGE), 'Product has been ' \
                                                                                                 'added... message is' \
                                                                                                 ' absent '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESSFULLY_MESSAGE), 'Success message ' \
                                                                                                     'should not be ' \
                                                                                                     'displayed '

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_SUCCESSFULLY_MESSAGE), 'Success message should disappear'

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert present")
        except NoAlertPresentException:
            print("No alert present")
