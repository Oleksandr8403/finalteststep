from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.password = ""
        self.email = ""

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "current url NOT ok"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        pole_mail = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_MAIL)
        pole_mail.send_keys(self.email)
        pole_password1 = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_PASSWORD1)
        pole_password1.send_keys(self.password)
        pole_password2 = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_PASSWORD2)
        pole_password2.send_keys(self.password)
        button_reg = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_BUTTON)
        button_reg.click()
