from requests import Response
from utils.http_methods import HttpMethods

BASE_URL = "https://rahulshettyacademy.com"
KEY = "?key=qaclick123"


class GoogleMapsApi:

    @staticmethod
    def create_new_place() -> Response:
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, coh 019",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = BASE_URL + "/maps/api/place/add/json" + KEY
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id: str) -> Response:
        get_resource = "/maps/api/place/get/json"
        get_url = BASE_URL + get_resource + KEY + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_place(place_id: str) -> Response:
        put_resource = "/maps/api/place/update/json"
        put_url = BASE_URL + put_resource + KEY
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления созданной локации (DELETE запрос)"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = BASE_URL + delete_resource + KEY
        print(delete_url)

        # Тело запроса содержит только place_id
        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete
        
