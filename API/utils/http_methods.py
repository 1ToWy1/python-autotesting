import requests


class HTTP_Methods:
    headers = {"Content-Type": "application/json"}
    cookie = ""

    # GET-запрос
    @staticmethod
    def get(url):
        result = requests.get(url, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result

    # POST-запрос
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result

    # PUT-запрос
    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result

    # DELETE-запрос
    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HTTP_Methods.headers, cookies=HTTP_Methods.cookie)
        return result