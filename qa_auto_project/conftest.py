import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Указываем путь к chromedriver.exe, который лежит в корне проекта
    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()