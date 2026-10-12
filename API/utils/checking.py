import json
from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code: int) -> None:
        assert response.status_code == status_code, f"Ожидался статус-код {status_code}, но получен {response.status_code}"
        print("Успешно. Статус код = " + str(response.status_code))


    @staticmethod
    def check_json_token(response: Response, expected_value: list) -> None:
        token = json.loads(response.text)
        assert list(token) == expected_value, f"Список полей {list(token)} не совпадает с ожидаемым {expected_value}"
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(response: Response, field_name: str, expected_value: str) -> None:
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Значение поля '{field_name}' равно '{check_info}', а ожидалось '{expected_value}'"
        print(field_name + " верен.")

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name: str, search_word: str) -> None:
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f"Слово '{search_word}' отсутствует в поле '{field_name}' (текст: '{check_info}')"
        print("Слово " + search_word + " присутствует.")
