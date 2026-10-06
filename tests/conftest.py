import pytest


# Фикстура подготовки почтового сервиса
@pytest.fixture
def prepare_email():
    print("Подготавливаем отправку письма...")
    print("Открываем почтовый сервис...")
    print("Авторизуем пользователя...")

    yield "Почтовый сервис готов"

    print("Тест завершён. Закрываем почтовый сервис...")


# Фикстура с областью действия function
@pytest.fixture(scope="function")
def function_scope():
    print("Запуск фикстуры function")

    yield

    print("Завершение фикстуры function")


# Фикстура с областью действия module
@pytest.fixture(scope="module")
def module_scope():
    print("Запуск фикстуры module")

    yield

    print("Завершение фикстуры module")