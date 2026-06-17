import requests
def main():
    user_id = int(input("Введите номер ID: "))
    params = {"userId": user_id}    
    try:
        response=requests.get("https://jsonplaceholder.typicode.com/posts", params=params, timeout=5)
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Потерно соеденение с интернотом")
    except requests.exceptions.Timeout:
        print("Время на ответ вышло")
