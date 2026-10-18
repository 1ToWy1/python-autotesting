from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    EMPTY_CART_MSG = (By.XPATH, "//*[contains(text(), 'в корзине пока пусто')]")
    TOTAL_PRICE = (By.XPATH, "//*[contains(text(), 'Итого:')]")
    CHECKOUT_BTN = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    def get_empty_message(self):
        return self.find_element(self.EMPTY_CART_MSG)

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BTN)