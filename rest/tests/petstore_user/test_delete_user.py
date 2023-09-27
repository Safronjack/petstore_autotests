import allure
import pytest

from rest.resources import urls as urls
from rest.steps import support_steps as support_steps
from rest.steps import generate_json_steps as generate_json_steps
from rest.steps import request_steps as request_steps
from rest.steps import assert_steps as assert_steps

# Переменная для хранения имени созданного пользователя
some_name = ""


# Негативный сценарий удаления записи пользователя
@allure.step
@pytest.mark.regress
@pytest.mark.negative
def test_delete_user_negative():
    with allure.step("Негативный сценарий метода удаления записи пользователя"):
        request = request_steps.request_delete(urls.user_url)
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_status_code_equal_405(request)


# Сценарий удаления записи пользователя
@allure.step
@pytest.mark.smoke
@pytest.mark.regress
def test_delete_user():
    with allure.step("Проверка сценария удаления записи пользователя"):
        request = request_steps.request_delete(urls.user_url_plus_query(some_name))
    # assert_steps.assert_status_code_equal_200(request)
