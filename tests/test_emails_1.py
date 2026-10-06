import pytest


@pytest.fixture
def prepare_email():
    print("Подготавливаем отправку письма...")
    print("Открываем почтовый сервис...")
    print("Авторизуем пользователя...")
        
    yield "Почтовый сервис готов"
    print("Тест завершён. Закрываем почтовый сервис...")


# Тест отправки первого письма
def test_send_first_email(prepare_email):
    print(prepare_email)
    print("Отправляем первое письмо...")

    assert True


# Тест отправки второго письма
def test_send_second_email(prepare_email):
    print(prepare_email)
    print("Отправляем второе письмо...")

    assert True
