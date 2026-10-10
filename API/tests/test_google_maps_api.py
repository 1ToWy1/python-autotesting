from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self) -> None:

        print('Метод POST')
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        # Проверяем, что локация успешно создана (код 200)
        assert result_post.status_code == 200

        print('Метод GET POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        assert result_get.status_code == 200

        print('Метод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверяем успешность PUT запроса и текст ответа
        assert result_put.status_code == 200
        check_put_json = result_put.json()
        assert check_put_json.get("msg") == "Address successfully updated"

        print('Метод GET PUT')
        result_get_after_put: Response = GoogleMapsApi.get_new_place(place_id)
        assert result_get_after_put.status_code == 200

        # Проверяем, что адрес в базе данных действительно изменился
        current_address = result_get_after_put.json().get("address")
        assert current_address == "100 Lenina street, RU"
        print("Тест успешно пройден: адрес обновлен корректно.")
