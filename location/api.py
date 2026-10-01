import requests


class LocationAPI:
    base_url = "https://rahulshettyacademy.com"
    post_resource = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    put_resource = "/maps/api/place/update/json"
    delete_resource = "/maps/api/place/delete/json"
    key = "?key=qaclick123"

    def update_place(self, place_id, new_address):
        put_url = self.base_url + self.put_resource + self.key
        headers = {"Content-Type": "application/json"}
        json_body = {
            "place_id": place_id,
            "address": new_address,
            "key": "qaclick123"
        }

        print(f"\n[PUT Request] URL {put_url}")
        print(f"[PUT Request] Body {json_body}")

        response = requests.put(put_url, json=json_body, headers=headers)
        return response

    def delete_place(self, place_id):
        delete_url = self.base_url + self.delete_resource + self.key
        headers = {"Content-Type": "application/json"}
        json_body = {
            "place_id": place_id
        }

        print(f"\n[DELETE Request] URL {delete_url}")
        print(f"[DELETE Request] Body {json_body}")

        response = requests.delete(delete_url, json=json_body, headers=headers)
        return response
