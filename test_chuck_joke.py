import requests


# Общий класс для тестов
class TestChuckJoke:

    # URL API
    url = 'https://api.chucknorris.io'

    # Метод для тестирования получения случайной шутки
    def test_create_random_joke(self):

        # Определяем категорию шутки
        category = 'dev'

        # Формируем путь для получения случайной шутки
        path_random_joke = f'/jokes/random?category={category}'

        # Формируем полный URL
        url_random_joke = self.url + path_random_joke

        # Выводим URL, по которому отправляем запрос
        print(f'URL запроса: {url_random_joke}')

        # Отправляем GET-запрос
        result = requests.get(url_random_joke)

        # Выводим статус-код ответа
        print(f'Статус-код: {result.status_code}')

        # Проверяем статус-код
        assert result.status_code == 200
        print('Статус-код корректен')

        # Получаем ответ в формате JSON
        check_joke = result.json()

        # Выводим JSON-ответ
        print(f'Ответ: {check_joke}')

        # Получаем категорию из ответа
        joke_category = check_joke.get('categories')

        # Проверяем соответствие категории
        assert category in joke_category
        print('Категория корректна')

        # Получаем текст шутки
        joke_text = check_joke.get('value')

        # Проверяем наличие имени Chuck в тексте шутки
        assert 'Chuck' in joke_text
        print('Имя Chuck присутствует в шутке')

        # Выводим саму шутку
        print(f'Шутка: {joke_text}')


# Создаем объект класса
start = TestChuckJoke()

# Запускаем тест
start.test_create_random_joke()