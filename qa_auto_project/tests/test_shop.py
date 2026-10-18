import time

import pytest
from pages.login_page import LoginPage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.admin_page import AdminPage

@pytest.mark.id("1")
def test_auth_success(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    assert "manageProductsPage" in driver.current_url or login_page.LOGOUT_BUTTON, \
        "Ошибка авторизации: не удалось войти в систему под учетной записью администратора"

@pytest.mark.id("2")
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    login_page.logout()
    assert len(driver.find_elements(*LoginPage.USERNAME_INPUT)) > 0, \
        "Ошибка выхода из системы: форма авторизации не отображается после логаута"

@pytest.mark.id("3")
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    store = StorePage(driver)
    store.add_product_to_cart()
    store.go_to_cart()
    cart = CartPage(driver)
    assert cart.TOTAL_PRICE, \
        "Ошибка корзины: итоговая стоимость товара не отображается в корзине"

@pytest.mark.id("4")
def test_empty_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    store = StorePage(driver)
    store.go_to_cart()
    time.sleep(1)
    cart = CartPage(driver)
    assert cart.get_empty_message().is_displayed(), \
        "Ошибка пустой корзины: сообщение о том, что корзина пуста, отсутствует"

@pytest.mark.id("5")
def test_create_product(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    admin = AdminPage(driver)
    admin.create_product("Тест Товар", "Описание", "Категория", "1000", "/img/test.png")
    time.sleep(1)
    assert "manageProductsPage" in driver.current_url, \
        "Ошибка создания товара: административная панель управления товарами не открылась"


@pytest.mark.id("6")
def test_edit_product(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")

    admin = AdminPage(driver)
    admin.go_to_edit_product()
    assert "editProduct" in driver.current_url, \
        "Ошибка редактирования товара: страница редактирования не была открыта"

    new_title = "Обновленный Товар"
    new_price = "1500"
    admin.edit_product(new_title, new_price)
    time.sleep(1)
    assert new_title in driver.page_source, \
        "Ошибка редактирования: обновленное название товара не отображается на странице"


@pytest.mark.id("7")
def test_delete_product(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")

    admin = AdminPage(driver)

    # 1. Создаем уникальный товар
    unique_product_name = "Товар для удаления 123"
    admin.create_product(unique_product_name, "Описание", "Категория", "500", "/img/test.png")
    time.sleep(1)

    admin.open("manageProductsPage")
    time.sleep(1)

    # Проверяем, что созданный товар отображается на странице
    assert unique_product_name in driver.page_source, "Ошибка: созданный товар не найден на странице"

    # 2. Удаляем именно созданный товар
    admin.delete_product_by_name(unique_product_name)
    time.sleep(1.5)  # Ждем перерисовки Vue.js

    # 3. Проверяем, что товар исчез со страницы
    assert unique_product_name not in driver.page_source, \
        "Ошибка удаления: товар остался на странице и не был удален из DOM"


@pytest.mark.id("8")
def test_successful_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    store = StorePage(driver)
    store.add_product_to_cart()
    time.sleep(1)
    store.go_to_cart_and_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.fill_order_form("Иван", "Иванов", "Иванович", "ул. Ленина 1", "1234567812345678")
    time.sleep(1)
    checkout.finish_checkout()
    time.sleep(1.5)
    success_text = checkout.get_success_message_text()
    assert "ваш заказ успешно создан" in success_text.lower(), \
        f"Ошибка: Ожидалась надпись о создании заказа, но получено: '{success_text}'"


@pytest.mark.id("9")
def test_empty_checkout_validation(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    store = StorePage(driver)
    store.add_product_to_cart()
    time.sleep(1)
    store.go_to_cart_and_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.click_submit_empty_form()
    time.sleep(1)
    error_text = checkout.get_error_message_text()
    assert "Введите имя, фамилию, отчество" in error_text, \
        f"Ошибка валидации не сработала, получено: '{error_text}'"


@pytest.mark.id("10")
def test_max_order_amount_limit_bug(driver):
    """Тест на баг: система не должна разрешать оформление заказа свыше 100 000 ₽"""
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    store = StorePage(driver)
    store.add_product_to_cart()
    time.sleep(1)
    cart_btn = store.find_element(store.CART_ICON_BTN)
    driver.execute_script("arguments[0].click();", cart_btn)
    time.sleep(1)
    checkout = CheckoutPage(driver)
    total_amount = checkout.get_total_price()
    time.sleep(1)
    checkout_btn = store.find_element(store.PROCEED_TO_CHECKOUT_BTN)
    driver.execute_script("arguments[0].click();", checkout_btn)
    time.sleep(1)
    checkout.fill_order_form("Иван", "Иванов", "Иванович", "ул. Ленина 1", "1234567812345678")
    time.sleep(1)
    checkout.finish_checkout()
    time.sleep(1.5)
    success_text = checkout.get_success_message_text().lower()
    assert not (total_amount > 100000 and "ваш заказ успешно создан" in success_text), \
        f"БАГ ОБНАРУЖЕН: Сумма заказа составляет {total_amount} ₽ (превышает лимит 100 000 ₽), но система позволила успешно оформить заказ!"


@pytest.mark.id("11")
def test_checkout_fields_validation(driver):
    """Тест на баг: форма принимает некорректные данные в полях оформления заказа без валидации"""
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")
    store = StorePage(driver)
    store.add_product_to_cart()
    time.sleep(1)
    store.go_to_cart_and_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.fill_order_form("!!!", "123", "@@@", "неверный_адрес", "abc")
    time.sleep(1)
    checkout.finish_checkout()
    time.sleep(1.5)
    success_text = checkout.get_success_message_text().lower()
    order_created = "ваш заказ успешно создан" in success_text
    assert not order_created, \
        "БАГ ОБНАРУЖЕН: Система позволила успешно оформить заказ с полностью некорректными данными в форме (без валидации)!"

@pytest.mark.id("12")
def test_https_protocol(driver):
    """Тест на баг: проверка работы по HTTPS"""
    driver.get("http://91.197.96.80/")
    current_url = driver.current_url
    assert current_url.startswith("https://"), \
        f"Ошибка безопасности (баг): сайт доступен по небезопасному протоколу HTTP (Текущий URL: {current_url})"

@pytest.mark.id("13")
def test_max_product_quantity_limit_bug(driver):
    """Тест на баг: система позволяет добавить более 100 единиц товара через плюс в магазине"""
    login_page = LoginPage(driver)
    login_page.login("admin", "admin")

    store = StorePage(driver)
    store.open()
    time.sleep(1)

    # 1. Добавляем 1 товар, чтобы появился счетчик и кнопки плюс/минус
    store.add_product_to_cart()
    time.sleep(0.5)

    # 2. Нажимаем на плюс еще 100 раз (всего получится 101 товар)
    store.click_plus_button_multiple_times(100)
    time.sleep(1)

    # 3. Считываем значение количества прямо из карточки товара в магазине
    quantity_input = store.find_element(store.QUANTITY_INPUT)
    actual_quantity = int(quantity_input.get_attribute("value"))

    # 4. Проверяем баг: если количество превышает 100 — тест зафиксирует баг
    assert actual_quantity <= 100, \
        f"БАГ ОБНАРУЖЕН: Система позволила добавить {actual_quantity} шт. одного товара (превышен лимит в 100 единиц)!"