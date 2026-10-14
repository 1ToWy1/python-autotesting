import requests

from typing import Any
from requests import Response

from utils.logger import Logger


class HttpMethods:
    headers: dict[str, str] = {"Content-Type": "application/json"}
    cookie: str = ""

    # GET-запрос
    @staticmethod
    def get(url: str) -> Response:
        Logger.add_request(url, method="GET")
        result: Response = requests.get(
            url,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # POST-запрос
    @staticmethod
    def post(url: str, body: dict[str, Any]) -> Response:
        Logger.add_request(url, method="POST")
        result: Response = requests.post(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # PUT-запрос
    @staticmethod
    def put(url: str, body: dict[str, Any]) -> Response:
        Logger.add_request(url, method="PUT")
        result: Response = requests.put(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # DELETE-запрос
    @staticmethod
    def delete(url: str, body: dict[str, Any]) -> Response:
        Logger.add_request(url, method="DELETE")
        result: Response = requests.delete(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result
