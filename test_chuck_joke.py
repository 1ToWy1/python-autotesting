import requests

class TestChuckJoke:
    
    url = "https://api.chucknorris.io"

    # Тест получения случайной шутки
    def test_create_random_joke(self):
        # Определяем категорию
        category = "dev"
        # Формируем URL запроса
        path_random_joke = f"/jokes/random?category={category}"
        url_random_joke = self.url + path_random_joke
        print(f"URL запроса: {url_random_joke}")

        # Отправляем GET-запрос
        result = requests.get(url_random_joke, timeout=10)
        print(f"Статус-код: {result.status_code}")

        # Проверяем статус-код
        assert result.status_code == 200, f"Ожидался статус 200, получен {result.status_code}"
        print("Статус-код корректен")

        # Получаем JSON-ответ
        check_joke = result.json()
        print(f"Ответ: {check_joke}")

        # Получаем категорию
        joke_category = check_joke.get("categories")
        # Проверяем категорию
        assert category in joke_category, f"Ожидалась категория {category}, получено {joke_category}"
        print("Категория корректна")

        # Получаем текст шутки
        joke_text = check_joke.get("value")
        # Проверяем наличие Chuck
        assert "Chuck" in joke_text, "Имя Chuck отсутствует в шутке"
        print("Имя Chuck присутствует в шутке")
        # Выводим шутку
        print(f"Шутка: {joke_text}")

# Создаём объект класса
start = TestChuckJoke()
start.test_create_random_joke()
