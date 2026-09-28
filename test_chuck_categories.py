import requests


# Общий класс для тестов
class TestChuckCategories:

    # URL API
    url = 'https://api.chucknorris.io'

    # Метод для получения шутки по каждой категории
    def test_get_joke_for_each_category(self):

        # Формируем путь для получения всех категорий
        path_categories = '/jokes/categories'

        # Формируем полный URL
        url_categories = self.url + path_categories

        # Выводим URL запроса
        print(f'URL запроса: {url_categories}')

        # Отправляем GET-запрос для получения всех категорий
        result = requests.get(url_categories)

        # Выводим статус-код ответа
        print(f'Статус-код: {result.status_code}')

        # Проверяем, что запрос выполнен успешно
        assert result.status_code == 200
        print('Статус-код корректен')

        # Получаем список категорий из JSON-ответа
        categories = result.json()

        # Выводим список всех категорий
        print(f'Категории: {categories}')

        # Перебираем каждую категорию
        for category in categories:

            # Формируем путь для получения случайной шутки
            path_random_joke = f'/jokes/random?category={category}'

            # Формируем полный URL запроса
            url_random_joke = self.url + path_random_joke

            # Выводим URL запроса
            print(f'URL шутки: {url_random_joke}')

            # Отправляем GET-запрос
            joke_result = requests.get(url_random_joke)

            # Проверяем статус-код
            assert joke_result.status_code == 200

            # Получаем ответ в формате JSON
            joke = joke_result.json()

            # Выводим полученную шутку
            print(f'Категория: {category}')
            print(f'Шутка: {joke.get("value")}')
            print('--------------------')


# Создаем объект класса
start = TestChuckCategories()

# Запускаем тест
start.test_get_joke_for_each_category()