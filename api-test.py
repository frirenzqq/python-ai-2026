import requests
try:
    response=requests.get("https://catfact.ninja/fact", timeout=5)
    if response.status_code == 200:
        data=response.json()
        print(data["fact"])
    else:
        print(f"Ошибка сервера: {response.status_code}")
except requests.exceptions.ConnectionError:
    print("Нет подключения к интернету")
except requests.exceptions.Timeout:
    print("Сервер не ответил вовремя")
        



