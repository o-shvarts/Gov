import requests

url = 'https://petfriends.skillfactory.ru/api/key'
email = 'o_schwarz@mail.ru'
password = '1z2x3c4v'

headers = {
    'email': email,
    'password': password
}

# Отправка GET-запроса с заголовками авторизации
response = requests.get(url, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    # Получение данных из ответа
    data = response.json()
    print(data)
else:
    print('Ошибка при выполнении запроса:', response.status_code)