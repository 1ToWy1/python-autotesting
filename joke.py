import requests

# URL запроса
url = "https://api.chucknorris.io/jokes/lGB67Ua_QtKibYgB2GdMEA"
print("URL запроса:", url)

result = requests.get(url, timeout=10)

# Проверка статус-кода
print("Статус-код:", result.status_code)
assert result.status_code == 200, (
    "Ошибка: статус-код не равен ожидаемому!"
)

print("ОР == ФР")

result.encoding = "utf-8"
print("Ответ в формате JSON:")
print(result.text)
