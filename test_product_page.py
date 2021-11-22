from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    time.sleep(2)
    product_page.click_add_to_basket()
    time.sleep(2)
    product_page.solve_quiz_and_get_code()
    time.sleep(2)