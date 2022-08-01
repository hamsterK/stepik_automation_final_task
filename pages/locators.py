from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-lg[type="submit"]')
    PRODUCT_ADDED_SUCCESSFULLY_MESSAGE = (By.XPATH, '//*[text()[contains(.,"has been added")]]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    PRODUCT_NAME_IN_ADDED_SUCCESSFULLY_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    PRODUCT_PRICE_ON_PAGE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div.alert:nth-child(3) strong')
