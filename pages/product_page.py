from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()

    def quiz(self):
        self.solve_quiz_and_get_code()