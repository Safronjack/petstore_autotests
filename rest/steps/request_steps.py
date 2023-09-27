import allure
import requests


# Отправляем GET запрос к эндпоинту
def request_get(url):
    with allure.step(f'Отправляем GET запрос к эндпоинту {url}'):
        request = requests.get(url, verify=False)
        return request


# Отправляем POST запрос к эндпоинту, где url = ссылка на эндпоинт, body = тело запроса
def request_post(url, body):
    with allure.step(f'Отправляем POST запрос к эндпоинту {url}'):
        request = requests.post(url, json=body, verify=False)
        return request


# Отправляем PUT запрос к эндпоинту, где url = ссылка на эндпоинт, body = тело запроса
def request_put(url, body):
    with allure.step(f'Отправляем PUT запрос к эндпоинту {url}'):
        request = requests.put(url, json=body, verify=False)
        return request


# Отправляем DELETE запрос к эндпоинту
def request_delete(url):
    with allure.step(f'Отправляем DELETE запрос к эндпоинту {url}'):
        request = requests.delete(url, verify=False)
        return request
