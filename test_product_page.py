import pytest
from .pages.main_page import MainPage
from .pages.product_page import PageProduct
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


# basket tests after authorization
class TestUserAddToBasketFromProductPage:
    # fixture for authorization in personal account, but to get into your personal account, we use not a login,
    # but registration
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "wsdrvbghy"
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page_login = LoginPage(browser, browser.current_url)
        page_login.register_new_user(email, password)
        page_login.should_be_authorized_user()

    # check the absence of a message about the successful addition of the product
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = MainPage(browser, link)
        page.open()
        without_click_basket = PageProduct(browser, browser.current_url)
        without_click_basket.should_not_be_success_message()

    # checking the addition of goods to the basket with authorization
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = MainPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.click_add_to_basket()
        page.solve_quiz_and_get_code()
        after_click_basket_page = PageProduct(browser, browser.current_url)
        after_click_basket_page.should_be_message_add_to_basket()
        after_click_basket_page.should_be_price_correct()


# checking the addition of goods to the basket without authorization
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    after_click_basket_page = PageProduct(browser, browser.current_url)
    after_click_basket_page.should_be_message_add_to_basket()
    after_click_basket_page.should_be_price_correct()


# check the presence of a link to enter in personal account
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


# check the transition to the authorization page
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


# check that there is no product in the basket
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageProduct(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page_from_items_page = BasketPage(browser, browser.current_url)
    basket_page_from_items_page.should_basket_without_items()
    basket_page_from_items_page.should_basket_message_without_items_is_present()


# broken test example
@pytest.mark.xfail(reason="we know that this test is fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    after_click_basket_page = PageProduct(browser, browser.current_url)
    after_click_basket_page.should_not_be_success_message()


# check the absence of a message about the successful addition of the product
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    without_click_basket = PageProduct(browser, browser.current_url)
    without_click_basket.should_not_be_success_message()


# learning to check that success message is disappeared, but we know that the test is not correct
@pytest.mark.xfail(reason="we know that this test is fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    after_click_basket_page = PageProduct(browser, browser.current_url)
    after_click_basket_page.should_success_message_is_disappeared()
