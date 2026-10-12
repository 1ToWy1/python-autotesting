import requests

from utils.logger import Logger


class HttpMethods:
    headers = {"Content-Type": "application/json"}
    cookie = ""

    # GET-запрос
    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(
            url,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # POST-запрос
    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # PUT-запрос
    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # DELETE-запрос
    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result
