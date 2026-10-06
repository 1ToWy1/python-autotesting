import pytest


# Фикстура выполняется перед каждым тестом
@pytest.fixture(scope="function")
def function_scope():
    print("Подготовка перед тестом")

    yield
    print("Очистка после теста")


# Фикстура выполняется один раз для всего модуля
@pytest.fixture(scope="module")
def module_scope():
    print("Подготовка перед запуском модуля")

    yield
    print("Очистка после завершения модуля")
