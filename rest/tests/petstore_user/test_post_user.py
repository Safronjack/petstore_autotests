import allure
import pytest

from rest.resources import urls as urls
from rest.steps import support_steps as support_steps
from rest.steps import generate_json_steps as generate_json_steps
from rest.steps import request_steps as request_steps
from rest.steps import assert_steps as assert_steps

# Переменная для хранения имени созданного пользователя
some_name = ""


# Негативный сценарий создания пользователя
@allure.step
@pytest.mark.parametrize(
    "scenario",
    [
        {"id": support_steps.generate_random_string(5)},
        {"id": support_steps.generate_random_email(5)}
    ],
    ids=["string", "some_query"]
)
@pytest.mark.regress
@pytest.mark.negative
def test_post_user_negative(scenario):
    with allure.step("Негативный сценарий отправки запроса на создание пользователя"):
        url = urls.user_url
        body = scenario
        request = request_steps.request_post(url, body)
    with allure.step("Проверка ответа от API"):
        assert request.json()["message"] == "something bad happened"


# # Создание пользователя
@allure.step
@pytest.mark.smoke
@pytest.mark.regress
def test_post_user():
    with allure.step("Сценарий отправки запроса на создание пользователя"):
        global some_name
        url = urls.user_url
        body = generate_json_steps.generate_json_post_user_with_all_params()
        some_name = body["username"]
        request = request_steps.request_post(url, body)
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_status_code_equal_200(request)
