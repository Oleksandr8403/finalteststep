from .pages.main_page import MainPage
from .pages.product_page import PageProduct

def test_guest_should_see_basket_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    after_click_basket_page = PageProduct(browser, browser.current_url)
    after_click_basket_page.should_be_message_add_to_basket()
    after_click_basket_page.should_be_price_correct()
