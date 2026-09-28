import requests



class TestUserCategory:

    url = 'https://api.chucknorris.io'

    # Метод для тестирования получения шутки по категории
    def test_get_joke_by_user_category(self):

        # Формируем путь для получения всех категорий
        path_categories = '/jokes/categories'

        # Формируем полный URL
        url_categories = self.url + path_categories

        # Выводим URL запроса
        print(f'URL запроса: {url_categories}')

        # Отправляем GET-запрос
        result = requests.get(url_categories)

        # Проверяем статус-код
        print(f'Статус-код: {result.status_code}')
        assert result.status_code == 200
        print('Статус-код корректен')

        # Получаем список категорий
        categories = result.json()

        # Выводим доступные категории
        print(f'Доступные категории: {categories}')

        # Просим пользователя выбрать категорию
        while True:

            # Получаем категорию от пользователя
            category = input('Введите категорию шутки: ').lower()

            # Проверяем, существует ли такая категория
            if category in categories:
                print('Категория существует')
                break

            # Если категории нет, предлагаем попробовать ещё раз
            print('Такой категории нет.')
            print('Попробуйте выбрать категорию из списка.')

        # Формируем путь для получения шутки
        path_random_joke = f'/jokes/random?category={category}'

        # Формируем полный URL
        url_random_joke = self.url + path_random_joke

        # Выводим URL запроса
        print(f'URL шутки: {url_random_joke}')

        # Отправляем запрос для получения шутки
        result_joke = requests.get(url_random_joke)

        # Проверяем статус-код
        assert result_joke.status_code == 200
        print('Шутка успешно получена')

        # Получаем JSON-ответ
        joke = result_joke.json()

        # Выводим шутку
        print(f'Шутка: {joke.get("value")}')


# Создаём объект класса
start = TestUserCategory()

# Запускаем тест
start.test_get_joke_by_user_category()