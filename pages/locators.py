from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.col-sm-6.register_form")
    LOGIN_REGISTER_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ALERT_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ALERT_PRICE_BOOK = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_WITHOUT_ITEMS_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
