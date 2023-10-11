import requests
import datetime

params = {
    "order": "desc",
    "sort": "activity",
    "tagged": "python",
    "fromdate": int((datetime.datetime.now() - datetime.timedelta(days=2)).timestamp()),
    "site": "stackoverflow"
}

response = requests.get("https://api.stackexchange.com/2.3/questions", params=params)

if response.status_code == 200:
    questions = response.json()['items']

    for question in questions:
        print("Заголовок:", question['title'])
        print("Ссылка: ", question['link'])
        print("---------------------------")
else:
    print("Ошибка при выполнении запроса: ", response.status_code)
