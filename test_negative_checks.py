from .pages.main_page import MainPage
from .pages.product_page import PageProduct

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    after_click_basket_page = PageProduct(browser, browser.current_url)
    after_click_basket_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    without_clock_basket = PageProduct(browser, browser.current_url)
    without_clock_basket.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    after_click_basket_page = PageProduct(browser, browser.current_url)
    after_click_basket_page.should_success_message_is_disappeared()