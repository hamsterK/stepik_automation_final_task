from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs'] //span //a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    pass


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]/p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_FORM_PASSWORD = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_FORM_CONFIRM_PASSWORD = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-lg[type="submit"]')
    PRODUCT_ADDED_SUCCESSFULLY_MESSAGE = (By.XPATH, '//*[text()[contains(.,"has been added")]]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    PRODUCT_NAME_IN_ADDED_SUCCESSFULLY_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    PRODUCT_PRICE_ON_PAGE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div.alert:nth-child(3) strong')
