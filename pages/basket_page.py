from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_basket_without_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items is in basket, but should not be"

    def should_basket_message_without_items_is_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_WITHOUT_ITEMS_MESSAGE), "Message about basket whithout items missing"
