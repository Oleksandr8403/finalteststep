from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.col-sm-6.register_form")

class ProductPageLocators():
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    ALERT_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ALERT_PRICE_BOOK = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")