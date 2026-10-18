import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPage(BasePage):
    CREATE_PRODUCT_LINK = (By.XPATH, "//a[contains(@href, 'createProduct')]")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Наименование']")
    DESC_INPUT = (By.XPATH, "//input[@placeholder='Описание']")
    CAT_INPUT = (By.XPATH, "//input[@placeholder='Ожидаемая категория']")
    PRICE_INPUT = (By.XPATH, "//input[@placeholder='Цена']")
    IMG_INPUT = (By.XPATH, "//input[@placeholder='Image Source']")
    SUBMIT_CREATE_BTN = (By.XPATH, "//button[contains(text(), 'Создать товар')]")
    DELETE_BTN = (By.XPATH, "(//button[span[text()='delete']])[last()]")
    EDIT_PRODUCT_LINK = (By.XPATH, "(//a[contains(@href, 'editProduct')])[1]")
    SUBMIT_EDIT_BTN = (By.XPATH, "//*[@id=\"app\"]/div/div/div[1]/div/div[2]/div/button")

    def create_product(self, name, desc, cat, price, img):
        self.open("createProduct")
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.DESC_INPUT, desc)
        self.enter_text(self.CAT_INPUT, cat)
        self.enter_text(self.PRICE_INPUT, price)
        self.enter_text(self.IMG_INPUT, img)
        self.click(self.SUBMIT_CREATE_BTN)

    def delete_product(self):
        self.open("manageProductsPage")
        time.sleep(1)
        delete_btn = self.find_element(self.DELETE_BTN)
        self.driver.execute_script("arguments[0].click();", delete_btn)

    def go_to_edit_product(self):
        self.open("manageProductsPage")
        self.click(self.EDIT_PRODUCT_LINK)

    def edit_product(self, new_name, new_price):
        name_input = self.find_element(self.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(new_name)

        price_input = self.find_element(self.PRICE_INPUT)
        price_input.clear()
        price_input.send_keys(new_price)

        self.click(self.SUBMIT_EDIT_BTN)

    def delete_product_by_name(self, product_name):
            self.open("manageProductsPage")
            time.sleep(1)

            # Динамический XPath: находит карточку товара, содержащую наше название, и берет в ней кнопку удаления
            xpath = f"//div[contains(@class, 'store-card')][.//div[contains(text(), '{product_name}')]]//button[contains(., 'delete')]"
            delete_btn = self.find_element((By.XPATH, xpath))
            self.driver.execute_script("arguments[0].click();", delete_btn)

