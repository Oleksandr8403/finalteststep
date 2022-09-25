from .base_page import BasePage
from .locators import ProductPageLocators

class PageProduct(BasePage):
    def should_be_message_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK).text == self.browser.find_element(*ProductPageLocators.ALERT_BOOK).text, "Name book not correct"

    def should_be_price_correct(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRICE_BOOK).text == self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text, "Price not correct"