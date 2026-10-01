import requests


class TestChuckCategories:
    # URL API
    url = "https://api.chucknorris.io"

    # Тест получения шутки для каждой категории
    def test_get_joke_for_each_category(self):
        # Получаем список категорий
        path_categories = "/jokes/categories"
        url_categories = self.url + path_categories
        print(f"URL запроса: {url_categories}")

        result = requests.get(url_categories, timeout=10)
        print(f"Статус-код: {result.status_code}")

        # Проверяем статус-код
        assert result.status_code == 200, f"Ожидался статус 200, получен {result.status_code}"
        print("Статус-код корректен")

        # Получаем категории
        categories = result.json()
        print(f"Категории: {categories}")

        # Проверяем каждую категорию
        for category in categories:
            path_random_joke = f"/jokes/random?category={category}"
            url_random_joke = self.url + path_random_joke
            print(f"URL шутки: {url_random_joke}")

            joke_result = requests.get(url_random_joke, timeout=10)

            assert joke_result.status_code == 200, (
                f"Для категории {category} ожидался статус 200, "
                f"получен {joke_result.status_code}"
            )

            joke = joke_result.json()
            print(f"Категория: {category}")
            print(f"Шутка: {joke.get('value')}")
            print("--------------------")


# Создаем объект класса
start = TestChuckCategories()
start.test_get_joke_for_each_category()
