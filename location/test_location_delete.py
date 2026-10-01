import requests
from api import LocationAPI


class TestDeleteLocation:

    source_file = "place_ids.txt"
    active_places_file = "active_place_ids.txt"

    def test_delete_and_filter_locations(self):
        api = LocationAPI()

        # 1. Читаем исходный файл с 5 place_id
        with open(self.source_file, mode="r", encoding="utf-8") as file:
            place_ids = [line.strip() for line in file if line.strip()]

        assert len(place_ids) == 5, f"В файле должно быть 5 place_id, найдено: {len(place_ids)}"

        # 2. Удаляем 2-ю и 4-ю локации (индексы 1 и 3 в списке)
        ids_to_delete = [place_ids[1], place_ids[3]]

        for target_id in ids_to_delete:
            result_delete = api.delete_place(target_id)
            assert result_delete.status_code == 200

            delete_json = result_delete.json()
            assert delete_json.get("status") == "OK"
            print(f"Локация {target_id} успешно удалена")

        # 3. Проверяем через GET все 5 локаций и делим на существующие и удаленные
        existing_place_ids = []
        deleted_place_ids = []

        for place_id in place_ids:
            get_url = api.base_url + api.get_resource + api.key + "&place_id=" + place_id
            result_get = requests.get(get_url)

            if result_get.status_code == 200:
                print(f"Локация {place_id} СУЩЕСТВУЕТ")
                existing_place_ids.append(place_id)
            else:
                print(f"Локация {place_id} НЕ СУЩЕСТВУЕТ")
                deleted_place_ids.append(place_id)

        # Проверяем, что отобралось ровно 3 существующих и 2 удаленных
        assert len(existing_place_ids) == 3
        assert len(deleted_place_ids) == 2

        # 4. Записываем 3 существующие локации в новый файл
        with open(self.active_places_file, mode="w", encoding="utf-8") as file:
            for pid in existing_place_ids:
                file.write(f"{pid}\n")

        print(f"Существующие локации успешно записаны в файл {self.active_places_file}")