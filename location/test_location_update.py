import requests
from api import LocationAPI


class TestUpdateLocation:

    file_name = "place_ids.txt"
    new_address = "100 New Side Layout, Cohen 10"

    def test_update_location_and_verify(self):
        # Создаем объект класса API
        api = LocationAPI()

        # Считываем первый place_id из файла
        with open(self.file_name, mode="r", encoding="utf-8") as file:
            place_ids = [line.strip() for line in file if line.strip()]

        assert len(place_ids) > 0, "Файл с place_id пуст"
        target_place_id = place_ids[0]

        # Вызываем метод через объект api
        result_put = api.update_place(target_place_id, self.new_address)

        assert result_put.status_code == 200
        put_json = result_put.json()
        assert put_json.get("msg") == "Address successfully updated"

        # Проверяем через GET
        get_url = api.base_url + api.get_resource + api.key + "&place_id=" + target_place_id
        result_get = requests.get(get_url)

        assert result_get.status_code == 200
        get_json = result_get.json()
        actual_address = get_json.get("address")

        assert actual_address == self.new_address
        print("Адрес успешно обновлен и проверен через GET")
