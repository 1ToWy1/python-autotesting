import requests


class TestNewLocation:
    base_url = "https://rahulshettyacademy.com"
    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    key = "?key=qaclick123"
    file_name = "place_ids.txt"

    def test_create_five_locations_and_save_to_file(self):
        post_url = self.base_url + self.post_resource + self.key

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # Открываем текстовый файл для записи place_id
        with open(self.file_name, mode="w", encoding="utf-8") as file:
            for i in range(5):
                result_post = requests.post(post_url, json=json_for_create_new_location)
                assert result_post.status_code == 200

                check_response_post = result_post.json()
                place_id = check_response_post.get("place_id")
                print(f"[{i + 1}] Создан place_id: {place_id}")

                # Записываем place_id в файл (каждый с новой строки)
                file.write(f"{place_id}\n")

        print(f"Все 5 place_id успешно записаны в файл {self.file_name}")

    def test_check_locations_from_file_via_get(self):
        # Открываем и читаем place_id
        with open(self.file_name, mode="r", encoding="utf-8") as file:
            # Считываем строки и убираем символ переноса строки \n
            place_ids = [line.strip() for line in file if line.strip()]

        print(f"Проверяем place_id из файла: {place_ids}")

        # Для каждого place_id из файла отправляем метод GET
        for place_id in place_ids:
            get_url = self.base_url + self.get_resource + self.key + "&place_id=" + place_id
            print(f"GET URL: {get_url}")

            result_get = requests.get(get_url)
            print(f"Ответ сервера: {result_get.json()}")

            # Проверяем статус-код ответа
            print(f"Статус-код: {result_get.status_code}")
            assert result_get.status_code == 200
            print(f"Статус-код GET корректен для place_id: {place_id}")