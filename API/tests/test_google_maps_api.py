from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Класс, содержащий тесты для создания локации"""

    def test_create_new_place(self):
        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        print(f"Статус-код ответа: {result_post.status_code}")