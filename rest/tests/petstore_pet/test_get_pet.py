import allure
import pytest

from rest.resources import urls as urls
from rest.steps import support_steps as support_steps
from rest.steps import generate_json_steps as generate_json_steps
from rest.steps import request_steps as request_steps
from rest.steps import assert_steps as assert_steps

# Переменная для хранения id созданного питомца
ids = 1


# Получение записи питомца
@allure.step
@pytest.mark.smoke
@pytest.mark.regress
def test_get_pet():
    with allure.step("Сценарий проверки метода получения записи питомца"):
        request = request_steps.request_get(urls.pet_url_plus_query(ids))
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_json_is_not_none(request)


# Негативный сценарий получения записи питомца
@allure.step
@pytest.mark.parametrize(
    "scenario",
    [
        {"id": support_steps.generate_random_string(5)},
        {"id": support_steps.generate_random_email(5)}
    ],
    ids=["string", "some_query"]
)
@allure.step
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.negative
def test_get_pet(scenario):
    with allure.step("Сценарий проверки метода получения записи питомца"):
        request = request_steps.request_get(urls.pet_url_plus_query(scenario))
    with allure.step("Проверка ответа от API"):
        assert_steps.assert_json_is_not_none(request)
