import requests
from environs import Env

def get_request():
    
    env = Env()
    env.read_env()
    bearer_token=env("BEARER_TOKEN")
    url = "http://127.0.0.1:8000/api/open/"      #"https://kuzovnojmaster.ru/api/"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json()
            
    except requests.exceptions.RequestException as e:
        return(f"Ошибка при выполнении запроса: {e}")


def retrieve_request():
    
    env = Env()
    env.read_env()
    bearer_token=env("BEARER_TOKEN")
    url = "http://127.0.0.1:8000/api/open/125/"      #"https://kuzovnojmaster.ru/api/"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json()
            
    except requests.exceptions.RequestException as e:
        return(f"Ошибка при выполнении запроса: {e}")