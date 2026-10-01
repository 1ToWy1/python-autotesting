import requests

class UserCategory:
    url = "https://api.chucknorris.io"

    def get_joke_by_user_category(self):
        path_categories = "/jokes/categories"
        url_categories = self.url + path_categories
        print(f"URL запроса: {url_categories}")

        result = requests.get(url_categories, timeout=10)
        print(f"Статус-код: {result.status_code}")

        assert result.status_code == 200, (
            f"Ожидался статус 200, получен {result.status_code}"
        )
        print("Статус-код корректен")

        categories = result.json()
        print(f"Доступные категории: {categories}")

        while True:
            category = input("Введите категорию шутки: ").lower()

            if category in categories:
                print("Категория существует")
                break

            print("Такой категории нет.\nПопробуйте выбрать категорию из списка.")

        path_random_joke = f"/jokes/random?category={category}"
        url_random_joke = self.url + path_random_joke
        print(f"URL шутки: {url_random_joke}")

        result_joke = requests.get(url_random_joke, timeout=10)

        assert result_joke.status_code == 200, (
            f"Ожидался статус 200, получен {result_joke.status_code}"
        )
        print("Шутка успешно получена")

        joke = result_joke.json()
        print(f"Шутка: {joke.get('value')}")


if __name__ == "__main__":
    start = UserCategory()
    start.get_joke_by_user_category()
