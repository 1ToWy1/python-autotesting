import requests

url = "https://api.chucknorris.io/jokes/lGB67Ua_QtKibYgB2GdMEA"
print("URL запроса:", url)
result = requests.get(url)
print("Статус код: " + str(result.status_code))
assert 200 == result.status_code, "Ошибка: Статус код не равен ожидаемому!"
if result.status_code == 200:
    print("ОР == ФР")
else:
    print("Провал, статус код не верен!")
result.encoding = 'utf-8'
print("Ответ в формате JSON:")
print(result.text)
