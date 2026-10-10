from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Класс, содержащий тесты для создания локации"""

    def test_create_new_place(self):
        
        print('Метод POST')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print('Метод GET')
        result_get: Response = Google_maps_api.get_new_place(place_id)

        # Проверяем статус ответа
        assert result_get.status_code == 200

        # Проверяем данные полученной локации
        check_get = result_get.json()
        assert check_get.get('name') == 'Frontline house'
