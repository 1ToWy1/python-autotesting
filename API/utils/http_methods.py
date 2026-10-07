import requests


class HTTPMethods:
    headers = {"Content-Type": "application/json"}
    cookie = ""

    # GET-запрос
    @staticmethod
    def get(url):
        result = requests.get(url, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result

    # POST-запрос
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result

    # PUT-запрос
    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result

    # DELETE-запрос
    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result
