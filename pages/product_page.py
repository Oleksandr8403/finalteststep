from .base_page import BasePage
from .locators import ProductPageLocators


# This class describes checks on the product page
class PageProduct(BasePage):
    def should_be_message_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK).text == self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK).text, "Name book not correct"

    def should_be_price_correct(self):
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRICE_BOOK).text == self.browser.find_element(
            *ProductPageLocators.PRICE_BOOK).text, "Price not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but shuold be"
