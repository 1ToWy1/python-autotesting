from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:

    def test_create_new_place(self):

        print('Метод POST')
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        # Проверяем, что локация успешно создана (код 200)
        Checking.check_status_code(result_post, 200)

        print('Метод GET POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print('Метод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверяем успешность PUT запроса и текст ответа
        Checking.check_status_code(result_put, 200)
        check_put_json = result_put.json()
        assert check_put_json.get("msg") == "Address successfully updated"

        print('Метод GET PUT')
        result_get_after_put: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get_after_put, 200)

        # Проверяем, что адрес в базе данных действительно изменился
        current_address = result_get_after_put.json().get("address")
        assert current_address == "100 Lenina street, RU"
        print("Тест успешно пройден: адрес обновлен корректно.")

        print('Метод DELETE')
        result_delete = GoogleMapsApi.delete_new_place(place_id)

        # Проверяем, что запрос прошел успешно (статус 200)
        Checking.check_status_code(result_delete, 200)
        check_delete_json = result_delete.json()

        # Проверяем тело ответа на наличие "status": "OK"
        assert check_delete_json.get("status") == "OK"
        print("Локация успешно удалена из базы данных.")

        print('Метод GET DELETE')
        # Проверяем с помощью GET запроса, что локация действительно удалена
        result_get = GoogleMapsApi.get_new_place(place_id)

        # Ожидаем статус 404, так как локация удалена
        Checking.check_status_code(result_get, 404)
        print("Проверка успешна: локация больше не существует, получен статус 404.")
