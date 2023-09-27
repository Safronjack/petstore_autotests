import allure
import pytest

from rest.resources import urls as urls
from rest.steps import support_steps as support_steps
from rest.steps import generate_json_steps as generate_json_steps
from rest.steps import request_steps as request_steps
from rest.steps import assert_steps as assert_steps

# Переменная для хранения имени созданного пользователя
some_name = ""


# Негативный сценарий изменения карточки пользователя
@allure.step
@pytest.mark.regress
@pytest.mark.negative
def test_put_user_negative():
    with allure.step("Негативный сценарий проверки метода изменения карточки пользователя"):
        url = urls.user_url
        body = generate_json_steps.generate_json_post_user_with_all_params()
        request = request_steps.request_put(url, body)
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_status_code_equal_405(request)


# Сценарий изменения карточки пользователя
@allure.step
@pytest.mark.regress
def test_put_user():
    with allure.step("Проверка метода изменения карточки пользователя"):
        global some_name
        body = generate_json_steps.generate_json_post_user_with_all_params()
        some_name = body["username"]
        request = request_steps.request_put(urls.user_url_plus_query("Karasik"), body)
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_status_code_equal_200(request)
