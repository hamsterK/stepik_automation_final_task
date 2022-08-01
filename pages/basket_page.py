from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), 'Basket should be empty'

    def should_be_present_empty_basket_text(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT), 'Text about empty basket should be present'
