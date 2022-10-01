from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
#    def should_be_login_link(self):
#        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

#    def should_be_basket_link(self):
#        assert self.is_element_present(*MainPageLocators.BASKET_LINK), "Basket button is not presented"

#    def go_to_login_page(self):
#        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        login_link.click()

#    def click_add_to_basket(self):
#        basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
#        basket_link.click()
