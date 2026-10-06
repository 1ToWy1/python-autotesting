import pytest


# Первый тест
@pytest.mark.order(6)
def test_first():
    print("Выполняется первый тест")
    assert True


# Второй тест
@pytest.mark.order(2)
def test_second():
    print("Выполняется второй тест")
    assert True


# Третий тест
@pytest.mark.order(3)
def test_third():
    print("Выполняется третий тест")
    assert True


# Четвёртый тест
@pytest.mark.order(4)
def test_fourth():
    print("Выполняется четвёртый тест")
    assert True


# Пятый тест
@pytest.mark.order(5)
def test_fifth():
    print("Выполняется пятый тест")
    assert True


# Шестой тест
@pytest.mark.order(1)
def test_sixth():
    print("Выполняется шестой тест")
    assert True