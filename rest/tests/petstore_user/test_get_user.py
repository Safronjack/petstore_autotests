import allure
import pytest

from rest.resources import urls as urls
from rest.steps import support_steps as support_steps
from rest.steps import generate_json_steps as generate_json_steps
from rest.steps import request_steps as request_steps
from rest.steps import assert_steps as assert_steps

# Переменная для хранения имени созданного пользователя
some_name = ""


# Получение записи пользователя
@allure.step
@pytest.mark.smoke
@pytest.mark.regress
def test_get_user():
    with allure.step("Проверка метода получения записи пользователя"):
        global some_name
        request = request_steps.request_get(urls.user_url_plus_query(some_name))
    # assert request.json()["username"] == some_name


# Негативный сценарий получение записи пользователя
@allure.step
@pytest.mark.regress
@pytest.mark.negative
def test_get_user_negative():
    with allure.step("Негативный сценарий проверки метода получения записи пользователя"):
        request = request_steps.request_get(urls.user_url_plus_query(support_steps.generate_random_int(3)))
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_user_not_found(request)
